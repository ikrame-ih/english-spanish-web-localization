# Worked audit — Task A (defective es-ES UI set)

Skill-guided **audit** of a small, deliberately defective `es-ES` UI/catalog set. The goal is to show the skill applying [`references/quality-gates.md`](../../references/quality-gates.md) and the deterministic catalog checker (`scripts/locale_guard.py`), not to report paired Instant scores. Those Instant numbers live only in [`instant-mini-2026-09-10/`](instant-mini-2026-09-10/).

This write-up is an example I checked myself. The full 30-case blind review is still ahead.

## Scope

- Mode: audit (findings and proposed copy; no product-code edits).
- Target locale: `es-ES`.
- Surfaces: UI strings plus a JSON locale catalog.
- Source material: QA fixtures (not in this repo). Do not expect a `fixtures/` tree here.

## locale_guard (structural)

Ran `python3 scripts/locale_guard.py` against the source/target catalog pair from the QA fixtures (not in this repo).

| Severity | Code | Finding |
|---|---|---|
| MAJOR | `PLACEHOLDER_MISMATCH` | A target string dropped or altered a named/printf placeholder that the source still uses. Release blocker under quality gates: placeholders must be preserved exactly. |

Investigate the mismatch; do not copy English into the target merely to silence the checker. Exit `1` with findings is the expected outcome on a defective catalog.

`--warn-expansion` (if used) only flags character-count growth for visual review. It is not a layout test.

## Linguistic / locale findings

| Area | Issue | Why it matters for `es-ES` | Proposed direction |
|---|---|---|---|
| Locale leakage | `computadora` where the product UI is Spain Spanish | `computadora` is typical of Latin American usage; Spain product copy prefers `ordenador` unless a house term exists | Replace with `ordenador` (or the project termbase equivalent) |
| Unnecessary Anglicism | `trackear` | Prefer an established Spanish verb (`seguir`, `rastrear`, according to the actual product action) | Use the concept that matches the UI, not the English stem |
| Polysemy | `coger` in a potentially ambiguous UI string | In Spain the verb can be fine in some senses and crude or misleading in others; short UI copy is high-risk | Rephrase with an unambiguous action (`coger` → `tomar` / `recoger` / `seleccionar` as context requires) |
| CTA expansion | CTA grown far beyond source without adding meaning | Length is a localization constraint; expansion that does not change outcome still needs visual QA | Keep the action verb and outcome; shorten without dropping recovery or conditions |
| Identical source | `We're hiring` left in English | Suspicious identical strings are a `locale_guard` signal; hiring CTAs are usually translatable | Localize (`Estamos contratando` / `Únete al equipo`) unless the brand keeps English on purpose (`--allow-identical` only then) |

## Revised catalog (illustrative)

After fixing placeholders and the issues above, a corrected `es-ES` catalog would:

1. Restore every source placeholder and tag.
2. Use Spain vocabulary (`ordenador`, not leaked `es-419` terms).
3. Replace `trackear` and risky `coger` with context-true Spanish.
4. Keep CTAs short and predictive of the click outcome.
5. Translate `We're hiring` unless identity-as-English is an explicit exception.

Exact key/value tables belong with the QA fixtures (not in this repo). This file does not invent those keys.

## Quality-gate outcome

- Structural: `PLACEHOLDER_MISMATCH` is a **major** integrity defect until fixed.
- Linguistic: leakage, Anglicism, and polysemy are **major** or **minor** depending on the surface; CTAs that mislead or overflow a primary control trend **major**.
- After the proposed corrections: **Overall Task A PASS** — zero remaining critical/major issues on this fixture set, with visual UI still **unverified** (no rendered breakpoints in this write-up).

Residual risk: catalog-only review cannot certify layout fit; identical-English exceptions need a recorded house-style decision.
