# Instant mini-proof results (2026-09-10)

Model: ChatGPT Instant. Fresh chat per condition. Raw JSON replies in this folder.

| Case | Gold | No skill | With skill | Author review |
|---|---|---|---|---|
| ikrame-19 | change (settle/install wording; avoid *aterrizar*) | `pass` — accepted *aterrizar* | `change` → `Guía para instalarse en Málaga: padrón, NIE, Seguridad Social.` | Skill recovered the contextual calque; baseline missed it. |
| ikrame-08 | ask (house style on EN tech terms) | `pass` — kept prompts/skills/routing in EN | `change` → localized *routing* → *enrutamiento*; still no question | Skill was stricter but did not match gold `ask`. Include as imperfect / non-gold outcome. |
| mtt-05 | change → *Arriba* | `change` → *Arriba* | not re-run (baseline already matched gold) | Non-improvement / already-correct baseline. |

No corpus-wide improvement percentage is claimed.
