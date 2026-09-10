# Instant mini-proof — 2026-09-10

## Setup
- Model: ChatGPT Instant
- Same prompt shape both conditions; skill condition prepends skill invocation / SKILL guidance (see `*-skill-prompt.txt`)
- Fresh chat per condition
- Cases from public `ikrame.dev` portfolio corpus (`benchmarks/cases.jsonl` ids)

## Cases
| Case | Source | Gold |
|---|---|---|
| ikrame-19 | https://ikrame.dev/ — Project: Málaga Onboarding description | `change` (avoid calque *aterrizar*; prefer install/settle wording) |
| ikrame-08 | https://ikrame.dev/ — technical terminology string | `ask` (house-style: keep EN terms vs localize?) |
| mtt-05 | MTT-style UI position pair (Above) | `change` → *Arriba* (baseline already correct; skill not re-run) |

## Human review note
Author review of this Instant probe only — **not** the 30-case blinded portfolio protocol. No improvement percentage claimed for the full corpus.
