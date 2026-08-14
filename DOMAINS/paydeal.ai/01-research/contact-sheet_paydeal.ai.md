# paydeal.ai — Executive Contact Sheet (Batch 1, Gap-fill 2/3)

> **Researcher:** domain-researcher | **Date:** 2026-08-14
> **Scope:** Verified executive contacts for top leads in the domain's leads file. Built to the Group-1 contact-sheet format (cf. `contact_nofail.ai.md`, `contact_knowlaw.ai.md`).
> **Verification:** Company LinkedIn URLs and public emails below were verified live this session via a curl sweep of company sites (HTTP 200, 2026-08-14). Exec names/roles/DMPS are carried from the domain's leads file. No email was invented — format-inferred addresses are explicitly marked M/L and flagged for owner verification before sending.

---

## 0. MISSING-CONTACTS SUMMARY (owner follow-up list)

Every exec whose **email** or **LinkedIn URL** could not be confirmed from a public source this session. Owner has offered to research these separately — this is the exact list.

| # | Company | Exec | Missing |
|---|---------|------|---------|
| 1 | Affirm | Max Levchin | email |
| 2 | Klarna | Sebastian Siemiatkowski | LinkedIn URL; email |
| 3 | Afterpay (Block) | Nick Molnar | LinkedIn URL; email |
| 4 | Groupon | Kedar Deshpande | email |
| 5 | Rakuten | Mickey Mikitani | email |
| 6 | Zip (Quadpay) | Larry Diamond | LinkedIn URL; email |
| 7 | Sezzle | Charlie Youakim | LinkedIn URL; email |

---

## Confidence Levels
- **H (High):** Verified from a public company page this session (HTTP 200)
- **M (Medium):** Likely correct based on company conventions; not independently confirmed from a public page
- **L (Low):** Best available; needs owner LLM verification

---

## Company Blocks (DMPS order)

### Affirm — affirm.com
| Field | Detail | Confidence |
|-------|--------|:---:|
| **Exec** | Max Levchin — CEO & Co-Founder | — |
| **Company LinkedIn** | https://www.linkedin.com/company/affirm | H |
| **Public email** | **MISSING** — no public address found on site sweep | — |
| **Source** | live curl sweep of affirm.com (+/about /contact /team) 2026-08-14; leads file for exec/DMPS | — |
| **DMPS** | 95 | — |
| **Intent signal** | BNPL leader; 'pay for a deal' | — |
| **Note** | Company LinkedIn (H); no public exec email | — |

### Klarna — klarna.com
| Field | Detail | Confidence |
|-------|--------|:---:|
| **Exec** | Sebastian Siemiatkowski — CEO | — |
| **Company LinkedIn** | MISSING — not found on site sweep | — |
| **Public email** | **MISSING** — no public address found on site sweep | — |
| **Source** | live curl sweep of klarna.com (+/about /contact /team) 2026-08-14; leads file for exec/DMPS | — |
| **DMPS** | 93 | — |
| **Intent signal** | BNPL + AI shopping/deals | — |
| **Note** | No public exec email | — |

### Afterpay (Block) — afterpay.com
| Field | Detail | Confidence |
|-------|--------|:---:|
| **Exec** | Nick Molnar — CEO & Co-Founder | — |
| **Company LinkedIn** | MISSING — not found on site sweep | — |
| **Public email** | **MISSING** — no public address found on site sweep | — |
| **Source** | live curl sweep of afterpay.com (+/about /contact /team) 2026-08-14; leads file for exec/DMPS | — |
| **DMPS** | 90 | — |
| **Intent signal** | BNPL pioneer; pay-in-4 | — |
| **Note** | No public contact found | — |

### Groupon — groupon.com
| Field | Detail | Confidence |
|-------|--------|:---:|
| **Exec** | Kedar Deshpande — CEO | — |
| **Company LinkedIn** | https://www.linkedin.com/company/groupon | H |
| **Public email** | **MISSING** — no public address found on site sweep | — |
| **Source** | live curl sweep of groupon.com (+/about /contact /team) 2026-08-14; leads file for exec/DMPS | — |
| **DMPS** | 85 | — |
| **Intent signal** | Deals marketplace; AI pivot potential | — |
| **Note** | Company LinkedIn (H); no public exec email | — |

### Rakuten — rakuten.com
| Field | Detail | Confidence |
|-------|--------|:---:|
| **Exec** | Mickey Mikitani — CEO | — |
| **Company LinkedIn** | https://www.linkedin.com/company/rakutenrewards | H |
| **Public email** | **MISSING** — no public address found on site sweep | — |
| **Source** | live curl sweep of rakuten.com (+/about /contact /team) 2026-08-14; leads file for exec/DMPS | — |
| **DMPS** | 83 | — |
| **Intent signal** | Cashback + deals; fintech | — |
| **Note** | Company LinkedIn rakutenrewards (H) | — |

### Zip (Quadpay) — zip.co
| Field | Detail | Confidence |
|-------|--------|:---:|
| **Exec** | Larry Diamond — CEO | — |
| **Company LinkedIn** | MISSING — not found on site sweep | — |
| **Public email** | **MISSING** — no public address found on site sweep | — |
| **Source** | live curl sweep of zip.co (+/about /contact /team) 2026-08-14; leads file for exec/DMPS | — |
| **DMPS** | 78 | — |
| **Intent signal** | BNPL; global expansion | — |
| **Note** | No public contact found | — |

### Sezzle — sezzle.com
| Field | Detail | Confidence |
|-------|--------|:---:|
| **Exec** | Charlie Youakim — CEO | — |
| **Company LinkedIn** | MISSING — not found on site sweep | — |
| **Public email** | **MISSING** — no public address found on site sweep | — |
| **Source** | live curl sweep of sezzle.com (+/about /contact /team) 2026-08-14; leads file for exec/DMPS | — |
| **DMPS** | 75 | — |
| **Intent signal** | Merchant BNPL | — |
| **Note** | No public contact found | — |

---

## Coverage Summary

| Metric | Count |
|---|---|
| Companies covered | 7 |
| Companies with verified public email (H) | 0 |
| Companies with verified LinkedIn (H) | 3 |
| Companies with NO public exec email | 7 — see §0 |

---

## Notes on Method & Caveats
- **No emails invented.** Every direct exec email above is either (a) publicly listed on the company site (H), or (b) carried from the leads file / format-inferred and marked M/L. Any M/L address must be verified before sending (owner LLM or hunter.io-style lookup).
- **LinkedIn URLs marked H** come from the company's own site footer/about pages — these are the companies' own published links, so risk is low; LinkedIn itself was not logged into, so profile pages weren't fetched directly.
- **Exec names/roles** are carried from the leads file at M confidence (they were researched previously); only company-level contact data was re-verified live this session.
- **JS-heavy / bot-protected sites** (e.g. doordash, carmax, duolingo, zapier) returned no extractable contacts — for these, exec email is MISSING by design and LinkedIn should be resolved via LinkedIn search (marked L).

## Files
- **Lead list:** `leads_*` in `paydeal.ai/01-research/`
- **Verification sweep:** `/home/team/shared/contact-verification/batch1-findings-2026-08-14.txt` (raw live-sweep output, 70 companies)
- **Reference format:** `../nofail.ai/01-research/contact_nofail.ai.md`
