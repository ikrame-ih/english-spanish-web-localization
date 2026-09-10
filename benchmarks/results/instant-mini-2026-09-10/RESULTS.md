# Instant mini-proof results (2026-09-10)

Model: ChatGPT Instant. Fresh chat per condition. Raw JSON replies in this folder.

| Case | Expected | No skill | With skill | Notes |
|---|---|---|---|---|
| ikrame-19 | change (settle/install wording; avoid *aterrizar*) | `pass` — accepted *aterrizar* | `change` → `Guía para instalarse en Málaga: padrón, NIE, Seguridad Social.` | Caught the aterrizar calque; without the skill it was missed. |
| ikrame-08 | ask (house style on EN tech terms) | `pass` — kept prompts/skills/routing in EN | `change` → localized *routing* → *enrutamiento*; still no question | Pushed harder on anglicisms but still did not ask about house style. |
| mtt-05 | change → *Arriba* | `change` → *Arriba* | not re-run (baseline already matched) | Baseline was already right; skill not re-run. |

I checked these myself. The full 30-case blind review is still ahead. This is not a score for the whole set.
