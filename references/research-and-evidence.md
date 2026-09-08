# Research and evidence protocol

Use this protocol only for ambiguity, specialized terminology, official names, regulated copy, or usage likely to have changed.

## Evidence hierarchy

Prefer evidence in this order, while respecting an explicit project glossary:

1. Product source of truth: approved glossary, design system, current UI, legal copy, content model, and stakeholder decisions.
2. Official target-market institution or standards body for the exact concept.
3. Current language authority: RAE/ASALE and FundéuRAE for Spanish; the selected English market's recognized dictionary and house style for English.
4. Domain authorities: legislation, regulators, professional bodies, official product documentation, standards, and established target-market organizations.
5. Unicode CLDR or the runtime's CLDR-backed locale APIs for plural categories and structured locale data.
6. A representative target-market corpus or several reputable native sources for actual usage.

Do not treat search-result counts, a single competitor, machine translation, bilingual dictionaries, or fluent-looking generated text as decisive evidence.

## Verification method

- Define the concept before searching; search for meaning and domain, not only the source word.
- Check the date and target market. Separate normative guidance from observed usage.
- Confirm official names on the owning institution's target-language site. If no official translation exists, preserve the source name and explain it rather than inventing an equivalent.
- For a candidate term, inspect native sentences showing the same sense and grammatical role.
- Prefer evidence from at least two independent authoritative sources when a choice is consequential and no single owner controls the term.
- Record only decisions that future strings need: concept, approved target, context, forbidden alternatives, evidence, and date checked.

## Escalation

Flag rather than guess when wording can change legal scope, eligibility, price, safety, consent, contractual obligation, medical meaning, or institutional identity. Offer concise candidates with their implications and request the missing decision.

For ordinary low-risk prose, do not browse term by term. Contextual judgment and the locale guide are sufficient.

## Maintained primary references

- RAE and ASALE language resources: https://www.rae.es/
- FundéuRAE current usage guidance: https://www.fundeu.es/
- Unicode CLDR: https://cldr.unicode.org/
- Unicode locale identifiers (UTS #35): https://www.unicode.org/reports/tr35/
- UN M49 geographic regions, including code 419: https://unstats.un.org/unsd/methodology/m49/
- W3C Internationalization: https://www.w3.org/International/
- WCAG 2.2: https://www.w3.org/TR/WCAG22/
- Google Search Central multilingual guidance: https://developers.google.com/search/docs/specialty/international/
- Google guidance for clear global English: https://developers.google.com/style/translation
- Greenhouse guidance on resume parsing failures: https://support.greenhouse.io/hc/en-us/articles/200989175-Unsuccessful-resume-parse
- Textkernel supported parsing languages: https://developer.textkernel.com/tx-platform/v10/languages/

Use these as live sources when web access is available; do not assume a locally remembered rule is current.
