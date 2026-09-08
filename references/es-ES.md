# Target locale: Spanish for Spain (`es-ES`)

## Voice and syntax

- Write idiomatic contemporary Spanish used in Spain. Prefer direct, clear sentences and active constructions.
- Choose `tú`, `usted`, or impersonal language from audience and existing brand voice; never switch treatment accidentally. Match verbs, pronouns, and possessives consistently.
- Avoid English-shaped noun stacks, redundant possessives, overused gerunds, passive chains, filler pronouns, and repeated subject pronouns.
- Use natural Spanish information order and collocations. Restructure freely when English syntax sounds foreign.
- Use inclusive, respectful language without making the copy cumbersome or changing factual meaning. Prefer neutral collective nouns and direct second person when suitable.
- Use `vosotros` only when it fits the audience and voice; never mix it with Latin-American plural-address conventions in the same locale.

## Meaning and terminology

- Treat cognates, polysemy, phrasal verbs, and metaphor as high-risk. Validate meaning from page purpose and domain, not the isolated string.
- Resolve metaphor by communicative purpose. A movement verb may describe onboarding, migration, market entry, travel, or physical arrival; choose the domain-appropriate Spanish concept rather than its most common dictionary equivalent.
- Prefer an established Spanish equivalent to an unnecessary Anglicism. Retain terms that are genuinely standard for the audience or product, and format or explain them only when the medium permits.
- Distinguish product labels from descriptive prose. Reuse official UI names and product terminology exactly where applicable.
- Preserve the distinction between a technical `landing page` and the ordinary verb or metaphor `landing`; never translate from a glossary without checking the sense.

## Web and UI conventions

- Use sentence case for headings, buttons, menu items, and labels unless the brand system explicitly requires another style.
- Start CTAs with a natural action verb and match the actual outcome: `Empieza`, `Solicita una demo`, `Ver proyectos`, `Crear cuenta`.
- Keep microcopy short, specific, and actionable. Errors should say what happened and how to recover without blaming the user.
- Use opening and closing question/exclamation marks. Do not insert a space before `:`, `;`, `?`, or `!`.
- Use Spanish quotation marks according to the project's typographic system; prefer angle quotes in editorial prose when no house style exists.
- Do not capitalize days, months, languages, nationalities, job titles, or every major word in headings merely because English does.
- Use correct accents, diaereses, inverted punctuation, and `ñ`; never remove them for speculative machine compatibility.

## Locale data

- Target locale is `es-ES`. Use locale-aware formatting through the project's existing i18n library when possible; do not hand-code volatile format rules.
- Preserve machine-readable ISO dates, API values, database values, and identifiers. Localize only their human-facing rendering.
- Use metric units and local currency only when conversion or adaptation is authorized and accurate. Never silently change the underlying value.
- Follow the project's established date, time, number, and currency format when it is valid for Spain; otherwise use `es-ES` conventions consistently.

## QA

Check agreement, clitics, prepositions, accents, punctuation, capitalization, treatment, terminology, line length, placeholders, plural/select branches, and markup. Read the result aloud mentally: if it sounds like English wearing Spanish words, rewrite it.

Run a source-interference pass: challenge retained English noun stacks, repeated possessives, title capitalization, passive voice, progressive forms, phrasal-verb calques, discourse markers, and metaphor. Keep an apparent Anglicism only when target-market evidence or the project termbase supports it.

Run a Spain-specificity pass: reject Latin-American-only lexical choices or treatment when the requested locale is `es-ES`, including unexplained `ustedes` as an informal plural, while avoiding caricatured regional slang. Prefer broadly natural usage in Spain unless the brief identifies a narrower audience.

Reference hierarchy for uncertain cases: project glossary and observed product usage; current RAE/ASALE resources; FundéuRAE for emerging usage and Anglicisms; Unicode CLDR or the runtime locale library for structured locale data.
