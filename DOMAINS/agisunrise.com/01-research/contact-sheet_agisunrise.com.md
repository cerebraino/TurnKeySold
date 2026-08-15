# agisunrise.com — Executive Contact Sheet (Batch 5B, Gap-fill 2/3)

> **Researcher:** domain-researcher | **Date:** 2026-08-15
> **Scope:** Verified executive contacts for top leads in the domain's leads file. Built to the Group-1 contact-sheet format (cf. `contact_nofail.ai.md`, `contact_knowlaw.ai.md`).
> **Verification:** Company LinkedIn URLs and public emails below were verified live this session via a curl sweep of company sites (HTTP 200, 2026-08-15). Exec names/roles/DMPS are carried from the domain's leads file. No email was invented — format-inferred addresses are explicitly marked M/L and flagged for owner verification before sending.

---

## 0. MISSING-CONTACTS SUMMARY (owner follow-up list)

Every exec whose **email** or **LinkedIn URL** could not be confirmed from a public source this session. Owner has offered to research these separately — this is the exact list.

| # | Company | Exec | Missing |
|---|---------|------|---------|
| 1 | OpenAI | Sam Altman | email; LinkedIn |
| 2 | Anthropic | Dario Amodei | email |
| 3 | DeepMind (Google) | Demis Hassabis | email |
| 4 | Safe Superintelligence Inc. | Ilya Sutskever | LinkedIn URL |
| 5 | Conjecture | Connor Leahy | email |
| 6 | Alignment Research Center | Paul Christiano | email; LinkedIn |

---

## Confidence Levels
- **H (High):** Verified from a public company page this session (HTTP 200)
- **M (Medium):** Likely correct based on company conventions; not independently confirmed from a public page
- **L (Low):** Best available; needs owner LLM verification

---

## Company Blocks (DMPS order)

### OpenAI — openai.com

| Field | Detail | Confidence |
|-------|--------|:---:|
| **Exec** | Sam Altman — CEO | — |
| **Company LinkedIn** | MISSING — not found on site sweep | — |
| **Public email** | **MISSING** — no public address found on site sweep | — |
| **Source** | live curl sweep of openai.com (+/about /contact /team) 2026-08-15; leads file for exec/DMPS | — |
| **DMPS** | 70 | — |
| **Intent signal** | AGI development; 'AGI sunrise' concept | — |
| **Note** | no public contact found on sweep | — |

### Anthropic — anthropic.com

| Field | Detail | Confidence |
|-------|--------|:---:|
| **Exec** | Dario Amodei — CEO | — |
| **Company LinkedIn** | https://www.linkedin.com/company/anthropicresearch | H |
| **Public email** | **MISSING** — no public address found on site sweep | — |
| **Source** | live curl sweep of anthropic.com (+/about /contact /team) 2026-08-15; leads file for exec/DMPS | — |
| **DMPS** | 68 | — |
| **Intent signal** | AI safety; AGI timeline | — |
| **Note** | — | — |

### DeepMind (Google) — deepmind.com

| Field | Detail | Confidence |
|-------|--------|:---:|
| **Exec** | Demis Hassabis — CEO | — |
| **Company LinkedIn** | https://www.linkedin.com/company/googledeepmind | H |
| **Public email** | **MISSING** — no public address found on site sweep | — |
| **Source** | live curl sweep of deepmind.com (+/about /contact /team) 2026-08-15; leads file for exec/DMPS | — |
| **DMPS** | 65 | — |
| **Intent signal** | AGI research | — |
| **Note** | — | — |

### Safe Superintelligence Inc. — ssi.inc

| Field | Detail | Confidence |
|-------|--------|:---:|
| **Exec** | Ilya Sutskever — CEO | — |
| **Company LinkedIn** | MISSING — not found on site sweep | — |
| **Public email(s)** | comms@ssi.inc | H |
| **Source** | live curl sweep of ssi.inc (+/about /contact /team) 2026-08-15; leads file for exec/DMPS | — |
| **DMPS** | 62 | — |
| **Intent signal** | Safe AGI company | — |
| **Note** | Public email(s): comms@ssi.inc (H) — may be shared inbox, verify exec reach | — |

### Conjecture — conjecture.dev

| Field | Detail | Confidence |
|-------|--------|:---:|
| **Exec** | Connor Leahy — CEO | — |
| **Company LinkedIn** | https://www.linkedin.com/company/conjecture | H |
| **Public email** | **MISSING** — no public address found on site sweep | — |
| **Source** | live curl sweep of conjecture.dev (+/about /contact /team) 2026-08-15; leads file for exec/DMPS | — |
| **DMPS** | 58 | — |
| **Intent signal** | AI safety | — |
| **Note** | — | — |

### Alignment Research Center — alignment.org

| Field | Detail | Confidence |
|-------|--------|:---:|
| **Exec** | Paul Christiano — Founder | — |
| **Company LinkedIn** | MISSING — not found on site sweep | — |
| **Public email** | **MISSING** — no public address found on site sweep | — |
| **Source** | live curl sweep of alignment.org (+/about /contact /team) 2026-08-15; leads file for exec/DMPS | — |
| **DMPS** | 55 | — |
| **Intent signal** | AI alignment | — |
| **Note** | no public contact found on sweep | — |

---

## Coverage Summary

| Metric | Count |
|---|---|
| Companies covered | 6 |
| Companies with verified public email (H) | 1 |
| Companies with verified LinkedIn (H) | 3 |
| Companies with NO public exec email | 5 — see §0 |

---

## Notes on Method & Caveats
- **No emails invented.** Every direct exec email above is either (a) publicly listed on the company site (H), or (b) carried from the leads file / format-inferred and marked M/L. Any M/L address must be verified before sending (owner LLM or hunter.io-style lookup).
- **LinkedIn URLs marked H** come from the company's own site footer/about pages — these are the companies' own published links, so risk is low; LinkedIn itself was not logged into, so profile pages weren't fetched directly.
- **Exec names/roles** are carried from the leads file at M confidence (they were researched previously); only company-level contact data was re-verified live this session.
- **JS-heavy / bot-protected sites** returned no extractable contacts — for these, exec email is MISSING by design and LinkedIn should be resolved via LinkedIn search (marked L).

## Files
- **Lead list:** `leads_*` in `agisunrise.com/01-research/`
- **Verification sweep:** `/home/team/shared/contact-verification/batch5-findings-2026-08-15.txt` (raw live-sweep output)
- **Reference format:** `../nofail.ai/01-research/contact_nofail.ai.md`