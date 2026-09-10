# Offline validation (no model calls)

Use this when you need confidence that the **package** works without spending Cursor/Codex quota on paired benchmark runs.

## What is already proven offline

Run from the repository root:

```bash
python3 -m unittest tests.test_locale_guard -v
```

Expected: four tests OK (valid catalog, missing key, placeholder drift, non-NFC + expansion warning).

Optional manual check:

```bash
python3 scripts/locale_guard.py path/to/source.json path/to/target.json
python3 scripts/locale_guard.py path/to/source.json path/to/target.json --warn-expansion 1.4
```

These checks are structural. They do **not** prove linguistic quality or rendered UI fit.

## What still needs controlled model runs (quota)

Do not claim skill vs baseline improvement until you have blinded paired results:

1. Portfolio regression: `benchmarks/cases.jsonl` (30 cases) — see `benchmarks/README.md`.
2. Optional low-cost pilot: `benchmarks/pilot/` (12 cases × 2 conditions = 24 chats) — subscription usage, no paid API key required if you use an existing agent allowance carefully.
3. External pack: `benchmarks/external/` — collecting sources; do not publish empty scores.

A previous Windows Cursor CLI pilot ZIP (`shared-background-v2`) can dry-run without model calls. A full `--run` (eight `cursor-grok-4.6-medium` calls) is expensive and was paused after a transport/JSON failure on call 1/8. Prefer the pilot folder or **one** carefully scoped paired case after an explicit usage OK.

## Install smoke check (still no localization calls)

```bash
npx skills add ikrame-ih/english-spanish-web-localization
```

Confirm the skill folder name is `english-spanish-web-localization` and that `SKILL.md` plus `references/` are present. Updating this repo does not auto-update an older installed copy.

## Documentation checklist before calling the skill "done"

- [ ] `python3 -m unittest tests.test_locale_guard -v` passes
- [ ] README install + invoke examples match current Skills CLI
- [ ] Benchmark tables show honest status (Not run / Collecting) until scores exist
- [ ] No fake paired screenshots in README
- [ ] `benchmarks/showcase.md` rules respected
- [ ] Instant mini-proof folder present (`benchmarks/results/instant-mini-2026-09-10/`) (optional human check)
- [ ] Any usage-heavy paired run has a recorded model, date, and blinded review plan
- [ ] Skills CLI install smoke: folder appears under the agent skills dir with SKILL.md + references/

## ChatGPT / Cursor note

When driving agents in ChatGPT or Cursor for this skill, use English in-product prompts and pick the lightest model that can follow the skill (rotate Terra/Astra/Grok effort by task). Do not burn an eight-call medium pilot by default.
