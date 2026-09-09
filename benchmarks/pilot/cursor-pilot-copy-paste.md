# Cursor pilot: copy-paste runs

This is the six-pair pilot defined in [operator-order.tsv](operator-order.tsv). It requires **12 fresh chats**: six baseline chats and six skill-assisted chats. Do not use the full benchmark repository as the workspace: it contains the expected decisions.

## Fixed settings

- Model: **Grok 4.6**
- Reasoning: **Medium**
- Mode: **Ask**
- Tools/web: **off**
- Answer format: JSON only; no prose before or after it.
- Use one fresh chat per run.
- Paste the relevant block below in that fresh chat, wait for the JSON reply, then save the reply under its run number.
- Do not reveal to the model that cases are paired. Do not open the public source URLs.

For a **baseline** run, use a clean workspace with no localization skill installed or selected.

For a **skill-assisted** run, use a clean workspace that contains only this repository's localization skill. Invoke that skill in the chat before pasting the block (for example via Cursor's skill selector). Do not attach the repository containing this benchmark.

## Send these 12 blocks, in this exact order

### 1 — run 02 — baseline

```text
Audit the observed target copy against the source copy and supplied UI context.

Return valid JSON only:
{"verdict":"pass|change|ask","revised_copy":null|string,"question":null|string,"rationale":"one concise sentence"}.

Use pass when the observed target is defensible. Use change only for a material localisation defect; then supply a revised_copy. Use ask only when the supplied context cannot settle a material decision; then supply one concise question. Preserve placeholders and markup exactly. Do not browse or use other context.

{"id":"box-03","product":"Box Annotations","category":"input","source_locale":"es-ES","source":"Escriba un comentario","observed_target":"Type a comment","target_locale":"en-US","locator":"Reply input placeholder (ba.popup.reply.field)","context":"Placeholder in a compact comment reply field."}
```

### 2 — run 03 — skill-assisted

```text
Audit the observed target copy against the source copy and supplied UI context.

Return valid JSON only:
{"verdict":"pass|change|ask","revised_copy":null|string,"question":null|string,"rationale":"one concise sentence"}.

Use pass when the observed target is defensible. Use change only for a material localisation defect; then supply a revised_copy. Use ask only when the supplied context cannot settle a material decision; then supply one concise question. Preserve placeholders and markup exactly. Do not browse or use other context.

{"id":"boxui-04","product":"Box UI Elements","category":"plural","source_locale":"es-ES","source":"Ver {repliesToLoadCount, plural, one {# respuesta} other {# respuestas}}","observed_target":"See {repliesToLoadCount, plural, one {# reply} other {# replies}}","target_locale":"en-US","locator":"UI message (be.activitySidebar.activityFeed.showReplies)","context":"Pluralised control. Preserve the ICU placeholder and plural branches."}
```

### 3 — run 05 — skill-assisted

```text
Audit the observed target copy against the source copy and supplied UI context.

Return valid JSON only:
{"verdict":"pass|change|ask","revised_copy":null|string,"question":null|string,"rationale":"one concise sentence"}.

Use pass when the observed target is defensible. Use change only for a material localisation defect; then supply a revised_copy. Use ask only when the supplied context cannot settle a material decision; then supply one concise question. Preserve placeholders and markup exactly. Do not browse or use other context.

{"id":"box-06","product":"Box Annotations","category":"instruction","source_locale":"en-GB","source":"Draw a box to comment","observed_target":"Dibuje un cuadro para comentar","target_locale":"es-419","locator":"Cursor-region instruction (ba.popups.popupCursor.regionPrompt)","context":"On-canvas instruction for drawing an annotation region."}
```

### 4 — run 06 — baseline

```text
Audit the observed target copy against the source copy and supplied UI context.

Return valid JSON only:
{"verdict":"pass|change|ask","revised_copy":null|string,"question":null|string,"rationale":"one concise sentence"}.

Use pass when the observed target is defensible. Use change only for a material localisation defect; then supply a revised_copy. Use ask only when the supplied context cannot settle a material decision; then supply one concise question. Preserve placeholders and markup exactly. Do not browse or use other context.

{"id":"mtt-01","product":"Mouse Tooltip Translator","category":"technical-ui","source_locale":"en-US","source":"LLM API Endpoint URL","observed_target":"LLM API Endpoint URL","target_locale":"es-419","locator":"Settings label (LLM_Api_Endpoint)","context":"Technical configuration label. Preserve LLM and API while localising the surrounding UI label."}
```

### 5 — run 09 — skill-assisted

```text
Audit the observed target copy against the source copy and supplied UI context.

Return valid JSON only:
{"verdict":"pass|change|ask","revised_copy":null|string,"question":null|string,"rationale":"one concise sentence"}.

Use pass when the observed target is defensible. Use change only for a material localisation defect; then supply a revised_copy. Use ask only when the supplied context cannot settle a material decision; then supply one concise question. Preserve placeholders and markup exactly. Do not browse or use other context.

{"id":"box-01","product":"Box Annotations","category":"ui","source_locale":"es-ES","source":"Cerrar","observed_target":"Close","target_locale":"en-GB","locator":"Annotation viewer close control (ba.annotationsClose)","context":"Compact UI button that closes the annotations experience."}
```

### 6 — run 11 — skill-assisted

```text
Audit the observed target copy against the source copy and supplied UI context.

Return valid JSON only:
{"verdict":"pass|change|ask","revised_copy":null|string,"question":null|string,"rationale":"one concise sentence"}.

Use pass when the observed target is defensible. Use change only for a material localisation defect; then supply a revised_copy. Use ask only when the supplied context cannot settle a material decision; then supply one concise question. Preserve placeholders and markup exactly. Do not browse or use other context.

{"id":"box-07","product":"Box Annotations","category":"restriction","source_locale":"en-US","source":"Comments restricted to single page","observed_target":"Los comentarios están restringidos a una sola página.","target_locale":"es-419","locator":"Highlight restriction message (ba.popups.popupHighlight.restrictedPrompt)","context":"Informational UI text explaining a one-page comment limitation."}
```

### 7 — run 13 — skill-assisted

```text
Audit the observed target copy against the source copy and supplied UI context.

Return valid JSON only:
{"verdict":"pass|change|ask","revised_copy":null|string,"question":null|string,"rationale":"one concise sentence"}.

Use pass when the observed target is defensible. Use change only for a material localisation defect; then supply a revised_copy. Use ask only when the supplied context cannot settle a material decision; then supply one concise question. Preserve placeholders and markup exactly. Do not browse or use other context.

{"id":"box-03","product":"Box Annotations","category":"input","source_locale":"es-ES","source":"Escriba un comentario","observed_target":"Type a comment","target_locale":"en-US","locator":"Reply input placeholder (ba.popup.reply.field)","context":"Placeholder in a compact comment reply field."}
```

### 8 — run 15 — baseline

```text
Audit the observed target copy against the source copy and supplied UI context.

Return valid JSON only:
{"verdict":"pass|change|ask","revised_copy":null|string,"question":null|string,"rationale":"one concise sentence"}.

Use pass when the observed target is defensible. Use change only for a material localisation defect; then supply a revised_copy. Use ask only when the supplied context cannot settle a material decision; then supply one concise question. Preserve placeholders and markup exactly. Do not browse or use other context.

{"id":"boxui-04","product":"Box UI Elements","category":"plural","source_locale":"es-ES","source":"Ver {repliesToLoadCount, plural, one {# respuesta} other {# respuestas}}","observed_target":"See {repliesToLoadCount, plural, one {# reply} other {# replies}}","target_locale":"en-US","locator":"UI message (be.activitySidebar.activityFeed.showReplies)","context":"Pluralised control. Preserve the ICU placeholder and plural branches."}
```

### 9 — run 16 — baseline

```text
Audit the observed target copy against the source copy and supplied UI context.

Return valid JSON only:
{"verdict":"pass|change|ask","revised_copy":null|string,"question":null|string,"rationale":"one concise sentence"}.

Use pass when the observed target is defensible. Use change only for a material localisation defect; then supply a revised_copy. Use ask only when the supplied context cannot settle a material decision; then supply one concise question. Preserve placeholders and markup exactly. Do not browse or use other context.

{"id":"box-06","product":"Box Annotations","category":"instruction","source_locale":"en-GB","source":"Draw a box to comment","observed_target":"Dibuje un cuadro para comentar","target_locale":"es-419","locator":"Cursor-region instruction (ba.popups.popupCursor.regionPrompt)","context":"On-canvas instruction for drawing an annotation region."}
```

### 10 — run 17 — skill-assisted

```text
Audit the observed target copy against the source copy and supplied UI context.

Return valid JSON only:
{"verdict":"pass|change|ask","revised_copy":null|string,"question":null|string,"rationale":"one concise sentence"}.

Use pass when the observed target is defensible. Use change only for a material localisation defect; then supply a revised_copy. Use ask only when the supplied context cannot settle a material decision; then supply one concise question. Preserve placeholders and markup exactly. Do not browse or use other context.

{"id":"mtt-01","product":"Mouse Tooltip Translator","category":"technical-ui","source_locale":"en-US","source":"LLM API Endpoint URL","observed_target":"LLM API Endpoint URL","target_locale":"es-419","locator":"Settings label (LLM_Api_Endpoint)","context":"Technical configuration label. Preserve LLM and API while localising the surrounding UI label."}
```

### 11 — run 20 — baseline

```text
Audit the observed target copy against the source copy and supplied UI context.

Return valid JSON only:
{"verdict":"pass|change|ask","revised_copy":null|string,"question":null|string,"rationale":"one concise sentence"}.

Use pass when the observed target is defensible. Use change only for a material localisation defect; then supply a revised_copy. Use ask only when the supplied context cannot settle a material decision; then supply one concise question. Preserve placeholders and markup exactly. Do not browse or use other context.

{"id":"box-01","product":"Box Annotations","category":"ui","source_locale":"es-ES","source":"Cerrar","observed_target":"Close","target_locale":"en-GB","locator":"Annotation viewer close control (ba.annotationsClose)","context":"Compact UI button that closes the annotations experience."}
```

### 12 — run 22 — baseline

```text
Audit the observed target copy against the source copy and supplied UI context.

Return valid JSON only:
{"verdict":"pass|change|ask","revised_copy":null|string,"question":null|string,"rationale":"one concise sentence"}.

Use pass when the observed target is defensible. Use change only for a material localisation defect; then supply a revised_copy. Use ask only when the supplied context cannot settle a material decision; then supply one concise question. Preserve placeholders and markup exactly. Do not browse or use other context.

{"id":"box-07","product":"Box Annotations","category":"restriction","source_locale":"en-US","source":"Comments restricted to single page","observed_target":"Los comentarios están restringidos a una sola página.","target_locale":"es-419","locator":"Highlight restriction message (ba.popups.popupHighlight.restrictedPrompt)","context":"Informational UI text explaining a one-page comment limitation."}
```

## Return results

Send the 12 raw JSON responses to the benchmark reviewer in this form:

```text
run 02
<raw JSON>

run 03
<raw JSON>

...through run 22
```

Do not add your own assessment of whether a response is good. The reviewer has the hidden reference set and will score it blind.
