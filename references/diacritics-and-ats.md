# Diacritics, Unicode, search, and ATS compatibility

## Default rule

Write correct target-language orthography. Preserve accents, diaereses, inverted punctuation, apostrophes, and `ñ` in human-facing text and personal, company, place, product, and institutional names. Never strip diacritics speculatively or present misspelled Spanish as an ATS optimization.

Store and emit text as Unicode, preferably UTF-8, and normalize comparable text to NFC where the system permits. Preserve code points in source-controlled content; do not replace letters with images or visual glyph substitutes.

## Separate display from matching

Treat canonical display text and machine matching as different layers:

- **Display:** correct spelling and the person's preferred name.
- **Search/index alias:** optionally add a normalized or ASCII-folded alias in a dedicated machine field when the system supports it and the requirement is proven.
- **Identifiers:** follow the receiving system's documented character contract; do not infer it.

Never overwrite canonical content with its ASCII-folded form. Never add noisy visible duplicates such as `administración / administracion` merely to game matching. If exact source keywords matter for recruitment, use their correct target-language equivalents and retain official technical terms where truthful.

## CV and ATS mode

For an ATS-facing CV or application:

1. Keep accents and names correct by default.
2. Prefer selectable text, standard fonts, conventional section headings, a simple reading order, and restrained columns, tables, headers, footers, text boxes, icons, and graphics.
3. Export to a format accepted by the stated ATS and verify text extraction in reading order. Confirm that names, contact details, headings, dates, skills, and accented words survive copy/paste or parser output.
4. Match relevant job terminology truthfully; do not introduce spelling errors or unsupported keyword stuffing.
5. If a named legacy system demonstrably fails on diacritics, explain the evidence and ask the user before creating an ASCII compatibility variant. Preserve the canonical accented version and never alter a person's name without explicit approval.

If the target ATS, submission country, or compatibility requirement is unknown and it could change the deliverable, ask the user. Do not promise universal ATS compatibility: parsers differ and document structure often causes failures independently of language.
