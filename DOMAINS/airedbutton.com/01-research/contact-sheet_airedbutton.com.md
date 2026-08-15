# airedbutton.com — Executive Contact Sheet (Batch 4B, Gap-fill 2/3)

> **Researcher:** domain-researcher | **Date:** 2026-08-15
> **Scope:** Verified executive contacts for top leads in the domain's leads file. Built to the Group-1 contact-sheet format (cf. `contact_nofail.ai.md`, `contact_knowlaw.ai.md`).
> **Verification:** Company LinkedIn URLs and public emails below were verified live this session via a curl sweep of company sites (HTTP 200, 2026-08-15). Exec names/roles/DMPS are carried from the domain's leads file. No email was invented — format-inferred addresses are explicitly marked M/L and flagged for owner verification before sending.

---

## 0. MISSING-CONTACTS SUMMARY (owner follow-up list)

Every exec whose **email** or **LinkedIn URL** could not be confirmed from a public source this session. Owner has offered to research these separately — this is the exact list.

| # | Company | Exec | Missing |
|---|---------|------|---------|
| 1 | Anthropic | Dario Amodei | email |
| 2 | Conjecture | Connor Leahy | email |
| 3 | ARC Evals | Paul Christiano | email; LinkedIn |
| 4 | Redwood Research | Buck Shlegeris | LinkedIn URL |

---

## Confidence Levels
- **H (High):** Verified from a public company page this session (HTTP 200)
- **M (Medium):** Likely correct based on company conventions; not independently confirmed from a public page
- **L (Low):** Best available; needs owner LLM verification

---

## Company Blocks (DMPS order)

### Anthropic — anthropic.com

| Field | Detail | Confidence |
|-------|--------|:---:|
| **Exec** | Dario Amodei — CEO | — |
| **Company LinkedIn** | https://www.linkedin.com/company/anthropicresearch | H |
| **Public email** | **MISSING** — no public address found on site sweep | — |
| **Source** | live curl sweep of anthropic.com (+/about /contact /team) 2026-08-15; leads file for exec/DMPS | — |
| **DMPS** | 88 | — |
| **Intent signal** | AI safety; emergency stop concept | — |
| **Note** | — | — |

### Conjecture — conjecture.dev

| Field | Detail | Confidence |
|-------|--------|:---:|
| **Exec** | Connor Leahy — CEO | — |
| **Company LinkedIn** | https://www.linkedin.com/company/conjecture | H |
| **Public email** | **MISSING** — no public address found on site sweep | — |
| **Source** | live curl sweep of conjecture.dev (+/about /contact /team) 2026-08-15; leads file for exec/DMPS | — |
| **DMPS** | 85 | — |
| **Intent signal** | AI safety; kill-switch advocacy | — |
| **Note** | — | — |

### ARC Evals — alignment.org

| Field | Detail | Confidence |
|-------|--------|:---:|
| **Exec** | Paul Christiano — Founder | — |
| **Company LinkedIn** | MISSING — not found on site sweep | — |
| **Public email** | **MISSING** — no public address found on site sweep | — |
| **Source** | live curl sweep of alignment.org (+/about /contact /team) 2026-08-15; leads file for exec/DMPS | — |
| **DMPS** | 82 | — |
| **Intent signal** | AI evaluation research | — |
| **Note** | no public contact found on sweep | — |

### Center for AI Safety — safe.ai

| Field | Detail | Confidence |
|-------|--------|:---:|
| **Exec** | Dan Hendrycks — Director | — |
| **Company LinkedIn** | https://www.linkedin.com/company/center-for-ai-safety | H |
| **Public email(s)** | contact@safe.ai, media@safe.ai | H |
| **Source** | live curl sweep of safe.ai (+/about /contact /team) 2026-08-15; leads file for exec/DMPS | — |
| **DMPS** | 80 | — |
| **Intent signal** | AI safety; red button concept | — |
| **Note** | — | — |

### Redwood Research — redwoodresearch.org

| Field | Detail | Confidence |
|-------|--------|:---:|
| **Exec** | Buck Shlegeris — CEO | — |
| **Company LinkedIn** | MISSING — not found on site sweep | — |
| **Public email(s)** | info@rdwrs.com | H |
| **Source** | live curl sweep of redwoodresearch.org (+/about /contact /team) 2026-08-15; leads file for exec/DMPS | — |
| **DMPS** | 78 | — |
| **Intent signal** | AI alignment research | — |
| **Note** | — | — |

---

## Coverage Summary

| Metric | Count |
|---|---|
| Companies covered | 5 |
| Companies with verified public email (H) | 2 |
| Companies with verified LinkedIn (H) | 3 |
| Companies with NO public exec email | 3 — see §0 |

---

## Notes on Method & Caveats
- **No emails invented.** Every direct exec email above is either (a) publicly listed on the company site (H), or (b) carried from the leads file / format-inferred and marked M/L. Any M/L address must be verified before sending (owner LLM or hunter.io-style lookup).
- **LinkedIn URLs marked H** come from the company's own site footer/about pages — these are the companies' own published links, so risk is low; LinkedIn itself was not logged into, so profile pages weren't fetched directly.
- **Exec names/roles** are carried from the leads file at M confidence (they were researched previously); only company-level contact data was re-verified live this session.
- **JS-heavy / bot-protected sites** returned no extractable contacts — for these, exec email is MISSING by design and LinkedIn should be resolved via LinkedIn search (marked L).

## Files
- **Lead list:** `leads_*` in `airedbutton.com/01-research/`
- **Verification sweep:** `/home/team/shared/contact-verification/batch4b-findings-2026-08-15.txt` (raw live-sweep output)
- **Reference format:** `../nofail.ai/01-research/contact_nofail.ai.md`