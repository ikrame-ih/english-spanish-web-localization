# English–Spanish Web Localization

[English](#english) · [Español](#español)

## English

A reusable agent skill for context-aware, bidirectional localization of websites and digital products across four deliberately separate locales:

| Locale | Target variety |
|---|---|
| `en-GB` | British English |
| `en-US` | US English |
| `es-ES` | Spanish for Spain |
| `es-419` | Broad Latin American Spanish |

This is not a word-replacement prompt. It treats copy as part of a product journey and evaluates meaning, audience, market, interface function, terminology, accessibility, SEO, layout constraints, and technical integrity before selecting a target formulation.

It also applies that standard outside a webpage: portfolios, CVs, Markdown, documentation, emails, forms, CMS exports, and locale catalogues. The format changes the checks, not the required contextual accuracy.

For example, **“Checklist for landing in Málaga”** may describe relocation rather than a plane landing. The skill first resolves that intent and can produce **“Lista para instalarte en Málaga”** or another context-appropriate version instead of the literal **“aterrizar”**.

### Two starting points

- **Create a missing language version.** Supply the original website, CV, Markdown file, or other content and the exact target locale. The agent creates complete localized copy using the product context; no existing target translation is needed.
- **Review or improve an existing localization.** Supply both versions. The agent checks meaning, naturalness, terminology, locale consistency and applicable format constraints. An audit returns findings and proposed wording; a request to fix or improve applies the authorized changes while retaining defensible copy.

Both workflows support English → Spanish and Spanish → English. If a suspected contextual calque changes meaning, it must be reported as an accuracy or fluency defect with a proposed correction. If the evidence cannot settle the reading, the agent must ask before dismissing it as style. Repository updates do not automatically update a previously installed copy of the skill or a frozen benchmark ZIP.

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

Install it with the Skills CLI in any supported agent environment:

```bash
npx skills add ikrame-ih/english-spanish-web-localization
```

Alternatively, clone the repository into the skills directory used by your agent. The folder name must match the skill name:

```text
english-spanish-web-localization/
```

The same core package works with [Claude Code](https://www.skills.sh/agent/claude-code), [Cursor](https://www.skills.sh/agent/cursor), [Codex](https://www.skills.sh/agent/codex), and [GitHub Copilot](https://www.skills.sh/agent/github-copilot), as well as other agents supported by the Skills CLI. `SKILL.md`, the references, and the deterministic checks are agent-neutral. [`agents/openai.yaml`](agents/openai.yaml) is optional Codex-facing interface metadata; agents that do not use it can ignore it.

When an agent supports explicit skill invocation, use `$english-spanish-web-localization`; otherwise invoke it through that agent’s usual skills workflow.

Example request for agents with explicit invocation:

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

### Benchmark

### Evidence dashboard

| Corpus | Sources | Locale routes | Cases | Result |
|---|---|---|---:|---|
| Portfolio regression | `ikrame.dev` | EN → `es-ES` | 30 | Not run |
| External bidirectional pack | At least 3 independent public products | `es-ES` → `en-GB`/`en-US`; `en-GB`/`en-US` → `es-419` | 30 minimum | Collecting sources |

| Evaluation | Baseline | With skill | Improvement |
|---|---:|---:|---:|
| Portfolio regression | — | — | — |
| External bidirectional pack | — | — | — |

The portfolio corpus is a public, 30-case real-world regression corpus with a blinded human-scoring protocol. Every pair has a public URL, retrieval date, and page locator. It tests contextual interpretation, voice, technical terminology, required clarification, and restraint when the existing target is already defensible. It is evidence for a specific site—not a universal or bidirectional quality claim. The external pack takes priority and has strict admission rules before publication. See [`benchmarks/`](benchmarks/) and [`benchmarks/external/`](benchmarks/external/).

### Visual paired evidence

The README will show a small set of real `no skill` versus `with skill` case studies only after controlled paired runs exist. Each card will link to its raw outputs and blinded human review; UI screenshots are added only when the same real component has been rendered at the same viewport. See [`benchmarks/showcase.md`](benchmarks/showcase.md).

## Español

Una skill reutilizable para agentes que localiza de forma contextual y bidireccional sitios web y productos digitales entre cuatro locales deliberadamente separados:

| Locale | Variante de destino |
|---|---|
| `en-GB` | Inglés británico |
| `en-US` | Inglés estadounidense |
| `es-ES` | Español de España |
| `es-419` | Español latinoamericano general |

No es un prompt de sustitución de palabras. Trata cada texto como parte de la experiencia del producto y valora significado, público, mercado, función de la interfaz, terminología, accesibilidad, SEO, restricciones de espacio e integridad técnica antes de elegir la formulación final.

También aplica este estándar fuera de una página web: portfolios, CV, Markdown, documentación, correos, formularios, exportaciones de CMS y catálogos de locales. Cambia la comprobación específica del formato, no el requisito de exactitud contextual.

Por ejemplo, **“Checklist for landing in Málaga”** puede hablar de una relocalización, no del aterrizaje de un avión. La skill resuelve primero esa intención y puede proponer **“Lista para instalarte en Málaga”** en vez del calco **“aterrizar”**.

### Dos puntos de partida

- **Crear la versión en el idioma que falta.** Proporciona la web, el CV, el archivo Markdown u otro contenido original y el locale exacto de destino. El agente crea el texto localizado completo usando el contexto del producto; no necesita una traducción previa.
- **Revisar o mejorar una localización existente.** Proporciona ambas versiones. El agente comprueba significado, naturalidad, terminología, coherencia regional y las restricciones del formato. Una auditoría entrega hallazgos y propuestas de redacción; una petición de corregir o mejorar aplica los cambios autorizados y conserva el texto ya defendible.

Ambos flujos funcionan del inglés al español y del español al inglés. Si un calco contextual cambia el significado, debe señalarse como defecto de exactitud o fluidez y acompañarse de una corrección propuesta. Si las evidencias no permiten resolverlo, el agente debe preguntar antes de descartarlo como estilo. Actualizar el repositorio no actualiza automáticamente una copia instalada anteriormente ni un ZIP de benchmark ya preparado.

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

Instálala con la CLI de Skills en cualquier entorno de agente compatible:

```bash
npx skills add ikrame-ih/english-spanish-web-localization
```

También puedes clonar el repositorio en el directorio de skills de tu agente. El nombre de la carpeta debe coincidir con el de la skill:

```text
english-spanish-web-localization/
```

El mismo paquete base funciona con [Claude Code](https://www.skills.sh/agent/claude-code), [Cursor](https://www.skills.sh/agent/cursor), [Codex](https://www.skills.sh/agent/codex) y [GitHub Copilot](https://www.skills.sh/agent/github-copilot), además de otros agentes compatibles con la CLI de Skills. `SKILL.md`, las referencias y las comprobaciones deterministas no dependen de un agente concreto. [`agents/openai.yaml`](agents/openai.yaml) contiene metadatos opcionales de interfaz para Codex; los agentes que no lo empleen pueden ignorarlo.

Cuando un agente admita invocación explícita de skills, usa `$english-spanish-web-localization`; en los demás casos, invócala desde el flujo habitual de skills de ese agente.

Ejemplo para agentes con invocación explícita:

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

### Benchmark

### Panel de evidencia

| Corpus | Fuentes | Rutas de locales | Casos | Resultado |
|---|---|---|---:|---|
| Regresión del portfolio | `ikrame.dev` | EN → `es-ES` | 30 | Sin ejecutar |
| Pack externo bidireccional | Al menos 3 productos públicos independientes | `es-ES` → `en-GB`/`en-US`; `en-GB`/`en-US` → `es-419` | 30 como mínimo | Recopilando fuentes |

| Evaluación | Base | Con la skill | Mejora |
|---|---:|---:|---:|
| Regresión del portfolio | — | — | — |
| Pack externo bidireccional | — | — | — |

El corpus del portfolio es una regresión pública de 30 casos reales con evaluación humana a ciegas. Cada par tiene URL pública, fecha de consulta y localizador de página. Evalúa interpretación contextual, voz, terminología técnica, aclaraciones obligatorias y la capacidad de no modificar un texto de destino ya defendible. Es evidencia de un sitio concreto, no una afirmación universal ni bidireccional. El pack externo tiene prioridad y solo se publicará cuando cumpla reglas estrictas de admisión. Consulta [`benchmarks/`](benchmarks/) y [`benchmarks/external/`](benchmarks/external/).

### Evidencia visual emparejada

El README mostrará unos pocos casos reales de `sin skill` frente a `con skill` solo después de contar con ejecuciones controladas y emparejadas. Cada ficha enlazará los outputs brutos y la revisión humana a ciegas; las capturas de interfaz solo se añadirán si el mismo componente real se ha renderizado en el mismo viewport. Consulta [`benchmarks/showcase.md`](benchmarks/showcase.md).

## License

MIT © 2026 ikrame-ih. See [`LICENSE`](LICENSE).
