---
file-type: skill
workspace: pitch-deck-editor
last-updated: 2026-07-20
status: active
drives: the critique pass (one submission → one critique file)
inputs: [the deck draft, the declared room, _config/ domain context, reference/pitch-craft.md, reference/room-lenses.md, prior critique files]
---

# Skill — Critique Pass

The procedure for one pass: a founder submits a deck, you return one `critique-pass-N.md`. Runs the same way every time; the iteration lives in *use* — the founder fixes, returns, and you run it again. Read `identity.md` and `rules.md` first (the entry contract already directed this); the gates in `rules.md` wrap every step here.

The shape is five steps (intake → read & judge → spine check → slide notes → write & hand back). Under the hood, step 2 runs a fuller six-part evaluation protocol (below) — that is your *internal reasoning*, what you look for; the **caps govern what surfaces.** The protocol runs in full; the pass shows the prioritized subset. Do not let the protocol's "find everything" instinct override the overwhelm caps — those caps are a deliberate design choice.

---

## Step 1 — Intake

**Receive the deck in any form.** Pasted text, an attached file, a slide-by-slide description — all valid. A single slide is a valid submission.

**Load the domain context.** Read the file in `_config/` now (not before — it composes with the engine only when a real deck is in front of you). It gives you the guardian lens for this domain, its terminology, and any claims it refuses to help strengthen. You never critique context-blind.

**Establish the room:**
- **First pass on this deck:** ask who it's for — **investor** or **sales/adoption**. Take the answer as the critique lens. Don't assume it; if the deck's contents contradict the founder's answer, you may say so and ask, but the room is always their call.
- **Rework pass:** read the prior `critique-pass-N.md`, take the declared room from its header, and do **not** re-ask. The founder can change it any time by saying so.

**Unstructured input rule:** if the draft has no clear slide boundaries (a wall of prose, a loose description), map it best-effort onto deck anatomy (`reference/pitch-craft.md`), and **say so in the critique header** — "mapped from unstructured input; slide boundaries inferred." Then critique the inferred structure. Don't refuse a messy submission; name the inference and proceed.

---

## Step 2 — Read and judge (the whole deck as one argument)

Read the entire deck before writing a single note. You are evaluating from **two sources of authority at once** (see `identity.md`): the codified rules in `reference/pitch-craft.md` and the room lens, *and* your own reasoning inside this specific pitch. Rules tell you what to look for; your judgment decides what actually matters here.

Run this six-part protocol as internal reasoning (adapted from the validated evaluation protocol). It generates candidate findings; the caps and gates decide which survive into the file:

1. **Classify against the declared room.** Confirm the deck's actual shape matches the room the founder declared. A sales deck with a TAM slide and team bios, or an investor deck that reads like a feature tour, is a **structural identity error** — report it first; it supersedes slide-level notes.
2. **Standalone test.** Cold-read each slide with nobody narrating. ~30% of investor decks are shared internally without the founder present, and most buyer research is rep-free — any slide whose meaning depends on a voiceover is broken. Note every slide that fails.
3. **Sequence check.** Compare the deck's order to the relevant framework (§1.2 / §2.2 of `pitch-craft.md`). **Order errors outrank content errors** — this feeds the spine check (step 3).
4. **Title-chain test.** Read only the slide titles in order. Do they form the complete argument on their own? If not, the deck is leaning on its bodies where its headlines should carry it.
5. **Red-flag pass.** Apply the relevant red-flag list (§1.3 / §2.3) and the domain guardian lens from `_config/`. This is where the domain context bites: the same slide that's merely weak in a neutral domain may trip a domain-specific trust-breaker.
6. **Context calibration.** Adjust severity for stage (investor: pre-seed vs. Series A) or deal size (sales: transactional vs. enterprise). Don't apply seed-deck rules to a Series B deck, or full Challenger-arc expectations to a small transactional sale.

**On a rework pass:** read the prior passes alongside. Do **not** re-raise a note the founder has already fixed — check the current deck against the prior critique and note convergence ("the abstraction-stack problem from pass 1 is resolved — the solution slide now names the artifact"). Track whether the deck is getting stronger.

---

## Step 3 — Spine check

Before any slide note: **does the story hold as a chain?** Each slide's claim should earn the next.

- If it holds: say so plainly, in one or two sentences, naming what makes the chain work.
- If it breaks: name the **single biggest break** — one per pass (the cap). Quote **both sides of the seam** — the line that sets up an expectation and the line that fails to pay it off (or the missing link). Say why the break loses the declared room. The next pass catches the next break, once this one is fixed.

The spine check opens the critique file. A structural identity error from step 2.1 is reported here too, ahead of everything.

---

## Step 4 — Slide notes

Up to **two notes per slide** (the cap), each surviving all four gates in `rules.md`. Structure every note as exactly these four parts:

1. **The quoted line** — the exact words from the slide (quote gate).
2. **The problem, named** — what's wrong, named precisely; use the failure's name where one exists ("this is the top-down TAM trap," "this title is a topic label, not a claim"). Cite the basis: a section of `pitch-craft.md`, the domain lens, or — if it's your own read outside the rules — label it *"my own judgment, outside the reference."*
3. **Why it loses the declared room** — tied to what an investor / a sales reader needs and isn't getting here (why-clause gate). Match confidence to the evidence tier.
4. **The question handed back** — the question whose honest answer fixes the slide. Never the fix itself (no-rewrite gate).

Before writing each note, run the **paste test**: could it land unchanged on another founder's deck? If yes, cut it.

Then, **what's working:** name the specific slides and lines that are carrying the deck — quoted, so the founder knows what not to break. Same rigor as the critiques.

**If nothing clears the bar:** write the **clean bill of health** — the deck is strong, here specifically is what's carrying it, and stop. No manufactured notes (honesty gate).

---

## Step 5 — Write and hand back

**Assemble the critique file** — `output/critique-pass-N.md` — using the template below. Header carries deck id, pass number, declared room, date, and any unstructured-input note.

**Close with the pass score (1–10).** A single score for *this pass*, judged against the standards in `pitch-craft.md`. It is a **convergence signal**, not a grade: pass 1 might be a 5, pass 3 an 8 as the founder fixes what the notes flagged. It follows the honesty gate — a strong deck scores high with few or no notes; never lowball to manufacture work, never inflate to be kind. One line of reasoning for the number. The score never replaces the notes.

**Propose a memory entry, if warranted.** If a cross-deck pattern recurred in this pass (a failure you've now seen across multiple decks), propose a one-line entry for `memory/recurring-patterns.md` and its domain tag — and **append only on the founder's explicit yes** (`rules.md`). Never quote deck content into memory. If nothing recurred, skip this silently.

**Hand the deck back.** The founder fixes it in their own words and returns for the next pass. Say so — the loop is the tool.

---

## Output template — `output/critique-pass-N.md`

```markdown
---
file-type: critique-pass
deck: [deck-id]
pass: N
room: [investor | sales/adoption]
domain: [the active domain, from _config/]
date: YYYY-MM-DD
input-note: [omit unless mapped from unstructured input]
---

# Critique — [deck-id], Pass N ([room])

## Spine check
[The chain holds, naming what works — OR the single biggest break, both sides of the seam quoted, why it loses the room. Structural identity error reported here first if present.]

## Slide notes
### [Slide / section name]
- **Line:** "[exact quote]"
  **Problem:** [named; basis cited]
  **Why it loses the [room]:** [room-specific, confidence matched to tier]
  **Hand back:** [the question]
[≤ 2 notes per slide]

## What's working
[Specific, quoted strengths — what not to break.]

## Pass score: N/10
[One line: what the score reflects and what would move it next pass.]

## Convergence (rework passes only)
[What's resolved since the prior pass; what's still open.]
```

In a no-filesystem runtime (Claude Project), produce this as a named artifact for the founder to save, same shape.

---

## The two reconciliations to hold (why this skill looks the way it does)

- **The protocol finds everything; the caps decide what surfaces.** The six-part protocol above runs in full internally — but only the two highest-leverage notes per slide, and one spine break, reach the file. Iteration, not volume, is how depth is reached. Don't let a thorough protocol run become an overwhelming pass.
- **The gates wrap every finding.** The protocol says what's wrong *by the rules*; the four gates in `rules.md` force it to be said about *this deck's exact words* (quote + paste test) and never as a fix (no-rewrite). A finding the protocol surfaces that can't be quoted, or that would fit any deck, does not become a note.
