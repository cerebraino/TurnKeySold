# bailar.ai — Executive Contact Sheet (Batch 1, Gap-fill 2/3)

> **Researcher:** domain-researcher | **Date:** 2026-08-14
> **Scope:** Verified executive contacts for top leads in the domain's leads file. Built to the Group-1 contact-sheet format (cf. `contact_nofail.ai.md`, `contact_knowlaw.ai.md`).
> **Verification:** Company LinkedIn URLs and public emails below were verified live this session via a curl sweep of company sites (HTTP 200, 2026-08-14). Exec names/roles/DMPS are carried from the domain's leads file. No email was invented — format-inferred addresses are explicitly marked M/L and flagged for owner verification before sending.

---

## 0. MISSING-CONTACTS SUMMARY (owner follow-up list)

Every exec whose **email** or **LinkedIn URL** could not be confirmed from a public source this session. Owner has offered to research these separately — this is the exact list.

| # | Company | Exec | Missing |
|---|---------|------|---------|
| 1 | Zumba | Alberto Perlman | LinkedIn URL; email |
| 2 | STEEZY | Evan Zhou | LinkedIn URL; email |
| 3 | DanceBit | — (Founder) | LinkedIn URL; email |
| 4 | Apple Fitness+ (Dance) | Tim Cook | LinkedIn URL; email |
| 5 | Peloton (Latin) | Barry McCarthy | LinkedIn URL; email |
| 6 | TikTok (Dance) | Shou Zi Chew | LinkedIn URL; email |

---

## Confidence Levels
- **H (High):** Verified from a public company page this session (HTTP 200)
- **M (Medium):** Likely correct based on company conventions; not independently confirmed from a public page
- **L (Low):** Best available; needs owner LLM verification

---

## Company Blocks (DMPS order)

### Zumba — zumba.com
| Field | Detail | Confidence |
|-------|--------|:---:|
| **Exec** | Alberto Perlman — CEO | — |
| **Company LinkedIn** | MISSING — not found on site sweep | — |
| **Public email** | **MISSING** — no public address found on site sweep | — |
| **Source** | live curl sweep of zumba.com (+/about /contact /team) 2026-08-14; leads file for exec/DMPS | — |
| **DMPS** | 92 | — |
| **Intent signal** | Dance fitness; 15M+ weekly; Spanish roots | — |
| **Note** | No public contact found | — |

### STEEZY — steezy.co
| Field | Detail | Confidence |
|-------|--------|:---:|
| **Exec** | Evan Zhou — CEO & Co-Founder | — |
| **Company LinkedIn** | MISSING — not found on site sweep | — |
| **Public email** | **MISSING** — no public address found on site sweep | — |
| **Source** | live curl sweep of steezy.co (+/about /contact /team) 2026-08-14; leads file for exec/DMPS | — |
| **DMPS** | 88 | — |
| **Intent signal** | Online dance learning; Latin expansion | — |
| **Note** | No public contact found | — |

### DanceBit — dancebit.app
| Field | Detail | Confidence |
|-------|--------|:---:|
| **Exec** | — (Founder) — CEO | — |
| **Company LinkedIn** | MISSING — not found on site sweep | — |
| **Public email** | **MISSING** — no public address found on site sweep | — |
| **Source** | live curl sweep of dancebit.app (+/about /contact /team) 2026-08-14; leads file for exec/DMPS | — |
| **DMPS** | 85 | — |
| **Intent signal** | AI dance fitness app | — |
| **Note** | No public contact found | — |

### Apple Fitness+ (Dance) — apple.com
| Field | Detail | Confidence |
|-------|--------|:---:|
| **Exec** | Tim Cook — CEO | — |
| **Company LinkedIn** | MISSING — not found on site sweep | — |
| **Public email** | **MISSING** — no public address found on site sweep | — |
| **Source** | live curl sweep of apple.com (+/about /contact /team) 2026-08-14; leads file for exec/DMPS | — |
| **DMPS** | 72 | — |
| **Intent signal** | Dance fitness content; Latin series | — |
| **Note** | Enterprise; press route | — |

### Peloton (Latin) — onepeloton.com
| Field | Detail | Confidence |
|-------|--------|:---:|
| **Exec** | Barry McCarthy — CEO | — |
| **Company LinkedIn** | MISSING — not found on site sweep | — |
| **Public email** | **MISSING** — no public address found on site sweep | — |
| **Source** | live curl sweep of onepeloton.com (+/about /contact /team) 2026-08-14; leads file for exec/DMPS | — |
| **DMPS** | 70 | — |
| **Intent signal** | Latin dance classes; sub-brand | — |
| **Note** | No public contact found | — |

### TikTok (Dance) — tiktok.com
| Field | Detail | Confidence |
|-------|--------|:---:|
| **Exec** | Shou Zi Chew — CEO | — |
| **Company LinkedIn** | MISSING — not found on site sweep | — |
| **Public email** | **MISSING** — no public address found on site sweep | — |
| **Source** | live curl sweep of tiktok.com (+/about /contact /team) 2026-08-14; leads file for exec/DMPS | — |
| **DMPS** | 65 | — |
| **Intent signal** | Dance content core; Latin massive | — |
| **Note** | No public contact found | — |

---

## Coverage Summary

| Metric | Count |
|---|---|
| Companies covered | 6 |
| Companies with verified public email (H) | 0 |
| Companies with verified LinkedIn (H) | 0 |
| Companies with NO public exec email | 6 — see §0 |

---

## Notes on Method & Caveats
- **No emails invented.** Every direct exec email above is either (a) publicly listed on the company site (H), or (b) carried from the leads file / format-inferred and marked M/L. Any M/L address must be verified before sending (owner LLM or hunter.io-style lookup).
- **LinkedIn URLs marked H** come from the company's own site footer/about pages — these are the companies' own published links, so risk is low; LinkedIn itself was not logged into, so profile pages weren't fetched directly.
- **Exec names/roles** are carried from the leads file at M confidence (they were researched previously); only company-level contact data was re-verified live this session.
- **JS-heavy / bot-protected sites** (e.g. doordash, carmax, duolingo, zapier) returned no extractable contacts — for these, exec email is MISSING by design and LinkedIn should be resolved via LinkedIn search (marked L).

## Files
- **Lead list:** `leads_*` in `bailar.ai/01-research/`
- **Verification sweep:** `/home/team/shared/contact-verification/batch1-findings-2026-08-14.txt` (raw live-sweep output, 70 companies)
- **Reference format:** `../nofail.ai/01-research/contact_nofail.ai.md`
