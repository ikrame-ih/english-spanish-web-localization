# Visual evidence standard

Use this format for the small set of paired examples shown in the repository README after a benchmark run. A showcase is evidence, not decoration.

## Required evidence for each card

| Field | Requirement |
|---|---|
| Real source | Public URL, retrieval date, and page/key locator. |
| Controlled run | Same model, reasoning level, prompt, tools, and fresh context in both conditions. |
| Baseline | Raw output without the skill, linked to the result record. |
| Skill-assisted output | Raw output with the skill, linked to the result record. |
| Human review | Blinded score and concise rationale. |
| Visual proof | Only for a UI/layout claim: same real component, same viewport, and an unedited before/after capture. |

## README card format

```markdown
| Real source | No skill | With skill | Human review |
|---|---|---|---|
| [Page and locator](URL) | Exact raw output | Exact raw output | Score change and why |
```

Use no more than five cards. Include at least one non-improvement or a case where both outputs are acceptable. Never label a handcrafted comparison as a paired result.

For layout, place the two real captures below the table with descriptive alt text. Do not use a mock-up, a generated image, a GIF, or a resized comparison as proof that a translated component fits.
