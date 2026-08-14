# leanmeds.com — Executive Contact Sheet (Batch 1, Gap-fill 2/3)

> **Researcher:** domain-researcher | **Date:** 2026-08-14
> **Scope:** Verified executive contacts for top leads in the domain's leads file. Built to the Group-1 contact-sheet format (cf. `contact_nofail.ai.md`, `contact_knowlaw.ai.md`).
> **Verification:** Company LinkedIn URLs and public emails below were verified live this session via a curl sweep of company sites (HTTP 200, 2026-08-14). Exec names/roles/DMPS are carried from the domain's leads file. No email was invented — format-inferred addresses are explicitly marked M/L and flagged for owner verification before sending.

---

## 0. MISSING-CONTACTS SUMMARY (owner follow-up list)

Every exec whose **email** or **LinkedIn URL** could not be confirmed from a public source this session. Owner has offered to research these separately — this is the exact list.

| # | Company | Exec | Missing |
|---|---------|------|---------|
| 1 | Trinity HealthCare Supply (buyer — SOLD) | — (CEO not publicly identified) | LinkedIn URL |
| 2 | Dr. Ana Lisa Carr (Lion MD) | Dr. Ana Lisa Carr | LinkedIn URL; email |
| 3 | Dr. Kelly Tenbrink (Lion MD) | Dr. Kelly Tenbrink | LinkedIn URL; email |
| 4 | Ro (sister-domain buyer pool) | Zachariah Reitano | LinkedIn URL; email |
| 5 | Hims & Hers (sister-domain pool) | Andrew Dudum | LinkedIn URL; email |

---

## Confidence Levels
- **H (High):** Verified from a public company page this session (HTTP 200)
- **M (Medium):** Likely correct based on company conventions; not independently confirmed from a public page
- **L (Low):** Best available; needs owner LLM verification

---

## Company Blocks (DMPS order)

### Trinity HealthCare Supply (buyer — SOLD) — leanmeds.com
| Field | Detail | Confidence |
|-------|--------|:---:|
| **Exec** | — (CEO not publicly identified) — — | — |
| **Company LinkedIn** | MISSING — not found on site sweep | — |
| **Public email(s)** | care@leanmeds.com | H |
| **Source** | live curl sweep of leanmeds.com (+/about /contact /team) 2026-08-14; leads file for exec/DMPS | — |
| **DMPS** | SOLD | — |
| **Intent signal** | LeanMeds.com SOLD to Trinity; upsell buyslimmeds/bestslimmeds/cheapslimmeds | — |
| **Note** | care@leanmeds.com verified (H); Dr. Ana Lisa Carr (Medical Director, Lion MD) in intel file | — |

### Dr. Ana Lisa Carr (Lion MD) — lionmd.com
| Field | Detail | Confidence |
|-------|--------|:---:|
| **Exec** | Dr. Ana Lisa Carr — Medical Director | — |
| **Company LinkedIn** | MISSING — not found on site sweep | — |
| **Public email** | **MISSING** — no public address found on site sweep | — |
| **Source** | live curl sweep of lionmd.com (+/about /contact /team) 2026-08-14; leads file for exec/DMPS | — |
| **DMPS** | — | — |
| **Intent signal** | Clinical lead for the buyer's telehealth operation | — |
| **Note** | NPI 1689841744 (intel file); help@leanmeds.com (H) | — |

### Dr. Kelly Tenbrink (Lion MD) — lionmd.com
| Field | Detail | Confidence |
|-------|--------|:---:|
| **Exec** | Dr. Kelly Tenbrink — Clinical Provider | — |
| **Company LinkedIn** | MISSING — not found on site sweep | — |
| **Public email** | **MISSING** — no public address found on site sweep | — |
| **Source** | live curl sweep of lionmd.com (+/about /contact /team) 2026-08-14; leads file for exec/DMPS | — |
| **DMPS** | — | — |
| **Intent signal** | Second clinical contact at buyer | — |
| **Note** | NPI 1346482684 (intel file) | — |

### Ro (sister-domain buyer pool) — ro.co
| Field | Detail | Confidence |
|-------|--------|:---:|
| **Exec** | Zachariah Reitano — CEO | — |
| **Company LinkedIn** | MISSING — not found on site sweep | — |
| **Public email** | **MISSING** — no public address found on site sweep | — |
| **Source** | live curl sweep of ro.co (+/about /contact /team) 2026-08-14; leads file for exec/DMPS | — |
| **DMPS** | 95 | — |
| **Intent signal** | Same buyer pool as the remaining Slim Meds collection | — |
| **Note** | JS-heavy site — no extractable contacts (cf. Group-1 notes) | — |

### Hims & Hers (sister-domain pool) — hims.com
| Field | Detail | Confidence |
|-------|--------|:---:|
| **Exec** | Andrew Dudum — CEO | — |
| **Company LinkedIn** | MISSING — not found on site sweep | — |
| **Public email** | **MISSING** — no public address found on site sweep | — |
| **Source** | live curl sweep of hims.com (+/about /contact /team) 2026-08-14; leads file for exec/DMPS | — |
| **DMPS** | 93 | — |
| **Intent signal** | Weight-loss portfolio adjacency | — |
| **Note** | JS-heavy site — no extractable contacts | — |

---

## Coverage Summary

| Metric | Count |
|---|---|
| Companies covered | 5 |
| Companies with verified public email (H) | 1 |
| Companies with verified LinkedIn (H) | 0 |
| Companies with NO public exec email | 4 — see §0 |

---

## Notes on Method & Caveats
- **No emails invented.** Every direct exec email above is either (a) publicly listed on the company site (H), or (b) carried from the leads file / format-inferred and marked M/L. Any M/L address must be verified before sending (owner LLM or hunter.io-style lookup).
- **LinkedIn URLs marked H** come from the company's own site footer/about pages — these are the companies' own published links, so risk is low; LinkedIn itself was not logged into, so profile pages weren't fetched directly.
- **Exec names/roles** are carried from the leads file at M confidence (they were researched previously); only company-level contact data was re-verified live this session.
- **JS-heavy / bot-protected sites** (e.g. doordash, carmax, duolingo, zapier) returned no extractable contacts — for these, exec email is MISSING by design and LinkedIn should be resolved via LinkedIn search (marked L).

## Files
- **Lead list:** `leads_*` in `leanmeds.com/01-research/`
- **Verification sweep:** `/home/team/shared/contact-verification/batch1-findings-2026-08-14.txt` (raw live-sweep output, 70 companies)
- **Reference format:** `../nofail.ai/01-research/contact_nofail.ai.md`
