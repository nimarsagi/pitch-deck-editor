#!/usr/bin/env python3
"""
score.py — the deterministic scorer for the Pitch Deck Editor.

Why this exists (60/30/10): converting a filled score sheet into a 1-10 number
is arithmetic — summing sixteen weighted criteria, dividing, applying a two-branch
linear map, subtracting capped defect deductions. That is orchestration, not
judgment: it must be identical every time and checkable by machine. The rubric
files (reference/scoring-rubric*.md) stay the source of truth for *what a level
means* and *what a defect costs*; a human still assigns each 0-3 level and reads
each defect. This script only does the maths those files describe, so the maths
can never silently drift from the worked examples again.

Usage:
    python3 tools/score.py --selftest        # reproduce the four committed scorecards
    python3 tools/score.py                    # same as --selftest

Or import and call score(...) with a filled sheet.
"""

from __future__ import annotations

from decimal import Decimal, ROUND_HALF_UP


def r1(x: float) -> float:
    """Round to one decimal, half-up — the convention the committed scorecards
    use (7.1 - 2.75 = 4.35 -> 4.4, not 4.3). Fixed here so the rounding rule is
    part of the code, not an accident of whichever float library ran last."""
    return float(Decimal(str(x)).quantize(Decimal("0.1"), rounding=ROUND_HALF_UP))

# ---------------------------------------------------------------------------
# Rubric structure. Identical for both the investor and sales rubrics:
# five Tier-A criteria (x3, max 9), nine Tier-B (x2, max 6), two Tier-C (x1, max 3).
# Full-deck maximum = 45 + 54 + 6 = 105 raw points.
# ---------------------------------------------------------------------------
WEIGHTS = {"A": 3, "B": 2, "C": 1}
TIERS = {
    "A1": "A", "A2": "A", "A3": "A", "A4": "A", "A5": "A",
    "B1": "B", "B2": "B", "B3": "B", "B4": "B", "B5": "B",
    "B6": "B", "B7": "B", "B8": "B", "B9": "B",
    "C1": "C", "C2": "C",
}

# Sales rubric only: any of these at level 0 caps the final score at 6.9
# (reference/scoring-rubric-sales.md, "The high-severity gate"). A3 is exempt
# when it is N/A, which is handled naturally — an N/A criterion has no level.
SALES_GATE = {"A1", "A2", "A3", "A4", "B5", "B7"}
SALES_GATE_CAP = 6.9


def raw_points(levels: dict[str, object]) -> tuple[int, int]:
    """Return (earned, possible) raw points. A level of 'NA' drops the criterion
    from *both* earned and possible (the N/A valve). Levels are 0-3."""
    earned = possible = 0
    for crit, tier in TIERS.items():
        lvl = levels.get(crit)
        if lvl == "NA" or lvl is None:
            continue  # N/A: out of both numerator and denominator
        w = WEIGHTS[tier]
        earned += int(lvl) * w
        possible += 3 * w
    return earned, possible


def convert(p: float) -> float:
    """The anchored raw->10 map from the rubric. Straight-Target (p=2/3) -> 8.0."""
    if p <= 0.667:
        return 1.0 + 10.5 * p
    return 8.0 + 6.0 * (p - 0.667)


def design_band(score: float) -> str:
    for lo, name in [
        (9.0, "Exceptional"), (8.0, "Strong"), (6.5, "Good, with named gaps"),
        (5.0, "Solid core, material gaps"), (3.5, "Structurally incomplete"),
        (0.0, "Not ready"),
    ]:
        if score >= lo:
            return name
    return "Not ready"


def send_band(deduction: float) -> str:
    d = abs(deduction)
    if d == 0:
        return "Send-ready"
    if d <= 1.0:
        return "Minor defects"
    if d <= 2.0:
        return "Do not send yet"
    return "Unfinished"


def score(levels: dict[str, object], *, rubric: str = "investor",
          defects: float = 0.0) -> dict:
    """Score one filled sheet.

    levels:  {"A1": 2, "A2": 3, ..., "C2": 2}, values 0-3 or "NA".
    rubric:  "investor" or "sales" (only affects the high-severity gate).
    defects: total defect deduction as a NEGATIVE number (e.g. -2.75), or 0.0.
             Capped at -3.0 and the artifact score is floored at 1.0.
    """
    earned, possible = raw_points(levels)
    p = earned / possible
    design = r1(convert(p))

    # Sales high-severity gate: any gate criterion at level 0 caps the final score.
    gate_fired = None
    capped_design = design
    if rubric == "sales":
        tripped = [c for c in SALES_GATE if levels.get(c) == 0]
        if tripped:
            gate_fired = sorted(tripped)
            capped_design = min(capped_design, SALES_GATE_CAP)

    # Artifact lens: apply capped defect load, floor at 1.0.
    ded = max(defects, -3.0)  # defects are negative; cap the magnitude at 3.0
    artifact = r1(max(capped_design + ded, 1.0))

    return {
        "earned": earned, "possible": possible, "p": p,
        "design": design, "design_band": design_band(design),
        "gate_fired": gate_fired, "capped_design": r1(capped_design),
        "defect_load": round(ded, 2), "artifact": artifact,
        "send_band": send_band(ded),
    }


def show(name: str, result: dict, expected: float | None = None) -> bool:
    tag = ""
    ok = True
    if expected is not None:
        ok = abs(result["design"] - expected) < 0.05
        tag = f"   [expected {expected} -> {'MATCH' if ok else 'MISMATCH'}]"
    print(f"{name}")
    print(f"  raw {result['earned']}/{result['possible']}  "
          f"p={result['p']:.4f}  ->  as designed {result['design']} "
          f"({result['design_band']}){tag}")
    if result["gate_fired"]:
        print(f"  high-severity gate fired on {', '.join(result['gate_fired'])} "
              f"-> capped at {result['capped_design']}")
    if result["defect_load"] != 0.0:
        print(f"  defect load {result['defect_load']:+} ({result['send_band']}) "
              f"-> as the file stands {result['artifact']}")
    print()
    return ok


# ---------------------------------------------------------------------------
# Self-test: the four committed pass-1 scorecards. Running this file reproduces
# every number that appears in output/*.md — the "commit the trace" for arithmetic.
# ---------------------------------------------------------------------------
CASES = [
    ("airbnb-seed-2008 (investor)", "investor",
     {"A1": 2, "A2": 3, "A3": 0, "A4": 1, "A5": 3,
      "B1": 3, "B2": 2, "B3": 3, "B4": 1, "B5": 1, "B6": 2, "B7": 2, "B8": 0, "B9": 1,
      "C1": 2, "C2": 2}, -2.75, 7.1),
    ("coinbase-zlides-reconstruction (investor)", "investor",
     {"A1": 2, "A2": 1, "A3": 2, "A4": 0, "A5": 2,
      "B1": 0, "B2": 1, "B3": 1, "B4": 2, "B5": 0, "B6": 0, "B7": 0, "B8": 0, "B9": 2,
      "C1": 3, "C2": 2}, -1.0, 4.8),
    ("immediately-sales-2015 (sales)", "sales",
     {"A1": 2, "A2": 2, "A3": 2, "A4": 1, "A5": 1,
      "B1": 0, "B2": 0, "B3": 2, "B4": 3, "B5": 0, "B6": 2, "B7": 1, "B8": 1, "B9": 1,
      "C1": 2, "C2": 2}, -0.5, 5.8),
    ("snapchat-advertiser-2015 (sales)", "sales",
     {"A1": 1, "A2": 2, "A3": 2, "A4": 0, "A5": 1,
      "B1": 2, "B2": 1, "B3": 1, "B4": 1, "B5": 2, "B6": 1, "B7": 0, "B8": 2, "B9": 2,
      "C1": 3, "C2": 2}, -1.0, 5.7),
]


def selftest() -> int:
    all_ok = True
    for name, rubric, levels, defects, expected in CASES:
        r = score(levels, rubric=rubric, defects=defects)
        all_ok &= show(name, r, expected)

    # Airbnb stage-adjusted: A4 (financials) and B8 (ask) set N/A at pre-seed.
    airbnb = dict(CASES[0][2])
    airbnb["A4"] = "NA"
    airbnb["B8"] = "NA"
    show("airbnb-seed-2008 stage-adjusted (A4, B8 -> N/A)",
         score(airbnb, rubric="investor"), 7.8)

    print("=" * 60)
    print("ALL MATCH" if all_ok else "SOME MISMATCH — investigate")
    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(selftest())
