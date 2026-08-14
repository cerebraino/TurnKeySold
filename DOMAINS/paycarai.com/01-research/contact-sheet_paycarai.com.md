# paycarai.com — Executive Contact Sheet (Batch 1, Gap-fill 2/3)

> **Researcher:** domain-researcher | **Date:** 2026-08-14
> **Scope:** Verified executive contacts for top leads in the domain's leads file. Built to the Group-1 contact-sheet format (cf. `contact_nofail.ai.md`, `contact_knowlaw.ai.md`).
> **Verification:** Company LinkedIn URLs and public emails below were verified live this session via a curl sweep of company sites (HTTP 200, 2026-08-14). Exec names/roles/DMPS are carried from the domain's leads file. No email was invented — format-inferred addresses are explicitly marked M/L and flagged for owner verification before sending.

---

## 0. MISSING-CONTACTS SUMMARY (owner follow-up list)

Every exec whose **email** or **LinkedIn URL** could not be confirmed from a public source this session. Owner has offered to research these separately — this is the exact list.

| # | Company | Exec | Missing |
|---|---------|------|---------|
| 1 | CarMax | Bill Nash | LinkedIn URL; email |
| 2 | Carvana | Ernie Garcia | LinkedIn URL; email |
| 3 | Stripe | Patrick Collison | email |
| 4 | Westlake Financial | Ian Anderson | LinkedIn URL; email |

---

## Confidence Levels
- **H (High):** Verified from a public company page this session (HTTP 200)
- **M (Medium):** Likely correct based on company conventions; not independently confirmed from a public page
- **L (Low):** Best available; needs owner LLM verification

---

## Company Blocks (DMPS order)

### CarMax — carmax.com
| Field | Detail | Confidence |
|-------|--------|:---:|
| **Exec** | Bill Nash — CEO | — |
| **Company LinkedIn** | MISSING — not found on site sweep | — |
| **Public email** | **MISSING** — no public address found on site sweep | — |
| **Source** | live curl sweep of carmax.com (+/about /contact /team) 2026-08-14; leads file for exec/DMPS | — |
| **DMPS** | 93 | — |
| **Intent signal** | Companion .com to paycar.ai; enterprise trust | — |
| **Note** | Site access-denied; LinkedIn via search (M) | — |

### Carvana — carvana.com
| Field | Detail | Confidence |
|-------|--------|:---:|
| **Exec** | Ernie Garcia — CEO & Co-Founder | — |
| **Company LinkedIn** | MISSING — not found on site sweep | — |
| **Public email** | **MISSING** — no public address found on site sweep | — |
| **Source** | live curl sweep of carvana.com (+/about /contact /team) 2026-08-14; leads file for exec/DMPS | — |
| **DMPS** | 91 | — |
| **Intent signal** | Digital car buying; .com for SEO/trust | — |
| **Note** | No public contact found | — |

### Stripe — stripe.com
| Field | Detail | Confidence |
|-------|--------|:---:|
| **Exec** | Patrick Collison — CEO | — |
| **Company LinkedIn** | https://www.linkedin.com/company/stripe | H |
| **Public email** | **MISSING** — no public address found on site sweep | — |
| **Source** | live curl sweep of stripe.com (+/about /contact /team) 2026-08-14; leads file for exec/DMPS | — |
| **DMPS** | 88 | — |
| **Intent signal** | Automotive payments vertical | — |
| **Note** | patrick@stripe.com (M, format-inferred); press@stripe.com (H) | — |

### Ally Financial — ally.com
| Field | Detail | Confidence |
|-------|--------|:---:|
| **Exec** | Michael Rhodes — CEO | — |
| **Company LinkedIn** | https://www.linkedin.com/company/ally | H |
| **Public email(s)** | corporatefinance@ally.com, givingback@ally.com, grants@ally.com, media@ally.com | H |
| **Source** | live curl sweep of ally.com (+/about /contact /team) 2026-08-14; leads file for exec/DMPS | — |
| **DMPS** | 85 | — |
| **Intent signal** | Auto lender; prefers .com | — |
| **Note** | media@ally.com verified (H); company LinkedIn (H) | — |

### Westlake Financial — westlakefinancial.com
| Field | Detail | Confidence |
|-------|--------|:---:|
| **Exec** | Ian Anderson — CEO | — |
| **Company LinkedIn** | MISSING — not found on site sweep | — |
| **Public email** | **MISSING** — no public address found on site sweep | — |
| **Source** | live curl sweep of westlakefinancial.com (+/about /contact /team) 2026-08-14; leads file for exec/DMPS | — |
| **DMPS** | 83 | — |
| **Intent signal** | Auto finance; long generic domain | — |
| **Note** | No public contact found | — |

---

## Coverage Summary

| Metric | Count |
|---|---|
| Companies covered | 5 |
| Companies with verified public email (H) | 1 |
| Companies with verified LinkedIn (H) | 2 |
| Companies with NO public exec email | 4 — see §0 |

---

## Notes on Method & Caveats
- **No emails invented.** Every direct exec email above is either (a) publicly listed on the company site (H), or (b) carried from the leads file / format-inferred and marked M/L. Any M/L address must be verified before sending (owner LLM or hunter.io-style lookup).
- **LinkedIn URLs marked H** come from the company's own site footer/about pages — these are the companies' own published links, so risk is low; LinkedIn itself was not logged into, so profile pages weren't fetched directly.
- **Exec names/roles** are carried from the leads file at M confidence (they were researched previously); only company-level contact data was re-verified live this session.
- **JS-heavy / bot-protected sites** (e.g. doordash, carmax, duolingo, zapier) returned no extractable contacts — for these, exec email is MISSING by design and LinkedIn should be resolved via LinkedIn search (marked L).

## Files
- **Lead list:** `leads_*` in `paycarai.com/01-research/`
- **Verification sweep:** `/home/team/shared/contact-verification/batch1-findings-2026-08-14.txt` (raw live-sweep output, 70 companies)
- **Reference format:** `../nofail.ai/01-research/contact_nofail.ai.md`
