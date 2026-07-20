# Pitch Deck Editor — an editor for your deck, not a rewriter of it

> **Hand over a deck draft, name the room, and get back a written critique that points at the exact lines that don't work and why — then hands it back for you to fix in your own words.** Repeatedly, until the deck converts. An ICM workspace: a domain-neutral engine you point at any pitch context by swapping one config file.

Most AI feedback on a pitch deck does one of two useless things: it flatters you ("great start — consider strengthening your intro!"), or it silently rewrites you, so the deck becomes the model's words and you learn nothing. This does neither. It reads the whole deck as one argument, finds the two or three things that are actually costing you the room, quotes the exact line, tells you why it loses *this* reader, and hands you back a question — never a fix.

It is an **editor, not a rewriter.** It will never produce a "fixed" version, a sample line, or paste-ready copy. The conviction is the whole point: the deck stays yours, in your words, and you fix it because you now see what a sharp reader saw.

## Who this is for

Any founder with a pitch deck draft and a room to win — investor or sales/adoption — who wants a critique with teeth instead of encouragement. It ships pointed at **ICM / AI-startup decks** (the flagship context below), where the room is uniquely hostile and the failure modes are specific. But the engine is domain-neutral: point it at any pitch context by swapping one file.

If you want something to write your deck for you, this is not it. If you want to know — precisely, line by line — why yours isn't landing, and to fix it yourself so it's still yours, this is built for exactly that.

## What it does, in one pass

You submit a deck; on its **first** pass it asks one question — *who is this deck for, an investor or a sales/adoption audience?* — because the same slide is judged by different rules in each room. Then it returns a `critique-pass-N.md`:

1. **A spine check** — does the story hold as a chain, or is there one break that outranks everything else? (At most one break named per pass.)
2. **Slide notes** — up to two per slide, each one: the exact line quoted, the problem named, why it loses your declared room, and a question handed back. Never a fix.
3. **What's working** — so you don't break it while fixing the rest.
4. **A 1–10 score for the pass** — judged against the pitching standards, tracking whether the deck is converging as you rework it.

Or, if the deck is strong and nothing clears the bar: **a clean bill of health**, and nothing else. It will not invent flaws to look useful.

You fix it in your own words, hand it back, and pass 2 picks up where pass 1 left off — same room, no re-asking, and it won't re-raise what you've already fixed.

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

## Built with ICM

This editor is itself an ICM workspace — an [Interpretable Context Methodology](https://www.skool.com/cliefnotes) build, where the behavior lives legibly in files (`identity.md`, `rules.md`, `skills/`, `reference/`, `_config/`), one job per file, not buried in a hidden prompt. You can read exactly how it decides what to critique and why. That legibility is the point: an editor you can audit is an editor you can trust.

- **Jake Van Clief**, for ICM — the methodology this is built on.
