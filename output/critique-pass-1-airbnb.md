---
file-type: critique-pass
deck: airbnb-seed-2008
pass: 1
room: investor
stage: pre-seed (2008)
date: 2026-07-22
input-note: The file critiqued is PitchDeckCoach's reproduction of Airbnb's deck, not the original — slide 10's body is lorem-ipsum placeholder, slide 8 has three empty image boxes, and slide 11 is a template ad. The argument is critiqued as reproduced; the file defects are counted separately in the score.
---

# Critique — airbnb-seed-2008, Pass 1 (investor)

## Spine check
The deck builds a full case and then doesn't close it. Nine slides do the work — a real problem, a matching solution, proof people already do this by hand, a market, a product, a revenue number, growth, competition. Then it stops. There's no team slide and no ask. An investor who's just seen a $200M number turns the page looking for who's going to build this and what you're raising, and lands on a list of advantages instead. These are missing pieces, not weak ones — adding them changes nothing else in the deck.

## Slide notes

### Slide 2 — Problem
"Price is an important concern for customers booking travel online." This is the weakest of your three problems, and it's given the same weight as the other two. Every investor already believes travel is price-sensitive, so it spends your most-read slide on the one line they can predict. The other two — hotels cut you off from the neighborhood, and there's no easy way to book with a local or become a host — are the ones only you are saying. Which of the three could a hotel-comparison site not have written, and should that be the one they read first?

### Slide 5 — Market Size
"10.6M — trips with AB&B." The funnel looks derived — 1.9B trips, down to 532M budget-and-online, down to 10.6M — but the last step is really a guess: it assumes you capture about 2% of the market, and nothing reasons toward 2% over 1% or 10%. The next slide's whole $200M rests on this number, so it's the one an investor leans on hardest. What's the case for 2%, and could you reach a similar number from the bottom up, starting from the 17,000 Craigslist listings you already counted on slide 4?

### Slide 7 — Business Model
"10.6M × $20 = $200M revenue, 2008–2011." This is one multiplication carrying the weight of a projection. It takes slide 5's 10.6M as given, so if that's high, the $200M is high by the same amount. Two more things weaken it: it folds four years into a single figure with no year-by-year build, and there's no cost side, so it's a revenue guess rather than a financial picture. What does this look like year by year, and which number in the chain would you least want an investor to push on?

### Slide 10 — Competitive Advantages
"1st to market." You listed this first of six advantages, and it's the one that protects you least — being first fades the moment a funded competitor shows up. The genuinely durable ones are right there on the same slide, ranked below it: "host incentive" and "profiles" are network effects that get stronger as you grow. An investor reads the top-left item as your own ranking of what protects the business, and sees the weakest moat leading. Of these six, which gets harder for a competitor to beat as you scale — and why isn't that one first?

## What's working
- Slide 1 says the business in one line: "Book rooms with locals, rather than hotels." A cold reader knows exactly what you do before slide 2.
- Slide 4 is the best move in the deck: "630,000 on couchsurfing.com" and "17,000 temporary housing listings on SF & NYC Craigslist, 07/09–07/16." Two checkable numbers with a date, proving people already do this by hand — demand you don't have to assert.
- The solution answers the problem one-for-one: SAVE MONEY / MAKE MONEY / SHARE CULTURE line up with the three problems in order.
- Slide 9's competition map plots real named rivals — hotels.com, Craigslist, CouchSurfing, VRBO — and shows genuine open space rather than claiming it.

## Score
As designed: a 7 out of 10 — the argument works, with two clear gaps (no team, no ask). As the file stands: a 4 — the structure is strong, but this exact file isn't sendable: slide 10 is placeholder lorem-ipsum text, slide 8 has three empty image boxes, and slide 11 is a template ad. That's a finishing problem, not a thinking problem.

**Worth fixing first:**
1. Add a team slide. The single biggest gap — investors expect one, and there isn't one here.
2. Shore up the market number. The 2% share is the load-bearing guess; give it a reason, or build it bottom-up from your slide-4 data.
3. Add an ask — how much you're raising and what it buys. Cheapest of the three to fix.

## Appendix — presentation prep
Things a sharp investor is likely to probe live — worth having an answer ready for, not worth cluttering the slide with:
- **The 2% market share on slide 5.** Everything downstream rests on it. Be ready to say where it comes from and what happens to the $200M if it's half that.
- **The $20 average fee on slide 7** (a $70/night, three-night stay at about 10%). Be ready to defend those inputs if asked.

## Scorecard (backup)
Check-my-work — read this only if you want to see where the number comes from.

| # | Criterion | Level | Points |
|---|---|---|---|
| A1 | Skim survivability | 2/3 | 6/9 |
| A2 | Standalone comprehension | 3/3 | 9/9 |
| A3 | Team | 0/3 | 0/9 |
| A4 | Financials & numbers credibility | 1/3 | 3/9 |
| A5 | Length & focus discipline | 3/3 | 9/9 |
| B1 | Business clear by slide 3 | 3/3 | 6/6 |
| B2 | Narrative sequence & title chain | 2/3 | 4/6 |
| B3 | Problem & solution | 3/3 | 6/6 |
| B4 | Why Now | 1/3 | 2/6 |
| B5 | Market sizing | 1/3 | 2/6 |
| B6 | Competition & moat | 2/3 | 4/6 |
| B7 | Business model | 2/3 | 4/6 |
| B8 | The Ask | 0/3 | 0/6 |
| B9 | Headline craft | 1/3 | 2/6 |
| C1 | Visual craft & legibility | 2/3 | 2/3 |
| C2 | Language hygiene & specificity | 2/3 | 2/3 |
| | **Total** | | **61/105** |

61 ÷ 105 = 0.581 → as designed **7.1**.
Stage-adjusted: setting financials and the ask aside as fair to skip at 2008 pre-seed gives 58 ÷ 90 = 0.644 → **7.8**. Team still counts — it's never waived.
As the file stands: 7.1 − 2.75 for defects (lorem −1.5, empty boxes −0.75, template/ad −0.5) = **4.4**.
Benchmark check: this pass's 7.1 design / 4.4 file is the number `tools/score.py` reproduces from this exact scorecard, and matches what `reference/scoring-rubric.md` §3 now records. (Reproducibility, not a blind test — the rubric was visible while scoring.)
