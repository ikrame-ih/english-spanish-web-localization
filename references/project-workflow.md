# Project-wide localization workflow

Use this guidance for repositories, CMS exports, locale catalogs, or multi-page products.

## Discover

Identify framework and localization mechanism before editing. Search for locale directories, translation functions, content collections, CMS schemas, route metadata, manifests, email templates, validation messages, image text, and hard-coded user-facing strings. Respect repository instructions and existing architecture.

Build a surface inventory grouped by:

- navigation and shared chrome;
- pages and reusable components;
- forms, validation, errors, empty/loading/success states;
- authentication, billing, consent, and transactional flows;
- SEO metadata, social cards, structured data, and sitemaps;
- accessibility names, alt text, captions, and transcripts;
- emails, notifications, downloadable content, and CMS-managed copy.

Distinguish source-of-truth content from generated output. Edit the source, never compiled bundles or generated artifacts unless the project explicitly requires it.

## Establish locale behavior

Determine source and target locale tags, fallback behavior, routing strategy, detection, persistence, canonical and alternate URLs, and whether content or formatting varies by market. Do not redesign locale architecture unless requested.

Use the project's i18n library for plurals, selects, dates, numbers, currency, relative time, and lists. Do not concatenate fragments that require language-dependent word order or agreement.

Declare the page language on the root HTML element and mark meaningful inline language changes when the framework permits. Use valid BCP 47 language tags. Keep visible labels aligned with accessible names after localization.

## Build terminology and context

Create a working termbase before bulk localization. Each entry should capture concept, source term, approved target, context or part of speech, forbidden alternatives, and product-specific notes. Extract repeated terms, navigation labels, product concepts, institution names, and ambiguous verbs first.

Associate short strings with their component, page, screenshot, or developer comment. If a key such as `open`, `apply`, or `plan` has multiple senses, split or annotate it rather than forcing one translation everywhere.

## Implement safely

Preserve key sets and nesting unless a migration is requested. Keep placeholders and markup structurally equivalent. Translate complete messages rather than concatenated fragments. Provide enough text around links for grammatical agreement and accessibility.

When localizing embedded source files, change only user-facing copy. Do not translate variable names, API fields, test selectors, analytics identifiers, CSS classes, routes, or filenames unless they are explicitly designed for localization.

Keep commits or change sets reviewable by separating infrastructure changes from copy changes when practical.

## Control text expansion and layout risk

Treat every string as content inside a component, not an unlimited paragraph. Record known constraints such as maximum characters, available width, intended line count, responsive breakpoints, fixed-height containers, table columns, navigation density, and neighboring controls.

Use this order when localized copy does not fit:

1. Rewrite idiomatically and more concisely without losing meaning, scope, tone, or required terminology.
2. Use an approved shorter term or UI pattern and record it in the termbase.
3. Improve the component's resilient layout when code changes are authorized: wrapping, intrinsic sizing, flexible height, sensible min/max widths, or a responsive alternative.
4. Ask the user to choose when meaningful trade-offs remain, such as shorter but less explicit copy versus a layout change.

Never solve overflow by deleting a qualification, changing the action, using an unnatural abbreviation, shrinking text below accessibility requirements, clipping, or relying on an unexplained ellipsis. Do not treat source character count as a universal target: rendered width varies by glyph, font, viewport, and component.

For each representative page or component, test the target locale at supported breakpoints and in realistic states, including longest labels, validation errors, plural branches, user-generated names, zoom, and increased text spacing when accessibility requirements apply. If rendering is unavailable, mark visual fit as unverified and provide a concrete test list.

## Roll out

Validate fallback behavior, locale switching, deep links, canonical/hreflang metadata, responsive layouts, truncation, text expansion, plural branches, form submission, and persistence. Verify that fallback never introduces a different regional variety into a supposedly strict locale. Flag content still owned outside the repository rather than silently omitting it.

For multilingual SEO, ensure every localized page declares itself and reciprocal alternates with fully qualified URLs. Use one project-approved implementation surface—HTML, HTTP headers, or sitemap—unless the architecture intentionally needs more. Consider `x-default` for unmatched users. Do not rely on automatic redirects or IP geolocation as the only way to reach a locale.
