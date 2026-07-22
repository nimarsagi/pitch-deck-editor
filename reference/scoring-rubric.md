---
file-type: reference
workspace: pitch-deck-editor
last-updated: 2026-07-22
status: active
note: Scoring layer for pitch-craft.md. That file defines what good looks like and carries the evidence tiers; this file turns those tiers into a weighted 1–10 score. Do not score without reading pitch-craft.md §0 first — a misclassified deck invalidates the score.
---

# scoring-rubric.md — Weighted 1–10 Deck Score

**Purpose:** Convert the findings in `pitch-craft.md` into a defensible number. Criteria are grouped by the evidence tier that backs them, and weighted accordingly: **an improvement on a Tier A criterion earns more than the same improvement on Tier B, which earns more than Tier C.**

**Scope:** This rubric is for **investor decks**. Classify first (`pitch-craft.md` §0). Sales and adoption decks use the sibling criteria set in `scoring-rubric-sales.md` — do not score a sales deck with this one. That file inherits everything structural from here (levels, weights, conversion, the two lenses, reporting, the §7 clarification shape) and changes only the criteria.

---

## How to score

1. **Classify the deck** and note its stage (pre-seed / seed / Series A+).
2. **Pick the lens** — score *as designed* or *as the artifact given* (see §4). If you report both, score design first, then apply defect deductions.
3. **Rate each criterion 0–3** using the descriptors in §2.
4. **Multiply by the tier weight**, sum to get points earned.
5. **Mark criteria N/A where the stage genuinely excludes them** (§5). N/A criteria drop out of *both* earned and possible.
6. **Convert** using the anchored scale below.

### Converting raw points to the 1–10 score

The scale is anchored to what real decks actually do, not to a theoretical perfect deck. Let **p = points earned ÷ points possible**.

```
if p ≤ 0.667:   Score = 1.0 + 10.5 × p              (below the Target anchor)
if p >  0.667:  Score = 8.0 +  6.0 × (p − 0.667)    (above the Target anchor)
```

| Anchor | Raw | Score | Why it sits here |
|---|---|---|---|
| Every criterion Unacceptable | 0% | **1.0** | Floor |
| Every criterion Acceptable | 33% | **4.5** | Present everywhere, underpowered everywhere |
| **Every criterion Target** | **67%** | **8.0** | **A complete, competent, fundable deck** |
| Every criterion Exemplary | 100% | **10.0** | Ceiling — near-unreachable by design |

**Why 8.0 for straight Target:** "Target" means *does its job properly, no investor objection*. A deck that clears that bar on all sixteen criteria is a strong deck and should read as one. The 8–10 stretch is reserved for decks that go past competent into advantage-creating, and it is deliberately steeper — the last two points cost roughly twice the raw work of the points below them.

**Sixteen criteria is not an instruction to build a sixteen-heavy deck.** Target on every criterion is one clean slide each — a team slide, a market slide, a model slide, an ask — which lands around 16–19 slides, itself the exemplary band in A5. Eight of the sixteen (A1, A2, A5, B1, B2, B9, C1, C2) score simplicity and clarity directly; a dense, overstuffed deck loses on those before it gains anything from being thorough elsewhere. A low score means a section is *missing*, never license to cram detail onto the slide that's there — "complete" and "crowded" are different failures, and this rubric scores against both.

Below the Target anchor, **1 raw point = +0.10** on the score, exactly. Above it, 1 raw point ≈ +0.06.

### Levels

| Level | Name | Meaning |
|---|---|---|
| 0 | Unacceptable | Absent, or present in a form that actively hurts |
| 1 | Acceptable | Present but underpowered — a reader notices the weakness |
| 2 | Target | Does its job properly; no investor objection |
| 3 | Exemplary | Does its job and creates advantage |

### Tier weights

| Tier | Backing | Weight | One level of improvement is worth |
|---|---|---|---|
| **A** | Measured research (DocSend/Harvard n=200, DocSend annual) | **×3** | 3 raw pts = **+0.30** on the 10-scale |
| **B** | Expert consensus (Sequoia, YC, Kawasaki, First Round) | **×2** | 2 raw pts = **+0.20** |
| **C** | Practitioner folklore | **×1** | 1 raw pt = **+0.10** |

Worked example of the weighting: taking **Team** from Unacceptable to Target earns 6 raw points (**+0.60**). Taking **Why Now** the same distance earns 4 (**+0.40**). Taking **Visual craft** the same distance earns 2 (**+0.20**). Fix the Tier A gaps first — the rubric pays you more for them because the evidence says investors punish them more.

**Full-deck maximum:** 105 raw points (Tier A 45 · Tier B 54 · Tier C 6).

---

## 1. Score sheet

**Notation:** always write levels and points as fractions of their maximum — `2/3 → 6/9 pts`. Never write `2 → 6`: a bare "3 → 9" reads as the fraction 3/9 and inverts the meaning of a top score. Tier A criteria max at 9 points, Tier B at 6, Tier C at 3.

| # | Criterion | Tier | Wt | Level (of 3) | Points (of max) |
|---|---|---|---|---|---|
| A1 | Skim survivability | A | ×3 | | |
| A2 | Standalone comprehension | A | ×3 | | |
| A3 | Team | A | ×3 | | |
| A4 | Financials & numbers credibility | A | ×3 | | |
| A5 | Length & focus discipline | A | ×3 | | |
| B1 | Business clear by slide 3 | B | ×2 | | |
| B2 | Narrative sequence & title chain | B | ×2 | | |
| B3 | Problem & solution | B | ×2 | | |
| B4 | Why Now | B | ×2 | | |
| B5 | Market sizing | B | ×2 | | |
| B6 | Competition & moat | B | ×2 | | |
| B7 | Business model | B | ×2 | | |
| B8 | The Ask | B | ×2 | | |
| B9 | Headline craft | B | ×2 | | |
| C1 | Visual craft & legibility | C | ×1 | | |
| C2 | Language hygiene & specificity | C | ×1 | | |
| | | | **Total** | | **/105** |

---

## 2. Level descriptors

### Tier A — measured (×3)

**A1 · Skim survivability** — *the deck is read in ~224 seconds*
- **0** — Multiple slides require study. Dense paragraphs, crowded charts, the reader must stop and parse.
- **1** — Most slides land, but two or three need re-reading or carry competing ideas.
- **2** — Every slide lands in seconds; at most one slows the reader.
- **3** — Whole deck absorbable in under three minutes; each slide's point is unmissable at a glance.

**A2 · Standalone comprehension** — *~30% of decks are first read internally with no founder present*
- **0** — Several slides are meaningless without narration: untitled images, bare visuals, cryptic diagrams.
- **1** — Broadly followable, but a few slides need a presenter to carry their meaning.
- **2** — Every slide states its own point; forwarding it cold loses nothing important.
- **3** — Reads as a document as well as a deck; a stranger could accurately summarize the thesis.

**A3 · Team** — *appeared in 100% of successful seed decks; among the two longest-dwell slides*
- **0** — No team slide.
- **1** — Present but buried mid-deck, or names and titles only, with no link to this problem.
- **2** — Present, positioned at the start or end, credentials that connect to the problem.
- **3** — Well positioned and makes an explicit "why we win this" case — prior wins, domain scars, unfair access.

**A4 · Financials & numbers credibility** — *~57% of successful decks vs 0% of failed ones included financials*
*Scope: A4 judges the deck's own arithmetic — internal consistency, stated assumptions. It does not re-judge whether an underlying market or usage number is defensible; that's B5's. If a weak number elsewhere cascades into a financial figure, note the inheritance once rather than scoring it here too.*
- **0** — No financials and no revenue model; or figures that contradict each other or are visibly stale.
- **1** — A revenue model or scattered figures, but no projections and key numbers unjustified.
- **2** — Projections present with stated assumptions; numbers internally consistent.
- **3** — Every headline number has a stated basis, and nothing here contradicts a figure claimed elsewhere in the deck.

**A5 · Length & focus discipline** — *successful seed decks averaged 19.2 slides; engagement drops past ~20*
- **0** — Over 25 slides, or padded with detail that belongs in an appendix.
- **1** — 21–25 slides, or noticeable redundancy.
- **2** — 20 or fewer, main flow tight, detail pushed to an appendix.
- **3** — Roughly 10–19 slides where every one earns its place; nothing cuttable without loss.

### Tier B — expert consensus (×2)

**B1 · Business clear by slide 3**
- **0** — A cold reader cannot state what the company does after slide 3.
- **1** — Inferable by slide 3, but only by assembling scattered signals.
- **2** — Stated plainly by slide 3.
- **3** — Stated in one memorable declarative line on slide 1.

**B2 · Narrative sequence & title chain**
- **0** — Titles absent or decorative; order arbitrary; no build.
- **1** — Recognizable order, but titles are topic labels and some sections sit out of sequence.
- **2** — Reading the titles alone conveys the argument; each slide builds on the last.
- **3** — Titles alone form a complete, persuasive case, with momentum toward the ask.

**B3 · Problem & solution**
- **0** — Problem vague, generic, or absent; solution described as features.
- **1** — Problem stated but never made to feel costly; solution clear but generic.
- **2** — Specific problem tied to real behavior; solution maps directly onto it.
- **3** — Problem in the customer's own words, with evidence people already hack around it; solution is the obvious relief.

**B4 · Why Now** — *weighted heaviest at pre-seed/seed*
- **0** — Absent; nothing explains why this couldn't have been built five years ago.
- **1** — Implied by context but never stated.
- **2** — Explicit shift named — technological, regulatory, or behavioral.
- **3** — Shift named and evidenced, with a reason the window closes.

**B5 · Market sizing**
*Scope: B5 owns whether the market number itself is defensible — an asserted share or segmentation is judged here, not re-docked under A4 or B7.*
- **0** — No sizing, or one giant TAM with no segmentation.
- **1** — TAM/SAM/SOM present but purely top-down; market share asserted with no rationale at all.
- **2** — Top-down, with a named beachhead and a stated rationale for the share claimed — reasoned, even if not fully derived.
- **3** — Bottom-up from real usage or customer data, with a credible path from beachhead to the wider market.

**B6 · Competition & moat**
- **0** — Not addressed, or "we have no competition."
- **1** — Competitors listed without positioning, or advantages asserted without support.
- **2** — Honest landscape including the status quo, plus a stated advantage.
- **3** — Positioning that shows genuine whitespace, and an advantage that compounds over time.

**B7 · Business model**
*Scope: B7 owns unit economics — margin, CAC against LTV. Don't re-score the market-share assumption underneath the model; that's B5's.*
- **0** — How the company makes money is never stated.
- **1** — Model named without rates, or economics left unclear.
- **2** — Model, pricing, and the basic math shown.
- **3** — Model plus unit economics — margin per transaction, or CAC against LTV — showing it improves with scale.

**B8 · The Ask**
- **0** — No ask.
- **1** — Amount only, or a vague "raising a round."
- **2** — Amount plus what it buys.
- **3** — Amount, runway, and the specific milestones it unlocks, tied to the next raise. (Terms stay out of the deck.)

**B9 · Headline craft** — *assertion-evidence structure*
- **0** — No headlines, or headlines that mislabel their content.
- **1** — Topic labels: "Traction", "Market", "Product".
- **2** — Most headlines are claims the slide then evidences.
- **3** — Every headline is the takeaway; the body is one clean visual proving it.

### Tier C — folklore (×1)

**C1 · Visual craft & legibility**
- **0** — Illegible type, broken layout, low-resolution or clashing elements.
- **1** — Readable but dated or inconsistent.
- **2** — Clean, consistent, legible at a glance.
- **3** — Design actively aids comprehension; visual hierarchy does argumentative work.

**C2 · Language hygiene & specificity**
- **0** — Buzzword-dense; adjectives stand in for evidence throughout.
- **1** — Some vague claims — "revolutionize", "seamless" — diluting the real points.
- **2** — Concrete and specific; numbers carry names and timeframes.
- **3** — Every claim falsifiable; no unearned adjectives anywhere.

---

## 3. Score bands

**These bands describe the _as designed_ score only.** Do not look up an artifact score here — a deck can be structurally excellent and still un-sendable because of placeholder text. Artifact scores use the send-readiness bands in §4.

| Score | Band | Reading |
|---|---|---|
| **9.0–10** | Exceptional | Rare. The deck itself does the persuading; several sections create advantage |
| **8.0–8.9** | Strong | Complete and competent throughout. Send it |
| **6.5–7.9** | Good, with named gaps | The argument works; two or three sections are underpowered. **Most solid real decks live here** |
| **5.0–6.4** | Solid core, material gaps | Thinking is sound but canonical sections are missing outright |
| **3.5–4.9** | Structurally incomplete | Real rework needed before this goes out |
| **1.0–3.4** | Not ready | Missing the basics of the form |

### Benchmarks — where known decks land

Score against these, not against 10. Both companies below raised successfully at these scores.

| Deck | As designed | Note |
|---|---|---|
| Airbnb seed (2008) | **7.1** | Excellent structure; no team slide, no ask. Reproducible from a fresh clone: `python3 tools/score.py` |
| Coinbase seed (2012) | **5.5** *(provisional)* | Strong traction and polish; no market, model, competition, or ask |

*Coinbase's 5.5 is provisional and not yet reproducible here: the file in `input/` is a later Zlides reconstruction (post-2017 product slides), not the 2012 original, so it can't be re-scored to confirm the figure. Until the 2012 deck is scored with this rubric, treat 5.5 as a recorded estimate, not a checked benchmark.*

**How to read your score.** A **7** means the argument works and you have two or three named, fixable gaps — that is a normal, respectable place for a real deck to sit, and it is where the most-taught seed deck in the world sits. An **8** means complete and competent, which is the realistic target for a deck you are about to send. **9–10 is not the goal** — it is reserved for decks where multiple sections actively create advantage, and chasing it usually means adding slides you do not need.

The number is a diagnostic, not a verdict. Its job is to rank what to fix next, and the §6 "points recoverable" list is the part you act on. A deck's score and its odds of raising are related but not the same thing — investors fund the company, and the deck's job is to not get in the way.

---

## 4. The two lenses

Score under one lens and say which. Report both only when they diverge.

**As designed** — the underlying thinking: argument, structure, sequence, and content quality. Forgives defects a quick fix would remove. Use §1–§2 as written.

**As the artifact given** — the actual file, defects included. Score as designed, then subtract:

| Defect | Deduction | Cap |
|---|---|---|
| Placeholder / lorem text on a content slide | −1.5 each | −3.0 |
| Empty or missing image box | −0.25 each | −1.0 |
| Third-party template or ad slide left in | −0.5 | −0.5 |
| Typos, or numbers that disagree between slides | −0.5 each | −1.0 |
| Unreadable export — blurry, cropped, clipped text | −1.0 | −1.0 |

**Total deductions capped at −3.0. Floor the result at 1.0.**

### Send-readiness bands (for artifact scores)

Band the artifact by **how much was deducted**, not by where the resulting number lands. Defect load measures whether the file is finished; it says nothing about whether the argument is good, and the §3 bands must not be used for it.

| Total deduction | Band | Reading |
|---|---|---|
| 0 | **Send-ready** | No visible defects |
| −0.25 to −1.0 | **Minor defects** | Cosmetic; fix in under an hour |
| −1.25 to −2.0 | **Do not send yet** | Defects a recipient will notice immediately |
| −2.25 to −3.0 | **Unfinished** | This is a working draft, not a deck |

Always report artifact results as **design score → defect load → artifact score**, with the band drawn from this table. Reporting the artifact number alone invites exactly the wrong conclusion: that a well-built deck is badly built.

> **Worked example.** Airbnb: design **7.1** (*Good, with named gaps*) → defect load **−2.75** (*Unfinished*) → artifact **4.4**. The correct reading is "a well-structured deck sitting in an unfinished file," **not** "a structurally incomplete deck." Its structure is the best thing about it.

When the two scores diverge, the gap *is* the to-do list: it separates what is fixable tonight from what needs real rework. When they match, there is no cheap win — the problems are structural.

---

## 5. Stage calibration (the N/A valve)

Do not punish a deck for a section its stage genuinely excludes. Mark the criterion **N/A** and drop it from both earned and possible points — the denominator shrinks and the remaining criteria carry more weight.

Legitimate N/A cases:
- **Pre-seed:** A4 Financials (no operating history to project from) and B8 Ask (often verbal) may be N/A. A5 may be N/A for a deliberate 5-slide teaser.
- **Series A+:** B4 Why Now drops in weight — if the deck is traction-led, mark it N/A rather than penalizing its absence.
- **Deliberate simplicity:** a founder's own choice to cut a section to keep the deck lean is as legitimate as a stage exclusion — mark it N/A with a reason ("cut for focus, not because we lack one"), not a scored 0 or 1.
- **Never N/A for any reason:** A1, A2, A3, B1, B2. These are the load-bearing ones — no stage, and no simplicity choice, excuses them.

Record every N/A with a one-line reason next to the score. An unexplained N/A is score inflation.

---

## 6. Reporting format

Lead with plain language; the sheet is backup. Order:

1. **What kind of deck, and stage** — one plain line.
2. **The score in plain words** — the number and what it means, not the arithmetic ("a 7 — the argument works, two gaps worth fixing"). If the file has defects that drop it (placeholder text, a bad export), give that as a second plain line.
3. **The notes, and the fixes worth the most** — in plain sentences, ranked by how much they'd raise the score but stated as *what to fix and why*, not as point deltas.
4. **The filled score sheet** (§1) and the p-value arithmetic — at the very bottom, as the scorecard the founder can check row by row if they want. Never the lead; never make them read it to follow the feedback.
5. **Any N/A calls**, each with a one-line plain reason, kept with the scorecard.

Rank fixes by **points recoverable** — that ranking is the whole purpose of the weighting — but keep the numbers in the scorecard and the founder-facing text plain.

**Always close by offering clarification** — ask which row they want unpacked, then stop. Never pre-explain every criterion; that buries the two or three that matter.

Do not rewrite the deck. Describe fixes; do not author them, unless explicitly asked.

---

## 7. Answering "why did X score that?"

When the founder picks a row, the answer follows six moves in order. The point is that a low score should leave them knowing exactly what to do — and, sometimes, that the right move is to do nothing. Print the answer as plain prose: the six moves are your checklist, not six labeled paragraphs, and no tiers or section numbers reach the page. Say each point once.

1. **Credit first — say why the score isn't lower.** Open with what the deck genuinely earns on this criterion. A founder who hears only the deficit stops listening, and the contrast is what makes the level meaningful: *why a 1 and not a 0* is more informative than *why not a 3*.
2. **Number the problems, each anchored to their deck.** Quote the actual figure, line, or slide. No abstractions — "the market number is unsupported" teaches nothing; "the 10.6M on slide 5 is roughly 2% of your serviceable market and nothing explains why 2%" is actionable.
3. **Name the load-bearing flaw and trace what inherits it.** Most criteria fail because one unsupported thing sits underneath several others. Show the chain — it collapses a list of complaints into a single fix.
4. **Separate the cheap fix from the expensive one.** Flag anything fixable with material already in the deck. Founders consistently overestimate what a gap costs to close.
5. **State what would move it, with the points attached.** Give the next level and the top level as concrete targets: *to 2/3 (+3 pts, +0.30): …; to 3/3 (+6 pts, +0.60): …*. Never "be more rigorous."
6. **Give the fairness caveat.** If the criterion is a legitimate N/A at their stage, or the low score is defensible as-is, say so plainly — including when the honest advice is to leave it alone.

**Worked example — "What's wrong with Airbnb's money slide?"** (the six moves, printed as plain prose):

> First, the good part: it does say how the business makes money — a 10% cut of each booking. Plenty of decks never say that at all. That's why it's not the lowest score.
>
> The problem is that the whole $200M rests on one number — 10.6M trips — and that number is really a guess. Slide 5 gets there by assuming Airbnb captures about 2% of the market, and nothing shows why 2% rather than 1% or 5%. The $200M is just 10.6M × $20, so if the 2% is off, the $200M is off by the same amount. Two smaller things sit on top: it mashes four years into one figure with no year-by-year build, and there's no cost side, so it's a revenue guess, not a financial picture.
>
> The cheap fix and the expensive one are different. Showing it year by year, and being ready to say where the 2% comes from, needs no new data — it's just exposing reasoning you already have, and slide 4 already carries Craigslist and Couchsurfing numbers you could anchor it to. Tying the whole thing to real numbers from your first cities is the bigger, later job.
>
> One fairness note: this is a 2008 pre-seed deck with barely any history to forecast from. "We take 10%, here's the market math" is a defensible place to stop at that stage — which is why the stage-adjusted score is higher than the raw one. Judged as a finished deck it's weak here; judged as pre-seed, it's fine.

Notice what it never does: hand over a fixed slide, a sample projection, or a number to paste in — and it never once says "Tier A," "1/3," or a point total. Every fix is described so the founder writes it themselves; the scoring machinery stays in the scorecard.
