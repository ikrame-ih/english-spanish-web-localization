# Paired-run protocol

This protocol measures the effect of this skill without representing a handcrafted rewrite as a model result.

## Eligible case

Run only a case whose record supplies the source string, exact source and target locales, visible function or surrounding context, a public immutable source URL, retrieval date, locator, and its permitted context sources. Existing target copy is evidence, not automatic ground truth.

## Conditions

Run each case twice in fresh, isolated contexts. Randomise condition order for each case.

| Condition | Context supplied to the agent |
|---|---|
| Baseline | The identical case payload, task prompt, model, reasoning level, tools, and permitted sources. Do not load this skill. |
| Skill-assisted | The identical payload and runtime configuration, plus this skill and only the guides it routes to for the target locale and content type. |

Do not give either condition the other output, an expected answer, a reviewer rationale, or a score. If a case permits project-source lookup, make precisely the same read-only sources available in both conditions; the difference must be the skill instructions, not hidden access.

## Required run record

Store one immutable record per condition with at least:

```json
{
  "case_id": "external-001",
  "condition": "baseline",
  "model": "gpt-5.6-terra",
  "reasoning_effort": "medium",
  "agent_and_version": "record exact runtime",
  "run_at": "ISO-8601 UTC",
  "prompt_sha256": "...",
  "tool_policy": "...",
  "source_snapshot": "case payload revision or SHA",
  "raw_output": "...",
  "parsed_decision": "pass | change | ask | invalid",
  "error": null
}
```

`gpt-5.6-terra` at `medium` is the initial cost-conscious configuration. Record the provider's resolved model ID and all non-default settings; do not assert a seed, temperature, or determinism when the runner cannot set and report them.

## Scoring

Hide condition labels and randomise outputs before review. A reviewer scores each output using `benchmarks/rubric.md`, marks the expected decision independently, and records a concise rationale tied to the supplied context. Disagreements or unresolved material ambiguity are reported, not averaged away.

Publish aggregate results only after both conditions complete for every included case. Report missing/error cases, score distribution, decision accuracy, sample size, exact corpus revision, model configuration, and the limits of the comparison. A case study, screenshot, or GIF may use only records produced by this protocol.

## Current state

The protocol is ready, but it has not run in this repository. A runner with access to the selected model is required to produce the raw paired outputs; this document is not evidence of performance.
