# No-extra-cost paired pilot

This is a 12-case manual pilot designed for an agent subscription that already includes usage allowance. It does not call a paid API, use a secret, or make a claim of benchmark results by itself.

## Set up

1. Choose **one** agent, exact model, and reasoning setting. Record all three. Do not compare different providers in this pilot.
2. Prepare two clean agent contexts:
   - **Baseline:** this localisation skill is not available to the agent.
   - **Skill-assisted:** this localisation skill is installed and available.
3. Do not give either context this repository, `benchmarks/external/cases.jsonl`, its expected decisions, or prior outputs. Supply only the individual payload from `cases.jsonl` and the prompt below.
4. Use a brand-new chat for every row in `operator-order.tsv`. Run the rows in that order.

The operator may know the condition in order to set it up. The reviewer must not: remove the condition column when sharing the raw outputs for scoring.

## Prompt

Use this exact prompt in both conditions, followed by one payload:

```text
Audit the observed target copy against the source copy and supplied UI context.
Return valid JSON only:
{"verdict":"pass|change|ask","revised_copy":null|string,"question":null|string,"rationale":"one concise sentence"}.

Use pass when the observed target is defensible. Use change only for a material localisation defect; then supply a revised_copy. Use ask only when the supplied context cannot settle a material decision; then supply one concise question. Preserve placeholders and markup exactly. Do not browse or use other context.
```

## Record and review

Copy each raw response without edits into a private results file with the run ID, case ID, model, reasoning setting, timestamp, and condition. When all 24 runs are complete, shuffle and relabel the outputs before a reviewer scores them with `../rubric.md`.

Do not publish a score, screenshot, GIF, or claim of improvement until the blinded review is complete.

## Scope

The pilot covers all four required routes and includes compact UI, plural ICU syntax, technical labels, and British/US spelling. It is a low-cost signal, not a substitute for the full 30-case paired benchmark.
