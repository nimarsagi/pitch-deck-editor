---
file-type: reference
workspace: pitch-deck-editor
last-updated: 2026-07-20
status: active
note: A thin lens summary. The evidence and detail live in reference/pitch-craft.md (§0, §1, §2); this file is the quick orientation, not a second copy. Domain-neutral by rule — see the seam note at the bottom.
---

# Room Lenses — who is reading, and what they weigh

The founder declares the room at intake (`rules.md`). The room decides which rules apply: **applying investor-deck criteria to a sales deck, or vice versa, invalidates the whole critique** (`pitch-craft.md` §0). This file is the fast orientation to the two lenses. For the evidence behind each weighting, the failure signatures, and the structural sequences, read `pitch-craft.md` — this only tells you where to point.

## The investor lens

The reader is deciding whether to *bet* on a future. They weigh — hardest first, by measured dwell time (`pitch-craft.md` §1.1):

- **Financials and team** get the most scrutiny; weak versions do disproportionate damage. A team slide that lists credentials without founder-market fit, or a missing/mid-deck team slide, is high-severity.
- **"What do you do by slide 3."** If a cold reader can't state the business by slide 3, that outranks almost everything.
- **The deck is an argument, not a brochure** — the title-chain should tell the whole story on its own.
- **Why-now, market built bottom-up, a real competitive map, a specific ask** tied to a milestone.
- Calibrate to **stage**: why-now matters most at pre-seed/seed; by Series A the deck should be traction- and unit-economics-heavy.

Telltale slides: TAM/SAM/SOM, team, financials, the ask. → Detail: `pitch-craft.md` §1.

## The sales / adoption lens

The reader is deciding whether to *change what they do*. The hero is the prospect, not the market. They weigh (`pitch-craft.md` §2):

- **Where the product first appears.** Product/feature/company-first openings are the measured low-completion shape; the customer's world comes first, product comes late, as the bridge.
- **Is there a cost-of-inaction moment.** A pain named but never made expensive has no urgency engine.
- **Is the shift bigger than the vendor** — a world-level change, not "stop using our competitor, use us."
- **Whose language the pain is in** — the prospect's own words beat generic "companies struggle with…".
- **Proof specificity** — a named customer + measured outcome + timeframe beats a logo wall.
- **The last slide is one concrete next step**, not "Questions?".
- Calibrate to **deal size**: full narrative arc for complex/enterprise; a tight PAS for transactional.

Telltale slides: cost of inaction, case studies with ROI, a clear CTA/next step. → Detail: `pitch-craft.md` §2.

## Both rooms share (the universal lens)

The deck is read **fast and alone** — every slide must stand without narration, every point land in seconds. **Narrative order is the highest-leverage variable** — critique sequence before content, content before design. Headlines carry the deck. One idea per slide. Specificity beats claims. (`pitch-craft.md` §3.)

---

## Seam rule — this file stays domain-neutral (audit-enforced)

These two lenses describe *rooms* (who's reading), not *domains* (what field the pitch is in). Anything domain-specific — a particular audience's skepticism, the trust-breakers of a given field, a skeptic-conversion framing — belongs in the `_config/` context file, which **composes with** the sales/adoption lens at runtime, not here.

**The test:** this file must read cleanly for a pitch in *any* field — biotech, climate hardware, consumer apps — with no field baked in. If a line here only makes sense for one domain, it has leaked across the seam and belongs in `_config/`.
