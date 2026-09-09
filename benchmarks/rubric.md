# Scoring rubric

Score every case against its `expected` object. Do not use source similarity, back-translation, or fluency alone as proof of a good result.

## Per-case score: 10 points

| Dimension | Points | What earns full credit |
|---|---:|---|
| Meaning and contextual sense | 4 | Selects the sense supported by the supplied product and journey context; preserves factual scope and user outcome. |
| Locale discipline | 2 | Uses Spanish for Spain consistently and does not introduce an unsupported regional variety. |
| Naturalness and voice | 2 | Reads as original target-language product copy and matches the stated register. |
| Terminology and technical integrity | 1 | Uses the established concept term or escalates where no authoritative decision exists; preserves non-translatable structure. |
| Decision handling | 1 | Makes the expected pass/change/ask decision and does not claim a rendered check that the public evidence does not support. |

## Expected-output rules

- `pass`: full credit requires recognising that the observed target is defensible. Do not invent a defect merely because a different wording is possible.
- `change`: full credit requires identifying the material defect and proposing a target that preserves the real page's meaning. The `reference` is an acceptable answer, not the only permitted wording.
- `ask`: full credit requires asking the material terminology or style question recorded in `expected.question`, rather than silently enforcing a preference.
- Do not award release-readiness or a visual-fit claim: this corpus verifies live copy and context, not every responsive state.

## Run-level reporting

Report the total as `points / 300`, then show category subtotals. Keep baseline and skill-assisted prompts, model, reasoning level, date, and evaluator fixed for a paired comparison. Record all prompts and outputs verbatim in a result file.

Human review is the final evaluator. A model may draft a preliminary score, but it must not score its own outputs without independent review.
