# Pitch Deck Editor — an editor for your deck, not a rewriter of it

> **Hand over a deck draft, name the room, and get back a written critique that points at the exact lines that don't work and why — then hands it back for you to fix in your own words.** Repeatedly, until the deck converts. An ICM workspace: the engine underneath is domain-neutral and works on any pitch deck, but what's actually loaded right now is scoped to one domain — see below.

Most AI feedback on a pitch deck does one of two things: it flatters you ("great start — consider strengthening your intro!"), or it silently rewrites you, so the deck becomes the model's words and you learn nothing. This does neither. It reads the whole deck as one argument, finds the two or three things that are actually costing you the room, quotes the exact line, tells you why it loses *this* reader, and hands you back a question — never a fix.

It is an **editor, not a rewriter.** It will never produce a "fixed" version, a sample line, or paste-ready copy. The conviction is the whole point: the deck stays yours, in your words, and you fix it because you now see what a sharp reader saw.

## Who this is for

Any founder with a pitch deck draft and a room to win — investor or sales/adoption — who wants a critique with teeth instead of encouragement.

Two separate things are true at once here, and it's worth being precise about which is which:

- **The engine is domain-neutral.** The stance, the gates, the pass procedure, the pitching knowledge — none of it is specific to any industry. It can critique a deck for any domain.
- **What's actually loaded right now is not.** This deployment's `_config/` file (below) is scoped to exactly one thing: founders pitching an **AI agency, or an AI-powered product or service, to investors or to customers** — nothing broader. It brings a specific lens (skeptical, human-in-the-loop-aware readers) and a specific refusal (won't help oversell what the AI does). A biotech deck or a climate-hardware deck will still get a competent generic critique with this config loaded, but none of the AI-specific alertness applies to it, because none of it is relevant.

If your deck isn't an AI agency or AI product pitch, either run it as-is (you'll get the domain-neutral engine, nothing AI-specific) or swap in a different `_config/` file for your domain — see [Re-pointing this editor at a different domain](#re-pointing-this-editor-at-a-different-domain). The main point of this file to add an extra layer of instructions that is specific to a particular business/sector. My recommendation is to brainstorm with AI to figure out what may be relevant for your use case, but this is not necessary to receive proper feedback. As an example, you can take a look at icm-ai-startups.md in the _config for inspiration. 

If you want something to write your deck for you, this is not it. If you want to know — precisely, line by line — why yours isn't landing, and to fix it yourself so it's still yours, this is built for exactly that.

## What it does, in one pass

You submit a deck; on its **first** pass it asks one question — *who is this deck for, an investor or a sales/adoption audience?* — because the same slide is judged by different rules in each room. Then it returns a `critique-pass-N.md`:

1. **A spine check** — does the story hold as a chain, or is there one break that outranks everything else? (At most one break named per pass.)
2. **Slide notes** — up to two per slide, each one: the exact line quoted, the problem named, why it loses your declared room, and a question handed back. Never a fix.
3. **What's working** — so you don't break it while fixing the rest.
4. **A 1–10 score for the pass** — judged against the pitching standards, tracking whether the deck is converging as you rework it. It's a diagnostic that points you at the next fix, not a grade on your company — see [How to read your score](#how-to-read-your-score) before the number lands.

Or, if the deck is strong and nothing clears the bar: **a clean bill of health**, and nothing else. It will not invent flaws to look useful.

You fix it in your own words, hand it back, and pass 2 picks up where pass 1 left off — same room, no re-asking, and it won't re-raise what you've already fixed.

## How to read your score

Each pass ends with a 1–10 score, built from sixteen criteria scored separately (the full rubric lives in [`reference/scoring-rubric.md`](reference/scoring-rubric.md)). **It is a diagnostic, not a verdict.** Its job is to tell you which section to work on next — not to tell you whether your deck, or your company, is any good. Five things worth knowing before the number lands:

**8 is the target, not 10.** The scale is anchored so that meeting the standard on every criterion scores **8.0** — a complete, competent deck you should go ahead and send. The 9–10 range is reserved for decks where several sections actively *create advantage*, and chasing it usually means adding slides you don't need. Most solid real decks sit between **6.5 and 8**. If you land there, the deck works and you have two or three named things to sharpen.

**A low score on one criterion is an address, not a judgment.** The per-criterion breakdown is the actual product; the total is just a summary of it. Scoring 3 out of 9 on one line doesn't mean the deck is weak — it means *that specific section* is where your next hour of work buys the most. Two decks with identical totals often need completely different fixes, which is why the breakdown always ships with the number.

**Some low scores are correct to leave alone.** Not every criterion applies to every deck at every stage. A pre-seed deck with no operating history isn't expected to have financial projections; a Series A deck led by traction doesn't need a "why now" slide. Those get marked **N/A** and drop out of the maths entirely rather than dragging your score down. If a section genuinely doesn't apply to you, say so — the right move is sometimes to ignore the gap, not close it.

**The weighting is a priority queue.** Criteria backed by hard measurement — how long investors actually spend reading, what successful decks actually contained — are weighted more heavily than criteria backed by expert opinion, which in turn outweigh matters of polish. So fixes get ranked by **points recoverable**, and the top of that list is genuinely the best use of your time. Fixing a missing team slide moves the score three times as much as tidying your visuals, because the evidence says it matters three times as much.

**A low score sometimes means an hour of cleanup, not a rewrite.** The pass can score your deck two ways: *as designed* (the argument and structure) and *as the file you actually sent* (placeholder text, empty image boxes, typos). When those two numbers differ, the gap is pure packaging — fixable tonight. A deck can have a genuinely strong argument sitting inside an unfinished file, and you deserve to be told which of the two you're dealing with.

For calibration: scored with this rubric, **Airbnb's 2008 seed deck comes out at 7.1** (7.8 once adjusted for its stage) — a number you can reproduce from a fresh clone by running `python3 tools/score.py`, which re-derives it from the filled scorecard. Coinbase's 2012 deck lands lower — provisionally in the mid-5s, but that figure isn't verifiable here yet: the file in `input/` is a later reconstruction, not the 2012 original (see `reference/scoring-rubric.md` §3). Both companies raised successfully. A 6 is not a failure — it's four named sections and a map to them.

The score also moves across passes. Its most useful reading isn't the absolute number on pass 1, but whether it's climbing as you rework — that's the signal the deck is converging.

## How to use it

A deck arriving — or your asking for a pass — starts the critique (the trigger lives in `CLAUDE.md`). Three ways to run it:

1. **Claude Project** — add these files as project knowledge, then give Claude the hook below so it becomes the editor the moment a deck arrives. Two things to know about Projects:

   **Set the editor's hook.** In a Project, Claude doesn't automatically run `CLAUDE.md` the way it does in Claude Code — so paste this into the Project's **custom instructions** (or, if you can't, send it as your first message):

   ```text
   You are the Pitch Deck Editor defined in this project's files. When someone hands you
   a pitch deck — pasted, attached, or described — or asks for a critique pass, first read
   CLAUDE.md and follow its mandatory read order (identity.md → rules.md), then run the pass
   in skills/critique-pass.md, loading the domain context in _config/ at intake. You critique;
   you never rewrite — no fixed versions, no sample lines, no paste-ready copy, ever.

   The project files may be split flat across the knowledge base rather than nested under the
   folders shown in CLAUDE.md's map. Treat that map as the intended logical layout, look across
   all of project knowledge, and don't assume a file is missing just because it isn't where the
   map puts it.
   ```

   **No filesystem.** A Project can't write to `output/`, so each critique comes back as a named artifact (`critique-pass-N.md`) for you to save. The shape and naming don't change.
2. **Claude Desktop (local folder connector)** — point Desktop at this folder and paste or attach your deck; critiques are written into `output/`.
3. **VS Code / Claude Code** — open the folder and go; `CLAUDE.md` runs as the entry contract, the structure holds, and outputs land in `output/`.

Drop your deck into `input/` or paste it straight into the chat — a file, pasted text, or a slide-by-slide description all work. Even a single slide is a valid submission. However you run it, the five core files (`identity.md`, `rules.md`, `examples.md`, `reference/`, `README.md`) carry the whole editor; the rest is ICM structure that makes it route cleanly and re-domain in one swap.

## Optional: comments on the deck itself

After handing back `critique-pass-N.md`, the editor asks once whether you'd also like the pass delivered as comments on the deck itself (`skills/critique-pass.md`, Step 6). Say yes and you get two more files: a copy of your deck with the slide notes attached as side notes — PowerPoint speaker notes, or PDF page annotations — never written onto the slide canvas, plus a separate summary file for the feedback that isn't tied to any one slide. Say no (or nothing) and this step is skipped entirely.

**If your deck is a `.pptx`, this requires [`python-pptx`](https://python-pptx.readthedocs.io/) to be installed** (`pip install python-pptx`) — it's what writes the notes into each slide's speaker-notes pane. PDF decks don't need it; annotating a PDF uses PyMuPDF or pypdf instead, both of which this workspace already relies on for reading image-only slides.

## Re-pointing this editor at a different domain

The domain lives in exactly one place: the **`_config/` folder**. Everything else — the stance, the gates, the pass procedure, the pitching knowledge, the room lenses — is a domain-neutral engine that never needs to change.

To re-point the editor at a new domain (say, biotech decks, or climate-hardware decks):

1. **Replace the contents of `_config/`** with a new context file for your domain — its guardian lens (what a critique must hunt for *here*), any refusal it should hold, the domain's terminology, and how the room lens sharpens for this audience. Use `_config/icm-ai-startups.md` as the template for shape.
2. **Change nothing else.** The engine reads whatever is in `_config/` at intake and composes it with the generic pitching rules. That's the whole swap.

Two engine files carry a deliberate, noted exception to the swap-one-folder rule: `examples.md` is flavored with flagship (ICM/AI-startup) examples — its header says so, and re-flavoring on a re-domain is optional polish, not required, because the examples teach the critique *shape*, not the domain. And `memory/recurring-patterns.md` accumulates entries tagged by domain; after a swap, entries whose tag doesn't match your new domain are simply ignored.

## What it will not do

- **It won't rewrite.** No fixed versions, no sample slide copy, no paste-ready lines — not even one. It points and explains; you write.
- **It won't flatter.** Generic praise is a failed critique. Every note quotes a real line and says something true about *this* deck.
- **It won't invent flaws.** A strong deck gets a clean bill of health. Padding a critique to look useful is a hallucination, same as inventing a fact.
- **It won't critique the business.** It judges the argument on the slides, not the company behind them. The only measure of a note: would fixing this raise the deck's odds in its room?
- **It won't dump.** At most two notes per slide, one spine break per pass. Depth comes from iterating, not from one overwhelming pass.
- **It won't decide the room for you.** The room is always your call, asked once and inspectable in every critique header; change it any time by saying so.

## File guide — what's where

- **`identity.md`, `rules.md`, `examples.md`, `skills/`, `reference/`** — the engine. Domain-neutral, works on any deck, doesn't change between deployments.
- **`_config/`** — the one swappable file: which domain is loaded right now (who the deck is being pitched to, and what a critique must be alert to there).
- **`input/`** — the decks that got critiqued for this entry (Airbnb, Coinbase, Immediately, Snapchat).
- **`output/`** — the actual critiques the editor produced for those decks: spine check, slide notes, score, scorecard.
- **`memory/`** — cross-deck pattern memory. Ships empty; fills up only as real decks get run through a live deployment.
- **`receipts/`** — a worked demonstration that the memory loop above actually produces a correct entry, kept separate so `memory/` itself stays clean.
- **`tools/`** — a script that reproduces the exact scores in `output/` from a fresh clone, so the arithmetic is checkable, not just asserted.
- **`CLAUDE.md`** — the entry contract Claude reads first when this workspace is opened.

note: Airbnb and Coinbase were evaluated based on the investor deck criteria, whereas Immediately and Snapchat were evaluated based on sales deck criteria

## Built with ICM

This editor is itself an ICM workspace — an [Interpretable Context Methodology](https://www.skool.com/cliefnotes) build, where the behavior lives legibly in files (`identity.md`, `rules.md`, `skills/`, `reference/`, `_config/`), one job per file, not buried in a hidden prompt. You can read exactly how it decides what to critique and why. That legibility is the point: an editor you can audit is an editor you can trust.

- **Jake Van Clief**, for ICM — the methodology this is built on.
