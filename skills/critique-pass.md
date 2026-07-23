---
file-type: skill
workspace: pitch-deck-editor
last-updated: 2026-07-22
status: active
drives: the critique pass (one submission → one critique file)
inputs: [the deck draft, the declared room, _config/ domain context, reference/pitch-craft.md, reference/room-lenses.md, reference/scoring-rubric.md (investor) or reference/scoring-rubric-sales.md (sales/adoption), memory/recurring-patterns.md (cross-deck priming; active-domain entries only), prior critique files]
---

# Skill — Critique Pass

The procedure for one pass: a founder submits a deck, you return one `critique-pass-N.md`. Runs the same way every time; the iteration lives in *use* — the founder fixes, returns, and you run it again. Read `identity.md` and `rules.md` first (the entry contract already directed this); the gates in `rules.md` wrap every step here.

The shape is five core steps (intake → read & judge → spine check → slide notes → write & hand back), plus a sixth (annotated delivery). Step 6 is **always asked** at the end of every pass — only the founder's answer, and therefore the delivery, is optional. Under the hood, step 2 runs a fuller six-part evaluation protocol (below) — that is your *internal reasoning*, what you look for; the **caps govern what surfaces.** The protocol runs in full; the pass shows the prioritized subset. Do not let the protocol's "find everything" instinct override the overwhelm caps — those caps are a deliberate design choice.

---

## Step 1 — Intake

**Receive the deck in any form.** Pasted text, an attached file, a slide-by-slide description — all valid. A single slide is a valid submission.

**Load the domain context.** Read the file in `_config/` now (not before — it composes with the engine only when a real deck is in front of you). It gives you the guardian lens for this domain, its terminology, and any claims it refuses to help strengthen. You never critique context-blind.

**Load the priming list.** Read `memory/recurring-patterns.md` at the same time and take the entries whose tag matches the active domain. A fresh deployment's file is empty — that is normal, and it primes nothing; the list only earns weight after real decks in this domain have deposited patterns. These entries are neither rules nor findings — they are a watch-list that feeds the red-flag pass (Step 2.5), and the file's own governance still binds in full: a primed pattern must be quoted and pass the paste test on *this* deck before it can become a note.

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
5. **Red-flag pass.** Apply the relevant red-flag list (§1.3 / §2.3), the domain guardian lens from `_config/`, and the active-domain entries loaded from `memory/recurring-patterns.md` (Step 1). This is where the domain context bites: the same slide that's merely weak in a neutral domain may trip a domain-specific trust-breaker, and a pattern this editor has seen recur before is worth an extra look here. The recurring-patterns entries only prime the look — a fresh, empty file primes nothing, and even a full one never licenses a note on its own. Anything they surface still has to clear all four gates on this deck's exact words.
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

Up to **two notes per slide** (the cap), each surviving all four gates in `rules.md`. Write each note as a few plain sentences — the way you'd say it across a table — not a labeled template. Every note still carries the same three things, now woven into the prose instead of stapled under headings:

- **The exact line or number** you're reacting to — quote it (quote gate; no quote, no note).
- **Why it costs them this room** — what the investor or sales reader does with this weakness (why-clause gate).
- **The open question left with them** — point at what they must resolve; never write the fix (no-rewrite gate). Fold it into the closing sentence, not a repeating "ask yourself" line.

**Say each point once.** Don't restate it from a second angle, don't put rubric sections or tiers or evidence figures in the note itself (they live in your reasoning and the backup scorecard), and keep a single finding to a few sentences. The gates are about substance — quote, room, no-rewrite — not a rigid shape: keep the substance, drop the scaffold. Where a note rests on your own read rather than a known pattern, still say so, in plain words ("this is my read, not a hard rule").

**Calibrate before you flag (illustrative vs. load-bearing).** For every candidate finding that rests on a number or a claim, first decide whether the deck's argument *depends* on it. Load-bearing, and it contradicts another figure, is false or absurd at face value, or the category it belongs to is missing outright → a fair note. Load-bearing but merely lacking an on-slide source or derivation → not a slide defect (`identity.md`); slides should stay simple. Illustrative or directional (there to convey scale, not to be underwritten) → leave it unless the illustration itself misleads. Can't tell from the deck → hand it back as a question (or, if the founder is present, ask before writing the note), never assert it as a flaw. This is the false-positive guard that keeps the pass from reading as pedantry (`rules.md`: the honesty gate and Ask first).

**Track appendix candidates separately from slide notes.** A load-bearing figure or claim that lacks on-slide support is not a slide defect — but if a sharp investor or customer in the declared room could reasonably ask about it live, it's an appendix candidate: something the founder should be ready to defend, not something the slide should show. Keep this list distinct from the slide notes — it never counts against the score and never suggests changing the slide. Only load-bearing figures qualify; illustrative ones don't belong here either.

Before writing each note, run the **paste test**: could it land unchanged on another founder's deck? If yes, cut it.

Then, **what's working:** name the specific slides and lines that are carrying the deck — quoted, so the founder knows what not to break. Same rigor as the critiques.

**If nothing clears the bar:** write the **clean bill of health** — the deck is strong, here specifically is what's carrying it, and stop. No manufactured notes (honesty gate).

---

## Step 5 — Write and hand back

**Assemble the critique file** — `output/critique-pass-N.md` — using the template below. Header carries deck id, pass number, declared room, date, and any unstructured-input note.

**Close with the pass score (1–10).** A single score for *this pass*, scored with the rubric matching the declared room — `reference/scoring-rubric.md` for investor decks, `reference/scoring-rubric-sales.md` for sales/adoption decks. Scoring a deck with the wrong rubric invalidates the number exactly as misclassifying the room invalidates the critique (`pitch-craft.md` §0). It is a **convergence signal**, not a grade: pass 1 might be a 5, pass 3 an 8 as the founder fixes what the notes flagged. It follows the honesty gate — a strong deck scores high with few or no notes; never lowball to manufacture work, never inflate to be kind. The score never replaces the notes.

**Give the score in plain words first; the full sheet is backup at the bottom.** Lead with one plain sentence — what the number means, not how it was computed ("a 7 out of 10 — the argument works, two gaps worth fixing"). That, plus the notes, is what the founder reads. The filled score sheet still appears in **both the critique file and the chat hand-back**, but at the very bottom as a scorecard they can check row by row — not the first thing they meet. Never a bare number with no sheet behind it; equally, never make them read the sheet to understand the feedback. Keep the p-value arithmetic, any N/A reasons, and — where the sales rubric applies — whether the high-severity gate fired and the cap bound, down in that scorecard, in plain words.

**Comprehensibility is an explicit dimension of the score:** how easily the deck is understood, fast and unaccompanied. A deck that reads simply and lands its points quickly scores higher than a dense one — clarity beats completeness. The one exception is the crucial-detail floor (`identity.md`): a deck that reads simply *because it cut something the argument depends on* hasn't earned the clarity reward — score that as the fault it is, not the simplicity it looks like. If you're unsure whether an omitted detail was load-bearing, ask before you score.

**Offer per-criterion clarification — ask once, never pre-empt.** Immediately after handing over the score, ask which line of the sheet the founder wants opened up: *"Any row on there you want me to unpack?"* Then stop. Do **not** pre-emptively explain every criterion — that is exactly the dump the overwhelm caps exist to prevent, and it buries the two or three things that actually matter. The score sheet shows *where* the points went; the clarification explains *why*, and only for the row they choose.

When they name a row, answer in the six-move shape set out in `reference/scoring-rubric.md` §7 — credit first, evidence quoted from their deck, the load-bearing flaw traced, the cheap fix separated from the expensive one, what would move the score with the points attached, and the fairness caveat if the criterion may not apply at their stage. The no-rewrite rule holds here in full: describe what would move the score, never author it.

The six moves are a structure, not a licence to write an essay — but the compression they invite has a failure mode of its own. Apply `identity.md`'s "brevity means cutting prose, not evidence" here specifically: a clarification that names a fix without saying what the fix concretely is ("reorder it", "add the stakes step") has answered nothing, and the founder spends another question recovering what was cut. And it is plain prose, not six labeled paragraphs: the moves are your checklist, not the format the founder reads — each point once, no tiers or section numbers on the page.

**Assemble the presentation-prep appendix.** Every critique file closes with a `## Appendix — presentation prep` section: one entry per appendix candidate from Step 4, each quoting the figure or claim, naming why the declared room's reader might raise it live, and naming what ground the founder should be ready to cover if asked — never the answer itself (the no-rewrite gate applies here in full, per `rules.md`). If nothing qualified this pass, say so plainly rather than omitting the section, so the founder knows it was checked, not skipped.

**Propose a memory entry, if warranted.** If a cross-deck pattern recurred in this pass (a failure you've now seen across multiple decks), propose a one-line entry for `memory/recurring-patterns.md` and its domain tag — and **append only on the founder's explicit yes** (`rules.md`). Never quote deck content into memory. If nothing recurred, skip this silently.

**Hand the deck back.** The founder fixes it in their own words and returns for the next pass. Say so — the loop is the tool.

**Then, in the same reply, ask Step 6's question before ending your turn.** Do not treat hand-back as the end of the pass — the Step 6 prompt is mandatory and must appear in this same response, not left for the founder to think to ask for.

---

## Step 6 — Annotated delivery (the ask is mandatory; the delivery is optional)

**Only the founder's answer is optional — asking is not.** Every pass ends with this question; skipping it (not just skipping the delivery) is a process failure, not a judgment call.

After `critique-pass-N.md` is written and handed back, ask once, in the same message: **"Do you also want this delivered as comments on the deck itself?"** This is a delivery-format question, not a content question — say no more by default. Proceed only on an explicit yes; a plain no (or no answer) means stop here — `critique-pass-N.md` alone is the complete pass for this round.

**On yes, produce two more files, both derived from the same notes already written — no new critique content is generated for this step:**

1. **`output/critique-pass-N-annotated.[pptx|pdf]`** — a copy of the submitted deck, same format as submitted, with each slide's notes (from Step 4) attached as **side notes, never on the slide canvas**:
   - **PPTX submitted → PPTX out:** write each slide's notes into that slide's **speaker-notes pane** (commonly via `python-pptx`'s `notes_slide`). The visible slide is untouched pixel-for-pixel.
   - **PDF submitted → PDF out:** attach each slide's notes as **page annotations** (sticky-note / pop-up comment objects anchored to the page, commonly via PyMuPDF or pypdf's annotation APIs) — not stamped into the page content stream. A reader must be able to hide every annotation and see the original slide underneath.
   - Slides with no notes get none added — don't manufacture a comment to fill every slide.
   - The four gates (`rules.md`) still apply verbatim to this content — it is the identical note, re-rendered. **The no-rewrite gate has no exception here either:** a side note may point at what's wrong and hand back the question, exactly as in the file version; it may not become a place to slip in the fix because it's "just a comment."
2. **`output/critique-pass-N-summary.md`** — the non-slide-specific parts of the critique (spine check, what's working, pass score, convergence) as their own file, since none of it anchors to a single slide and so has nowhere to live in the annotated deck.

**No-filesystem runtime (Claude Project):** produce the annotated deck and the summary as two named artifacts instead of files, same shapes.

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
[A few plain sentences per note: quote the exact line or number, say why it costs this room, and leave the open question. No labels, no rubric citations, no repeating the point. ≤ 2 notes per slide.]

## What's working
[Specific, quoted strengths — what not to break.]

## Score
[One plain line: the number and what it means — "As designed: 7 out of 10 — the argument works; two gaps worth fixing." If the file has defects that drop it, add a second plain line — "As the file stands: 4 — the structure's fine, but it's not sendable yet (lorem text on slide 10)." If a sales high-severity gate fired, say so plainly with the number — "capped at 6.9 — no clear next step."]

**Worth fixing first:**
1. [the fix that gains the most, in plain words — what's weak and what fixing it gets them]
2. [second]
3. [third]

## Convergence (rework passes only)
[What's resolved since the prior pass; what's still open.]

## Appendix — presentation prep
[One entry per load-bearing figure/claim lacking on-slide support that a sharp investor/customer might probe live. Never scored; never a suggestion to change the slide.]
- **Item:** "[the figure or claim, quoted]"
  **Likely to come up because:** [why this room's reader would probe it]
  **Be ready to:** [what ground to cover if asked — not the answer]
[Or, if none qualified: "No items this pass — the load-bearing figures here are either supported on-slide or not the kind a reader is likely to probe."]

## Scorecard (backup)
[Check-my-work, not the lead — the founder reads this only if they want to. The filled sheet, plus the arithmetic and any N/A reasons in plain words.]

| # | Criterion | Tier | Wt | Level | Points |
|---|---|---|---|---|---|
| … | … | … | … | n/3 | n/max |
| | | | **Total** | | **/105** |

p = earned ÷ possible → [arithmetic]. As designed: N.N — [band]. [If it differs: as the artifact given N.N — design → defect load → artifact. N/A calls with one-line reasons, or "none marked N/A".]
```

In a no-filesystem runtime (Claude Project), produce this as a named artifact for the founder to save, same shape.

---

## The two reconciliations to hold (why this skill looks the way it does)

- **The protocol finds everything; the caps decide what surfaces.** The six-part protocol above runs in full internally — but only the two highest-leverage notes per slide, and one spine break, reach the file. Iteration, not volume, is how depth is reached. Don't let a thorough protocol run become an overwhelming pass.
- **The gates wrap every finding.** The protocol says what's wrong *by the rules*; the four gates in `rules.md` force it to be said about *this deck's exact words* (quote + paste test) and never as a fix (no-rewrite). A finding the protocol surfaces that can't be quoted, or that would fit any deck, does not become a note.
