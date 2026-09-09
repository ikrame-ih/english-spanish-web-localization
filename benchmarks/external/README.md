# External evidence pack

This directory contains the independent corpus that takes priority over further portfolio-only cases. The 30 records in [`cases.jsonl`](cases.jsonl) are real, public user-facing catalogue strings from three products not owned by this repository's author. Each pair is pinned to a public source commit and was retrieved on 2026-09-09.

## Admission rules

Each case must have all of the following:

1. Real, public, user-facing source and target copy from a product not owned by this repository's author.
2. A public URL for both locale versions; use a commit permalink when the source is a public localisation catalogue.
3. An explicit locale route, not an inferred generic language. The initial coverage target is `es-ES → en-GB`, `es-ES → en-US`, `en-GB → es-419`, and `en-US → es-419`.
4. A retrieval date and an observable page, key, or component locator.
5. Enough real context to assess meaning, register, terminology, and UI function.
6. A human-reviewed expected decision: pass, change, or ask. Do not use an existing translation as unquestioned ground truth.

Reject examples whose locale cannot be established, whose source is private, whose page context cannot be checked, or whose wording must be invented to make the case interesting.

## Publication rule

The pack contains 30 cases drawn equally from Box Annotations, CodeCombat, and Mouse Tooltip Translator. Report it separately from the portfolio regression corpus and never merge their scores.

## What the records establish

- The source and observed target are real product strings, not invented prompts.
- The source and observed-target URLs make each string independently checkable.
- Existing observed copy is evidence, **not** automatic ground truth. The human-reviewed `expected` decision may be `pass`, `change`, or `ask`.
- `es-ES → en-GB`, `es-ES → en-US`, `en-GB → es-419`, and `en-US → es-419` all occur in the corpus.

This is still a benchmark corpus, not an executed model comparison. Paired outputs and aggregate results must follow [`../paired-run-protocol.md`](../paired-run-protocol.md).
