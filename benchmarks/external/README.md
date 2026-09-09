# External evidence pack

This directory is reserved for the independent corpus that takes priority over further portfolio-only cases. It is intentionally empty until every included example satisfies the rules below.

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

Publish the external pack only when it contains at least 30 cases drawn from at least three independent products. Report it separately from the portfolio regression corpus and never merge their scores.
