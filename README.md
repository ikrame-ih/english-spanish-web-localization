# English–Spanish Web Localization

[English](#english) · [Español](#español)

## English

A reusable Codex skill for context-aware, bidirectional localization of websites and digital products across four deliberately separate locales:

| Locale | Target variety |
|---|---|
| `en-GB` | British English |
| `en-US` | US English |
| `es-ES` | Spanish for Spain |
| `es-419` | Broad Latin American Spanish |

This is not a word-replacement prompt. It treats copy as part of a product journey and evaluates meaning, audience, market, interface function, terminology, accessibility, SEO, layout constraints, and technical integrity before selecting a target formulation.

For example, **“Checklist for landing in Málaga”** may describe relocation rather than a plane landing. The skill first resolves that intent and can produce **“Lista para instalarte en Málaga”** or another context-appropriate version instead of the literal **“aterrizar”**.

### What it does

- Localizes in either direction among the four supported locales.
- Keeps British and US English strictly separate.
- Keeps Spain and Latin American Spanish strictly separate.
- Handles ambiguous terms through page, component, domain, and user-journey context.
- Asks the user when meaningful preference choices remain after context and criteria have been exhausted.
- Treats available width and text expansion as localization constraints and requires rendered UI checks before claiming release readiness.
- Preserves placeholders, tags, links, ICU syntax, keys, identifiers, and other non-translatable structure.
- Covers UI copy, marketing pages, metadata, accessibility text, forms, errors, emails, CMS content, and locale catalogs.
- Preserves correct Unicode spelling and diacritics, including in CVs, while applying evidence-based ATS precautions.
- Includes a deterministic JSON catalog checker.

`es-419` is a standard macroregional locale for Latin America and the Caribbean; it does **not** imply that every country uses the same Spanish. When country-level differences matter, the skill asks for or uses a narrower locale such as `es-MX`, `es-AR`, or `es-CO`.

### Installation

Once published at the proposed repository address, install it with:

```bash
npx skills add ikrame-ih/english-spanish-web-localization
```

Alternatively, clone the repository into the skills directory used by your Codex environment. The folder name must match the skill name:

```text
english-spanish-web-localization/
```

Invoke it explicitly as:

```text
$english-spanish-web-localization
```

Example request:

```text
Use $english-spanish-web-localization to localize this product site from en-US to es-ES. Preserve the concise brand voice, audit responsive text fit, and ask me before resolving any material preference that the available context does not settle.
```

### Workflow

1. Establish the exact source and target locales, audience, voice, domain, content surfaces, and UI constraints.
2. Inspect page-level and journey-level context before translating ambiguous strings.
3. Build or follow a concept-based termbase.
4. Localize complete messages without mixing locale varieties.
5. Run structural, linguistic, locale, accessibility, SEO, and visual checks.
6. Report blockers, assumptions, decisions, changed files, and residual risk.

### UI length and visual QA

The skill does not force translations to mimic source character counts. It first seeks a concise, natural formulation without losing meaning; then it uses an approved shorter pattern or improves the component when authorized. If the trade-off is subjective or consequential, it asks the user.

Visual QA covers representative mobile and desktop breakpoints, navigation, buttons, tabs, cards, tables, forms, errors, dialogs, plural branches, long user data, zoom, and increased text spacing. Without rendered evidence, the result must be labelled visually unverified.

### Diacritics and ATS-safe CVs

Correct accents and `ñ` remain the default. Modern multilingual parsers support Spanish; documented parsing failures are often caused by image-based files or complex layout. For ATS-facing CVs, the skill prefers selectable text, conventional headings, a simple reading order, and tested extraction. It creates an ASCII compatibility variant only for a demonstrated system constraint and only after asking the user; canonical names and prose remain correctly accented.

### Catalog guard

```bash
python3 scripts/locale_guard.py source.json target.json
python3 scripts/locale_guard.py source.json target.json --warn-expansion 1.4
```

The checker detects missing or extra keys, structural/type drift, empty translations, placeholder/tag/link mismatches, brace and whitespace defects, likely mojibake, non-NFC Unicode, suspicious identical strings, and optionally large character-count expansion. It complements—not replaces—linguistic and rendered UI review.

### Scope and limitations

The skill supports localization, audits, terminology, strategy, and QA. It does not certify legal, medical, financial, or sworn translations, and it does not promise universal ATS compatibility. High-risk ambiguity is researched and escalated rather than guessed.

### Evidence base

The guidance prioritizes product sources of truth and uses primary references including RAE/ASALE, FundéuRAE, Unicode CLDR and UTS #35, W3C Internationalization and WCAG, Google Search Central, Greenhouse, and Textkernel. See [`references/research-and-evidence.md`](references/research-and-evidence.md).

## Español

Una skill reutilizable para Codex que localiza de forma contextual y bidireccional sitios web y productos digitales entre cuatro locales deliberadamente separados:

| Locale | Variante de destino |
|---|---|
| `en-GB` | Inglés británico |
| `en-US` | Inglés estadounidense |
| `es-ES` | Español de España |
| `es-419` | Español latinoamericano general |

No es un prompt de sustitución de palabras. Trata cada texto como parte de la experiencia del producto y valora significado, público, mercado, función de la interfaz, terminología, accesibilidad, SEO, restricciones de espacio e integridad técnica antes de elegir la formulación final.

Por ejemplo, **“Checklist for landing in Málaga”** puede hablar de una relocalización, no del aterrizaje de un avión. La skill resuelve primero esa intención y puede proponer **“Lista para instalarte en Málaga”** en vez del calco **“aterrizar”**.

### Qué hace

- Localiza en ambas direcciones entre los cuatro locales compatibles.
- Separa estrictamente el inglés británico del estadounidense.
- Separa estrictamente el español de España del latinoamericano.
- Resuelve términos ambiguos usando el contexto de la página, el componente, el dominio y el recorrido del usuario.
- Pregunta al usuario cuando persisten decisiones relevantes de preferencia después de aplicar todo el contexto y los criterios disponibles.
- Considera el ancho disponible y la expansión del texto como restricciones de localización y exige revisar la interfaz renderizada antes de declararla lista.
- Conserva placeholders, etiquetas, enlaces, sintaxis ICU, claves, identificadores y demás estructura no traducible.
- Cubre interfaz, marketing, metadatos, accesibilidad, formularios, errores, correos, CMS y catálogos de locales.
- Mantiene la ortografía Unicode y las tildes correctas, también en CV, con precauciones ATS basadas en evidencias.
- Incluye un comprobador determinista para catálogos JSON.

`es-419` es un locale macroregional estándar para Latinoamérica y el Caribe; **no** significa que todos los países empleen el mismo español. Cuando importan las diferencias nacionales, la skill solicita o utiliza un locale más preciso, como `es-MX`, `es-AR` o `es-CO`.

### Instalación

Cuando esté publicado en el repositorio propuesto, instálalo con:

```bash
npx skills add ikrame-ih/english-spanish-web-localization
```

También puedes clonar el repositorio en el directorio de skills de tu entorno Codex. El nombre de la carpeta debe coincidir con el de la skill:

```text
english-spanish-web-localization/
```

Invócala expresamente así:

```text
$english-spanish-web-localization
```

Ejemplo:

```text
Usa $english-spanish-web-localization para localizar este sitio de producto de en-US a es-ES. Conserva la voz concisa de la marca, revisa el encaje del texto en responsive y pregúntame antes de resolver cualquier preferencia relevante que el contexto disponible no determine.
```

### Flujo de trabajo

1. Determina los locales exactos de origen y destino, el público, la voz, el dominio, las superficies de contenido y las restricciones de interfaz.
2. Inspecciona el contexto de la página y del recorrido antes de traducir cadenas ambiguas.
3. Crea o aplica una base terminológica por conceptos.
4. Localiza mensajes completos sin mezclar variantes regionales.
5. Ejecuta comprobaciones estructurales, lingüísticas, regionales, de accesibilidad, SEO y visuales.
6. Informa de bloqueos, supuestos, decisiones, archivos modificados y riesgos pendientes.

### Longitud del texto y QA visual

La skill no obliga a que la traducción copie el número de caracteres del original. Primero busca una formulación natural y concisa sin perder significado; después recurre a un patrón corto aprobado o mejora el componente si tiene autorización. Si la compensación es subjetiva o relevante, pregunta al usuario.

El QA visual abarca anchos representativos de móvil y escritorio, navegación, botones, pestañas, tarjetas, tablas, formularios, errores, diálogos, plurales, datos largos de usuario, zoom y espaciado de texto aumentado. Sin una comprobación renderizada, el resultado debe marcarse como no verificado visualmente.

### Tildes y CV compatibles con ATS

Las tildes y la `ñ` correctas son la opción predeterminada. Los analizadores multilingües modernos admiten español; los fallos documentados suelen deberse a archivos basados en imágenes o a maquetaciones complejas. En un CV destinado a un ATS, la skill prioriza texto seleccionable, encabezados convencionales, un orden de lectura sencillo y la comprobación de la extracción. Solo crea una variante ASCII ante una limitación demostrada del sistema y después de consultar al usuario; los nombres y el texto canónico conservan su ortografía correcta.

### Comprobador de catálogos

```bash
python3 scripts/locale_guard.py source.json target.json
python3 scripts/locale_guard.py source.json target.json --warn-expansion 1.4
```

Detecta claves ausentes o adicionales, cambios de estructura o tipo, traducciones vacías, diferencias en placeholders, etiquetas o enlaces, problemas de llaves y espacios, posible mojibake, Unicode sin normalizar a NFC, cadenas sospechosamente idénticas y, opcionalmente, una expansión elevada del número de caracteres. Complementa —no sustituye— la revisión lingüística y visual.

### Alcance y límites

La skill sirve para localización, auditoría, terminología, estrategia y QA. No certifica traducciones juradas ni textos legales, médicos o financieros, y no promete compatibilidad universal con todos los ATS. Investiga y eleva las ambigüedades de alto riesgo en vez de adivinarlas.

### Fuentes

La guía prioriza las fuentes de verdad del producto y se apoya en referencias primarias como RAE/ASALE, FundéuRAE, Unicode CLDR y UTS #35, W3C Internationalization y WCAG, Google Search Central, Greenhouse y Textkernel. Consulta [`references/research-and-evidence.md`](references/research-and-evidence.md).

## License

MIT © 2026 ikrame-ih. See [`LICENSE`](LICENSE).
