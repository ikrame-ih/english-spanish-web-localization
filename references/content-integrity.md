# Content-surface integrity

Apply the same contextual-localisation standard to every user-facing or repository content surface. Do not treat web copy as the only valid input.

## Format-aware handling

- **Web and app UI:** inspect the component, interaction outcome, nearby strings, breakpoints, accessible name, and visible layout.
- **Portfolio and marketing copy:** infer voice, audience, project domain, and claims from the whole page or project card before deciding a term.
- **CVs and application materials:** preserve canonical spelling and diacritics; retain selectable text, headings, reading order, dates, factual claims, and role terminology. Read `diacritics-and-ats.md` for ATS work.
- **Markdown and documentation:** preserve YAML front matter, heading hierarchy, code fences, inline code, link destinations, anchors, tables, admonitions, images, reference definitions, and command syntax. Localise prose and visible link labels only when appropriate.
- **Locale catalogues and structured content:** preserve keys, placeholders, ICU branches, tags, IDs, and data types. Run deterministic structural checks where available.
- **Emails, forms, and transactional messages:** preserve actions, conditions, consent, error recovery, deadlines, and the relationship between visible labels and accessible names.

## Reliability contract

Do not promise or report “100% accurate” localisation merely because the result is fluent. A result is ready only when the available evidence supports its meaning, locale, terminology, and format integrity.

If a material decision cannot be justified from the content, product context, established terminology, target locale, or authoritative evidence, stop and ask the user. State precisely what is missing. Never fill the gap with an elegant guess.

Use rendered or extracted evidence appropriate to the format: browser/UI preview for interface fit, Markdown rendering for documentation, and text extraction plus human review for ATS-facing CVs. Mark the specific check unverified when that evidence is unavailable.
