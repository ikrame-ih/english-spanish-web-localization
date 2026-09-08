# Shared English localization guidance

## Confirm the variety

- Infer the target from audience, domain, URL, locale files, existing English copy, and house style.
- Use the separate `en-GB` or `en-US` guide. If neither can be inferred, ask; do not silently produce generic or mixed English.
- Never mix locale conventions merely because both forms are understood.

## Voice and syntax

- Rebuild the sentence naturally; do not mirror Spanish word order.
- Prefer concise, concrete verbs and active voice. Remove unnecessary articles, duplicated nouns, long prepositional chains, and subjects that English requires but Spanish omits only after resolving their referents.
- Resolve Spanish pronouns, gender, `ser`/`estar`, and omitted subjects from context. Do not invent gender when English can remain neutral.
- Translate emphasis rather than importing intensifiers mechanically. Avoid false friends such as `actual`, `eventual`, `assist`, `pretend`, `sensible`, `constipated`, and `compromise`; verify meaning in context.
- Adapt idioms, humour, institutional references, qualifications, and culture-bound terms by communicative effect. Retain a Spanish term when it names a Spain-specific institution or document and an English substitute would misrepresent it; add a concise gloss if useful.

## Web and UI conventions

- Follow the existing house style for sentence case or title case. Without one, prefer sentence case for UI and headings.
- Use short, outcome-oriented CTAs: `Get started`, `View projects`, `Request a demo`, `Create account`.
- Write actionable, non-blaming errors. Keep button and navigation labels parallel.
- Use natural contractions when the brand voice is conversational; avoid them in formal or legal copy when inappropriate.
- Preserve official product and UI names. Do not translate Spain-specific identifiers such as `NIE`, `padrón`, or official programme names into a misleading supposed equivalent; explain them according to audience need.

## Locale data

- Use the exact locale, not generic assumptions, for human-facing dates, times, numbers, currency, units, addresses, and phone numbers.
- Avoid ambiguous all-numeric dates. Use month names or an unambiguous product-approved format when audience is international.
- Preserve machine-readable ISO dates, API values, database values, and identifiers.
- Do not convert currencies or units unless authorized; distinguish formatting from conversion.

## QA

Check spelling variety, agreement, articles, prepositions, referents, capitalization, punctuation, terminology, line length, placeholders, plural/select branches, and markup. Test the copy by function: a headline should scan, a CTA should predict the action, and an error should support recovery.

Run a source-interference pass: challenge Spanish word order, unnecessary articles, abstract-noun chains, impersonal constructions, repeated connectors, overlong sentences, omitted English subjects, cognates, and literal institutional equivalence.

Run a variety pass using the selected locale guide across spelling, vocabulary, punctuation, quotation style, dates, time, units, address conventions, and collective-noun agreement.

Reference hierarchy for uncertain cases: project glossary and observed product usage; the chosen target market's house style; established dictionaries or official institutional terminology; Unicode CLDR or the runtime locale library for structured locale data. For international technical English, favor clear, concise, unambiguous wording.
