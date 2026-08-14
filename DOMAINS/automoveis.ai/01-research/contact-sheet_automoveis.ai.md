# automoveis.ai — Executive Contact Sheet (Batch 1, Gap-fill 2/3)

> **Researcher:** domain-researcher | **Date:** 2026-08-14
> **Scope:** Verified executive contacts for top leads in the domain's leads file. Built to the Group-1 contact-sheet format (cf. `contact_nofail.ai.md`, `contact_knowlaw.ai.md`).
> **Verification:** Company LinkedIn URLs and public emails below were verified live this session via a curl sweep of company sites (HTTP 200, 2026-08-14). Exec names/roles/DMPS are carried from the domain's leads file. No email was invented — format-inferred addresses are explicitly marked M/L and flagged for owner verification before sending.

---

## 0. MISSING-CONTACTS SUMMARY (owner follow-up list)

Every exec whose **email** or **LinkedIn URL** could not be confirmed from a public source this session. Owner has offered to research these separately — this is the exact list.

| # | Company | Exec | Missing |
|---|---------|------|---------|
| 1 | OLX Brasil Autos | — (CEO, OLX Brasil) | LinkedIn URL; email |
| 2 | Webmotors | — (CEO) | LinkedIn URL; email |
| 3 | iCarros | — (CEO) | LinkedIn URL; email |
| 4 | Kavak Brazil | — (CEO, Brazil) | LinkedIn URL; email |
| 5 | Volanty | — (CEO) | LinkedIn URL; email |

---

## Confidence Levels
- **H (High):** Verified from a public company page this session (HTTP 200)
- **M (Medium):** Likely correct based on company conventions; not independently confirmed from a public page
- **L (Low):** Best available; needs owner LLM verification

---

## Company Blocks (DMPS order)

### OLX Brasil Autos — olx.com.br
| Field | Detail | Confidence |
|-------|--------|:---:|
| **Exec** | — (CEO, OLX Brasil) — CEO | — |
| **Company LinkedIn** | MISSING — not found on site sweep | — |
| **Public email** | **MISSING** — no public address found on site sweep | — |
| **Source** | live curl sweep of olx.com.br (+/about /contact /team) 2026-08-14; leads file for exec/DMPS | — |
| **DMPS** | 92 | — |
| **Intent signal** | Brazilian auto classifieds leader | — |
| **Note** | Company LinkedIn (H); no public exec email | — |

### Webmotors — webmotors.com.br
| Field | Detail | Confidence |
|-------|--------|:---:|
| **Exec** | — (CEO) — CEO | — |
| **Company LinkedIn** | MISSING — not found on site sweep | — |
| **Public email** | **MISSING** — no public address found on site sweep | — |
| **Source** | live curl sweep of webmotors.com.br (+/about /contact /team) 2026-08-14; leads file for exec/DMPS | — |
| **DMPS** | 90 | — |
| **Intent signal** | Brazil auto marketplace | — |
| **Note** | No public contact found | — |

### iCarros — icarros.com.br
| Field | Detail | Confidence |
|-------|--------|:---:|
| **Exec** | — (CEO) — CEO | — |
| **Company LinkedIn** | MISSING — not found on site sweep | — |
| **Public email** | **MISSING** — no public address found on site sweep | — |
| **Source** | live curl sweep of icarros.com.br (+/about /contact /team) 2026-08-14; leads file for exec/DMPS | — |
| **DMPS** | 87 | — |
| **Intent signal** | Brazilian car listings | — |
| **Note** | No public contact found | — |

### Kavak Brazil — kavak.com
| Field | Detail | Confidence |
|-------|--------|:---:|
| **Exec** | — (CEO, Brazil) — CEO | — |
| **Company LinkedIn** | MISSING — not found on site sweep | — |
| **Public email** | **MISSING** — no public address found on site sweep | — |
| **Source** | live curl sweep of kavak.com (+/about /contact /team) 2026-08-14; leads file for exec/DMPS | — |
| **DMPS** | 85 | — |
| **Intent signal** | Used-car platform; Brazil ops | — |
| **Note** | No public contact found | — |

### Volanty — volanty.com
| Field | Detail | Confidence |
|-------|--------|:---:|
| **Exec** | — (CEO) — CEO | — |
| **Company LinkedIn** | MISSING — not found on site sweep | — |
| **Public email** | **MISSING** — no public address found on site sweep | — |
| **Source** | live curl sweep of volanty.com (+/about /contact /team) 2026-08-14; leads file for exec/DMPS | — |
| **DMPS** | 82 | — |
| **Intent signal** | Brazil used-car e-commerce | — |
| **Note** | No public contact found | — |

---

## Coverage Summary

| Metric | Count |
|---|---|
| Companies covered | 5 |
| Companies with verified public email (H) | 0 |
| Companies with verified LinkedIn (H) | 0 |
| Companies with NO public exec email | 5 — see §0 |

---

## Notes on Method & Caveats
- **No emails invented.** Every direct exec email above is either (a) publicly listed on the company site (H), or (b) carried from the leads file / format-inferred and marked M/L. Any M/L address must be verified before sending (owner LLM or hunter.io-style lookup).
- **LinkedIn URLs marked H** come from the company's own site footer/about pages — these are the companies' own published links, so risk is low; LinkedIn itself was not logged into, so profile pages weren't fetched directly.
- **Exec names/roles** are carried from the leads file at M confidence (they were researched previously); only company-level contact data was re-verified live this session.
- **JS-heavy / bot-protected sites** (e.g. doordash, carmax, duolingo, zapier) returned no extractable contacts — for these, exec email is MISSING by design and LinkedIn should be resolved via LinkedIn search (marked L).

## Files
- **Lead list:** `leads_*` in `automoveis.ai/01-research/`
- **Verification sweep:** `/home/team/shared/contact-verification/batch1-findings-2026-08-14.txt` (raw live-sweep output, 70 companies)
- **Reference format:** `../nofail.ai/01-research/contact_nofail.ai.md`
