# Localization quality gates

Use these gates for audits and before release. Separate objective defects from optional style improvements.

## Release blockers

- Missing or extra locale keys; untranslated production strings.
- Changed, missing, or malformed placeholders, ICU branches, tags, Markdown links, or interpolation syntax.
- Meaning reversals, omitted constraints, invented claims, wrong prices, or incorrect legal/product behavior.
- Broken locale routing, fallback, canonical URLs, alternate-language metadata, forms, or transactional flows.
- Critical text clipped, hidden, overlapping, or inaccessible at supported breakpoints.
- Copy shortened by losing meaning, conditions, or recovery guidance merely to fit a component.
- Incorrect pluralization, agreement, date/number/currency rendering, or ambiguous converted values.
- Alt text, accessible names, consent, errors, or recovery instructions absent where the source provides them.
- Missing or invalid page/fragment language declarations, or a localized visible label no longer contained in the control's accessible name.
- Non-reciprocal or invalid `hreflang` annotations, wrong locale tags, or alternates pointing to non-equivalent pages.

## Linguistic and UX defects

- Literal translation that conflicts with page, domain, or user-journey context.
- A grammatical calque whose target-language reading selects the wrong real-world sense, journey, or product concept. This is not a preference: classify it as **Accuracy** when meaning changes, otherwise **Fluency**, and include a corrected rendering in an audit.
- False friends, calques, mixed target-language varieties, inconsistent treatment, or terminology drift.
- Any cross-locale leakage: UK conventions in `en-US`, US conventions in `en-GB`, Spain-only usage in `es-419`, or Latin-American-only usage in `es-ES`.
- CTA text that does not predict the resulting action.
- Headline, navigation, error, or form copy that is grammatically valid but unnatural for its function.
- Search snippets or metadata that misrepresent the page or exceed project constraints.

## Error model

Classify each issue by category and severity:

- **Accuracy:** mistranslation, omission, addition, factual distortion, or untranslated content.
- **Terminology:** wrong domain term, inconsistent concept, or unauthorized product-name change.
- **Fluency:** grammar, syntax, spelling, punctuation, register, or unnatural target-language usage.
- **Locale convention:** wrong language variety, formats, units, address/name behavior, or cultural convention.
- **Style:** house-style, voice, capitalization, or avoidable verbosity.
- **Design/functional:** truncation, broken interaction, placeholder/markup damage, accessibility, SEO, or locale routing.

Severity is based on user impact, not how conspicuous the wording looks:

- **Critical:** can cause harm, legal/financial exposure, data loss, unsafe action, or a broken primary journey.
- **Major:** changes meaning, misleads users, breaks functionality, violates a required term, or materially damages comprehension.
- **Minor:** localized defect with limited impact that still warrants correction.
- **Preference:** defensible alternative with no objective defect; never report it as an error.

Do not label a contextual calque as a preference just because readers can infer the intended source-language meaning. Evaluate the target-language reading first: if it naturally evokes a contradictory action, object, setting, or user journey, it is a defect. If the supplied context cannot settle that reading, ask one targeted question before categorising it as style or preference. Severity follows the affected surface: a key product claim, CTA, onboarding step, or safety/recovery instruction is normally at least **Major**; an isolated descriptive phrase may be **Minor**.

A release passes only with zero critical and zero major issues, all deterministic integrity checks passing, and every required surface accounted for. If the project accepts another threshold, state it explicitly.

## Deterministic catalog check

For two JSON locale catalogs, run:

```bash
python3 scripts/locale_guard.py path/to/source.json path/to/target.json
```

The script detects duplicate JSON keys, missing/extra leaves, type and empty-target defects, named and printf placeholder drift, opening/closing tag drift, Markdown link-target changes, unbalanced braces, edge-whitespace changes, likely encoding corruption, non-NFC target strings, and suspicious identical text. Use repeatable `--allow-identical KEY` only for intentional identical strings.

Optionally add `--warn-expansion 1.4` or another project-approved ratio to identify strings that deserve visual review. This is a triage signal, not a layout test: character count cannot predict rendered width, and a flagged translation must not be shortened by deleting meaning.

It is a structural guard, not a linguistic reviewer. Investigate every finding; do not copy source text into the target merely to make the check pass. Exit `0` means structural checks passed, `1` means findings exist, and `2` means a catalog could not be safely parsed.

## Review sequence

1. Structural integrity and build/tests.
2. Completeness against the surface inventory.
3. Accuracy against source and product behavior.
4. Monolingual naturalness in target context.
5. Terminology and target-locale consistency.
6. Visual and interaction QA at representative breakpoints.
7. SEO, accessibility, and transactional-path checks.

Visual QA must cover navigation, buttons, tabs, cards, tables, form labels, errors, empty states, dialogs, mobile widths, desktop widths, the longest plural/select branches, 200% zoom where applicable, and increased text-spacing checks. Compare screenshots or rendered output when available. A catalog-only review cannot certify layout fit.

Report findings with severity, location/key, source, current target, problem, and recommended correction. Group systemic issues so reviewers can fix the cause rather than dozens of symptoms.
