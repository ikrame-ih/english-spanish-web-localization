# Public real-world regression corpus

This is a 30-case contextual-localisation audit corpus. Every source and observed Spanish target is real, public, user-facing copy from [ikrame.dev](https://ikrame.dev/), retrieved on 2026-09-09. There are no invented sentences, simulated UI limits, or fictional product contexts.

To verify a case, open [ikrame.dev](https://ikrame.dev/), use its visible `EN / ES` language switcher, and find the section named in `locator`. Each JSON line records the exact English source, the actual current Spanish target, and the review decision a strong audit should reach.

## Scope

This is a transparent **portfolio regression corpus**, not a universal claim about every website, language market, or model. Its value is that anyone can independently inspect every source/target pair, including the `landing` → `aterrizar` failure that motivated this skill.

Future packs must use the same standard: real public text, public source URL, observed context, a recorded retrieval date, and no synthetic cases. They should add independently owned products and explicit locale tags before any broad best-in-class claim is made.

## Run protocol

1. Fix model, reasoning level, prompt, browsing policy, date, and evaluator.
2. Run all cases without the skill, then with the skill loaded. Do not expose `expected` to either condition.
3. Save raw outputs and metadata.
4. Have a human reviewer score blinded results with [`rubric.md`](rubric.md).
5. Publish all scores and non-improvements, never only favourable examples.

Use this same prompt in both conditions:

```text
Audit the observed Spanish copy against the English source and page context. Distinguish
an objective localisation defect from a defensible preference. Preserve technical terms
and identifiers when justified. If the public context cannot settle a material choice,
ask one concise question. Return: verdict, corrected copy only when needed, and rationale.

<case JSON without expected>
```
