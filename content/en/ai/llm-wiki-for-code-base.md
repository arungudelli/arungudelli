---
title: "Your LLM Keeps Re-reading the Same Code. Give It a Wiki."
slug: "llm-wiki-for-code-base"
description: "Documentation is software's oldest chore, and LLMs are finally good at it, because they don't mind boring work. Inspired by Karpathy's LLM Wiki, here's the page wiki: one distilled, source-anchored markdown file per page that humans can read to understand the codebase and LLMs reuse to skip re-reading it. A shared, durable knowledge base that cuts input tokens and stays honest via a git-hash freshness anchor. With a runnable demo that measures the saving."
date: "2026-09-19T00:29:00+05:30"
lastmod: "2026-09-19T00:29:00+05:30"
draft: "false"
type: "docs"
mermaid: false
images: ["images/page-wiki-durable-codebase-knowledge.png"]
---

I did not publish anything from last one year.

Reason is LLM only. Because when AI can explain everything very fast, writing step-by-step tutorial is waste of time.

But this one is different. It is not a tutorial.

It is about making AI remember our project code. So next time it will not start from zero.

It starts with very boring problem in software.

In every team I worked, everyone has same tension: documentation is not updated.

Reason is simple. Updating docs is very boring work.

We engineers are lazy to write docs. And we are also very bad at it.

You will write one time, then code will change. 

After six months, doc is totally wrong. 

But new joiner will trust it because he don't know anything.

Nobody ever bothered to fix this. We just ignore it and continue our work.

Main project knowledge (like payment flow logic, or why one function is there) is only inside senior engineer head or some old Slack message which difficult to find.

But think about LLMs they won't get bored. They can check fifteen files and update the details, and again do same thing tomorrow without complaining.

The boring work which developers like us hate, LLMs will do happily daily. 

This will completely change how we do documentation.

I understood this properly after reading one gist on GitHub.

It is written by **Andrej Karpathy**. 

He calls it the <a href="https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f" target="_blank">**LLM Wiki**</a>.

His point is simple. Right now *"the LLM is rediscovering knowledge from scratch on every question. There's no accumulation."* 

Every answer is lost. Next time it starts from zero again.

His fix is not a better search. 

It is a wiki which the LLM builds one time and keeps updated. 

One file which keeps growing.

He even connects it to Vannevar Bush's 1945 **Memex**. That idea failed first time because *humans* could not do the maintenance. 

Now the LLM will do that part.

He says the full division of work in one line: *"You're in charge of sourcing, exploration, and asking the right questions. The LLM does all the grunt work, the summarizing, cross-referencing, filing, and bookkeeping."*

Next question is, what should these docs look like?

Nothing fancy. Any format will work.

I am using plain markdown files. Small YAML frontmatter on top. And links between pages.

That is it.

One markdown file renders as a **Hugo website which a human can read**. 

The *same file* is plain text which an **LLM can read**. One file.

No special tool needed here. If you already have some format you like, just use it.

Human gets a map of the codebase which is correct. LLM gets the context ready, so it will not grep the whole repo again.

I built a small demo where every page in the codebase gets its own documentation file. 

I call it a page wiki: **page-wiki.md**. 

Here **page** means one bounded area of a codebase, not only a browser page. A page wiki can be:

- A UI route
- An API endpoint
- A background job
- A service
- A data pipeline
- Any related group of files which you understand and change together

---

## How does LLM read our codebase??

You ask the LLM to change one page. 

It opens five files. Reads everything. 

Then it understands how they are connected. 

After that only it starts the work.

Tomorrow you ask one more change in the same page. 

It opens the same five files. 

Reads everything again. From zero.

Every time it is learning the same thing again.

For a small script, no issue.

But in a project where you are working for months, you are paying for this again and again. 

**More tokens**, more waiting, and your context window is full before the real work starts.

---

## What is missing? An index.

Think about a dictionary.

While searching a word in dictionary, we won't read a dictionary from first page to last page. 

The dictionary sorted alphabetically. 

We jump directly the first letter of the word, then the move few pages, and reach the word in seconds.

That alphabetical order *is* an index. 

It is the only reason a book with 100,000 words is still usable.

Now imagine the same dictionary in random order. 

Same words, same meanings. No alphabetical order.

To find one word you have no option. 

Start from page, Read page after page. Until you find that word.

Same book. But without the index it is almost useless. 

We were stuck doing a slow, one-by-one search.

**Finding code in a new repo is exactly this random-order dictionary.**

A codebase is a book with thousands of "words" (functions, components, endpoints) spread across hundreds of "pages," the files. 

When an LLM tries to change the code, it does not have any knowledge about the code base, just like the  dictionary without index.

So it will do scanning of our code base file by file, based on the words from our prompt (grep search). 

Opens whatever files match. 

Reads them to check if they are correct. 

If not, greps again and opens more.

Every miss is one more page turned. 

One more file read. One more turn. 

**One more few thousand tokens.**

And if the code you want to change is not using the same words you typed, the search will simply miss it.

Maybe the file is using some other name. 

Maybe the call is happening indirectly, at runtime.

Now the model is lost. It starts guessing.

This is exactly how a human mind also works.

Put a fresh engineer into a large codebase. 

Tell them to change the **book-list search**. 

They also can't jump straight to the correct file.

They open files. Read. Follow imports. Guess. Check. Go back. The human version of grep.

It is slow. And it is slow for the same reason. No index yet.

Now take one senior engineer working in that same codebase from two years.

Same task. He will not search at all.


He already knows it. *"That is the `BookListComponent`. Search is a computed signal on the in-memory list. And one thing, filtering is happening only on client-side."*

He opens the file directly. And he already knows where to change the code.

He is not more intelligent than the fresher. 

He is just having the index ready in his head.

With an LLM, every session it is the fresher. 

It has no memory of your codebase.

However smart it is at reasoning, it wakes up every time having never seen your repo. 

And builds the map from zero. 

Same as you, if your memory reset every morning.

A page wiki is that senior engineer's mental index. Written down and kept fresh.

So a new teammate, or the model, who never saw this code will also get the same shortcut or index on day one.

Now no searching. The LLM opens one page. 

That page tells which files to touch and what to be careful about.


---

## So what is the actual idea?

The pattern is one sentence:

> Understand a page **once**, write down the distilled, reusable truth as a `page-wiki.md`, anchor that file to the source by git blob hash, then reuse the page instead of re-reading the source every time. When the source changes, the anchor goes *stale*, and only *then* do you re-read.

That is it. Two things make it work. These are the parts people usually skip:

1. Each page is a **distilled** summary which a human (or a model) wrote on purpose. Not a raw dump of the files.
2. Each page is **anchored to the exact source it describes**. So it can tell you when it is out of date, instead of misleading you silently.

A wiki which cannot tell you it is stale is a liability, not an asset.

The git-hash anchor is the thing which turns "notes I wrote one time" into durable knowledge. Something you can trust session after session, and give to someone else.

---

## What are the three layers?

In simple words, the pattern has three layers:

```text
app source        (many files — the ground truth)
   ↑ re-read ONLY when the page is STALE
page-wiki.md      (one distilled file per page, anchored to source by git hash)   ← reused every time
   ↑ resolved via
wiki-index        (which page is this request even about?)
```

- **Source** is the truth. It is big. It is spread across many files. Reading all of it is what costs you.
- **`page-wiki.md`** is one small file per bounded area. It has the overview, the component or request-flow map, the data flow, the key files, and most importantly the *gotchas* which a model would otherwise work out again. Each page stores the git blob hash of every source file it summarizes.
- **`wiki-index`** answers a different question. For a fuzzy request like *"fix the book list search"*, which page do I load? It is a light resolver. So you don't need to know the file layout to find the correct page.

---

## Why anchor to the git blob hash?

This is my one real addition to Karpathy's pattern. It exists because a codebase behaves differently from a pile of documents.

In the original LLM Wiki, freshness is mostly a human-driven event. You give the agent new sources. It reads them again. A periodic *lint* pass checks for contradictions and stale claims. This works when *you* control when the sources change.

Source code will not wait for you. It changes all the time. Silently. From every commit and every teammate.

So the freshness check must be automatic, cheap, and impossible to fudge. That is the part which makes the full thing safe.

A `page-wiki.md` stores the git blob hash of each source file it describes. Then checking freshness is trivial and exact. You re-hash the current source files and compare:

- **All hashes match → the page is FRESH.** Reuse it. Do **not** re-read the source.
- **A hash differs → that file DRIFTED → the page is STALE.** Re-read *only the changed files*, update the summary, re-anchor.

{{< wiki-animation >}}

You can also just timestamp each file ("last updated on…"). That is fine for "when did we last touch this."

But a timestamp cannot tell you if the *bytes* actually changed. Only if the clock moved.

On code, that is the difference which matters.

A content hash either matches what is on disk or it does not. No "I think this is probably still correct."

So the wiki fails loudly. It tells you the moment it is out of date. Which is exactly the moment a naive copy would silently give you a wrong answer.

---

The catch is the part people skip. You have to build the index first. Understanding a page and writing its `page-wiki.md` is real work.

But this work you do one time. And the LLM does it, because it is exactly the boring type. Every future request gets the benefit. Build one time, reuse many times.

At query time, the full loop looks like this:

<img src="/images/page-wiki-query-flow.png" alt="Sequence diagram of one page-wiki request: the LLM resolves the page via wiki-index, reads the distilled page-wiki.md, re-hashes the source files against the stored hashes, then reuses the page when FRESH or refreshes and re-anchors it when STALE" loading="lazy" width="1300" height="940" style="max-width:100%;height:auto;border-radius:8px;">


---

## What does a real demo look like?

Talking about token savings is easy. So I built a small demo. You can run the loop and measure it yourself:

**<a href="https://github.com/arungudelli/token-llm-wiki" target="_blank">github.com/arungudelli/token-llm-wiki</a>**

Both pieces are deployed to GitHub Pages. No setup needed to see the pattern working:

- <a href="https://arungudelli.github.io/token-llm-wiki/app/" target="_blank">**Live Angular bookstore**</a>, the toy codebase which the wiki describes.
- <a href="https://arungudelli.github.io/token-llm-wiki/" target="_blank">**Live wiki**</a>, one `page-wiki.md` per page, rendered as a Hugo site. Open the <a href="https://arungudelli.github.io/token-llm-wiki/pages/book-list/" target="_blank">book-list entry</a> to see exactly what an LLM reads instead of the source.

It is three pieces:

| Folder | Role |
|---|---|
| `app/` | A toy **Angular bookstore** (list → detail → cart). This is the "codebase" an assistant would otherwise read file by file. |
| `wiki/` | A **Hugo** site: one `page-wiki.md` per page plus a `wiki-index` resolver. This is the wiki layer. |
| `tools/` | `facts.mjs`, a dependency-free CLI that runs the whole loop: resolve → check freshness → compare → demo. |

Here is a real `page-wiki.md` from the demo.

Nothing fancy. Plain markdown, small YAML frontmatter, and links to related pages. One file which renders as a web page for humans and reads as plain text for an LLM.

The only thing I added is the `source-hashes` block. That is the anchor:

```markdown
---
title: "Book List — Page Wiki"
node-id: book-list
summary: "Bookstore catalog: responsive grid of books with search + genre filter, and an add-to-cart button per card."
resolve-terms: [catalog, browse books, book grid, genre filter, search books, add to cart]
routes: /books
last-anchored: 2026-09-16
source-hashes:
  - file: app/src/app/pages/book-list/book-list.component.ts
    hash: f033198f679e96d10779a231c35eb111d5aac46a
  - file: app/src/app/pages/book-list/book-list.component.html
    hash: 8c68e988d6a7160c146ca4e896855875a0d5f79f
  # …one hash per source file the page describes
---

## Overview
Standalone component `BookListComponent` (route `/books`, the app's default). Renders the
whole catalog as a card grid with a live search box + genre `<select>`, plus a per-card
**Add to cart**.

## Gotchas
- Filtering is client-side over the full in-memory list — fine for the demo, would need
  server paging for a real catalog.
- `Add to cart` mutates shared `CartService` state; the header/cart count updates
  reactively everywhere.
```

That "Gotchas" section is the full point. A model which reads *this* already knows the non-obvious things. The things it would otherwise work out again by reading every file.

---

## What does it actually save?

The CLI (`node tools/facts.mjs compare-all`) compares the cost two ways for each page. Re-reading all the source files, versus reading the single `page-wiki.md`:

| Page | Source files | Re-read source | Reuse `page-wiki.md` | Saved |
|---|---|---|---|---|
| `book-list` | 5 | ~1,277 tok | ~593 tok | **~54%** |
| `book-detail` | 6 | ~1,414 tok | ~680 tok | **~52%** |
| `cart-checkout` | 6 | ~1,027 tok | ~590 tok | **~43%** |
| **Total** | 17 | **~3,718 tok** | **~1,863 tok** | **~50%** |

Roughly half the tokens. Per page, per visit. On a toy app where the files are already small.

On a real page with a service, two-three models, a template, and its styles, the gap is bigger. The `page-wiki.md` size stays flat while the source it replaces keeps growing.

So take these demo numbers as a floor, not a ceiling. This is a tiny toy repo. On a large codebase where one page pulls thousands of tokens of source, a one-page summary saves much more.

One thing to be clear about. This is a saving on **input tokens**. The context you feed into the model.

You are not re-reading and re-analysing the source on every request. So the prompt you send in becomes small. That is the full win. It is on the input side.

**Output tokens**, what the model writes back, do not change. The same edit still has to be typed out.

But in a coding session the input is much bigger than the output. The code you pour in is far bigger than the answer which comes out. Reducing the input is exactly where the cost is.

A fair-play note on the numbers. The demo estimates tokens with the well-known `~4 characters per token` rule of thumb. Not an exact BPE tokenizer.

That is on purpose. It is more than enough to show the *relative* saving. And you can swap in `tiktoken` behind the same function if you want exact figures.

The point is you stop paying full price to learn the same page again. The exact second decimal does not matter.

The freshness check is also cheap:

```text
$ node tools/facts.mjs check-all

book-list:     FRESH (5/5 source hashes match)
book-detail:   FRESH (6/6 source hashes match)
cart-checkout: FRESH (6/6 source hashes match)
```

The full loop, end to end:

```text
$ node tools/facts.mjs demo "book list"

resolve "book list":  [2] book-list  Book List — wiki/content/pages/book-list/page-wiki.md
book-list: FRESH (5/5 source hashes match)
=> REUSE page-wiki.md — read ~593 tokens instead of ~1277 (saved ~54%). Source NOT re-read.
```

Resolve the page. Check it is fresh. Reuse the page. For a comprehension pass, the source is never opened.

---

## What happens across a whole team?

That ~50% is per page, per visit, for *one* person.

The wiki is not personal. It lives in the repo, in version control, right next to the code. So it is shared.

One engineer understands the book-list page one time. Its `page-wiki.md` goes into the repo. From then on, every teammate (and every future session of his own) starts from that page. Nobody works it out again.

Now do the large-team maths. Take thirty engineers. Each opening a few AI sessions a day. All working on the same few hundred pages.

Without a shared wiki, every one of those sessions re-reads the same code from zero. The same page found again thousands of times a week.

With one wiki, that discovery happens once per page. Everyone else reuses it. The saving spreads across the full team, not only your own sessions.

And you don't have to document everything up front. The pages get built as you go.

The trick is to make it a pipeline. Every task starts by resolving the page. Then asks one question. Does a fresh wiki page already exist?

- **Yes** → reuse it. You paid nothing to make it. You just ride the shared knowledge.
- **No, or it is stale** → the LLM produces (or refreshes) the `page-wiki.md` right there, anchors it, and *then* does the work.

Either way you get your answer. The difference is the second path leaves a fresh page behind. So the next session, and the next teammate, find it ready.

<img src="/images/page-wiki-team-pipeline.png" alt="Flowchart of the produce-or-reuse pipeline: a prompt resolves to a page via wiki-index; if a fresh page-wiki.md exists it is reused without re-reading source, otherwise the LLM produces or refreshes and anchors it, then the work is done and the page is reused by the next session or teammate" loading="lazy" width="1120" height="1000" style="max-width:100%;height:auto;border-radius:8px;">


Yes, you have to build the index first. But "first" is lazy and step by step. The first person who touches a page pays to make it. Everyone after him rides free.

The wiki is a living artifact which you maintain, same as you maintain the code. It just happens to be maintained mostly by the one worker who does not mind the upkeep.

---

## When is this worth it?

I want to be honest about the trade-offs. This is not free.

**It helps when:**

- The codebase is **large and fairly stable**. You come back to the same areas often, and they do not churn every hour.
- You work across **many sessions**. The wiki spreads its cost over every future visit. The more you return, the more it saves.
- The non-obvious knowledge (gotchas, data flow, cross-file coupling) is **expensive to rediscover** each time.

**It is not worth it when:**

- The code changes constantly. You will spend all your time re-anchoring stale pages.
- The codebase is small enough that reading it costs nothing anyway.
- The work is a one-shot throwaway which you will never touch again.

There is also a real fidelity cost to know about. A distilled summary is, by definition, lossy. If a page shows one field and skips a sibling's exact type, an assistant which trusts the page can miss that detail.

The fix is to be careful about what the summary carries. Record the *shapes* and the *differences* which matter. And confirm the small details from source when a change actually depends on them.

A page wiki is a starting point. Not a replacement for looking when it counts.

**A few honest edges, from actually using it.**

I did not hit these in theory. Each one bit me while building the demo and running the pattern on my own code. They are worth knowing before you depend on it:

- **The hash is byte-level, not meaning-level.** A reformatted import or a renamed local variable flips a page STALE even though the summary is still perfectly true. The first time a formatting-only commit turned one of my pages red, it drove the lesson home: treat STALE as *"re-verify,"* not *"rewrite from scratch."* Most of the time a quick glance confirms the distilled truth still holds, and you just re-anchor.
- **Reuse is a discipline, not a guarantee.** The anchor tells you a page *can* be trusted. It does not force reuse. Early on I would still catch myself opening the source "just to be sure" and burning the tokens anyway. That is the whole reason [a command pipeline](#what-is-still-missing) matters. The tooling is what actually decides when to lean on the page and when to fall back to source.
- **Editing still reads the file you are changing.** This one caught me out at first. I expected the page to replace the source outright. It does not. The biggest saving is on *understanding*: the data flow, the coupling, the gotchas you would otherwise work out again. You will still open the one file you are about to patch. That is fine: working out the understanding again is the expensive part, and that is exactly what the page saves.

None of these break the idea. They are the natural next things to sharpen (a meaning-aware anchor, a resolver which double-checks itself). And they are why this is a starting pattern to build on, not a finished tool.

---

## Who writes the wiki, the LLM or the human?

The full thing is only as good as the knowledge inside it.

An accurate page saves you tokens *and* gets the change correct. A slightly wrong one saves tokens and silently misleads you.

So accuracy is the real lever. That is where the human comes back in.

An LLM is very good at the *first draft* of a page. It reads everything and writes down what it saw. Fast and without complaining.

But the best `page-wiki.md` is one which a human has reviewed. A human catches what the model skipped. And knows the gotcha which is not written anywhere in the code.

That is the best of both worlds. The LLM does the boring bulk. The human does the judgement.

And it should not be a one-time review.

You are mid-session. You notice a page missed something. A mismatch, a subtle behaviour, a gotcha the model never showed. You should be able to just say so, and that correction goes straight back into the page.

That is a second pipeline worth building into your setup. Correct-in-place, along with produce-or-reuse. The moment a human spots a gap, the fix lands in the wiki.

So the next session, and the next teammate, get the sharper version. Over time the wiki stays fresh and actually gets *smarter*. Every human correction is a permanent upgrade which everyone downstream rides for free.

---

## What is still missing?

The demo CLI shows each step by hand. Resolve, check, compare, reanchor. That is on purpose. It makes every part of the loop visible and measurable.

But running it by hand is not how this scales.

The steps are fully deterministic. Resolve the page. Check freshness against the source hashes. Update the summary if anything drifted. Re-anchor. That is a pipeline. And pipelines belong in commands, not in prompts.

The natural fit is a shared command which everyone on the team runs the same way:

- A **Claude Code command or skill** which wraps the full loop. When you start work on a page, it resolves the page, checks freshness, and hands you a ready wiki. Or generates one if it does not exist yet.
- A **post-commit hook** which detects which source files changed, finds the affected page wikis, and re-anchors them automatically. Without anyone remembering to.
- A **CI step** which runs `check-all` on every PR and flags any page wiki which drifted from the diff.

When a new file is added to the codebase, the pipeline sees it has no hash in any existing wiki. It adds it to the correct page's source list and re-anchors. The wiki grows along with the codebase instead of lagging behind it.

This is what turns the pattern from a habit which a few careful engineers maintain into infrastructure which the whole team depends on. The CLI in the demo is the core logic. The command pipeline is the wrapper which makes it invisible.

The idea is yours to adapt. Build the wrapper one time for your stack, and the wiki takes care of itself.

---

## Want to try it yourself?

Clone it, run the loop, watch the numbers:

```bash
git clone https://github.com/arungudelli/token-llm-wiki.git
cd token-llm-wiki
node tools/facts.mjs compare-all
node tools/facts.mjs demo "book list"
```

Then edit a source file in `app/`, run `check-all` again, and watch that page flip to **STALE**. The anchor catches the drift immediately.

Your codebase deserves a wiki which stays true. One which your team can read and your AI can reuse. Instead of one which rots the moment you write it.

If you try it on your own project, tell me what saving you measure.
