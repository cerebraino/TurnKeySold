# TurnKeySold — Repository Index (LLM & Human Onboarding)

> **Read this first.** This is the single canonical entry point to understand every asset in this repository, how the information is structured, and which guiding documents govern the work. A future LLM (or new team member) should be able to read **only this file** and reach full context — without exploring 600+ files.
>
> **Last updated:** 2026-08-15 · **Repo:** `cerebraino/TurnKeySold` · **Portfolio:** 145 domains + 1 bundle (coldbeerportfolio) = 146 dirs in `DOMAINS/`

---

## Quick Reference (asset type → location → status → format doc)

| Asset | Location | Status (ASSET_AUDIT 2026-08-14) | Defines the format |
|---|---|---|---|
| Appraisal / value (A1) | `01-research/leads_<domain>.md` §1 | 146/146 | — |
| Buyer categories (A2) | `01-research/leads_<domain>.md` §2 | 146/146 | `COMPANY/research-framework.md` |
| DMPS-scored leads (A3) | `01-research/leads_<domain>.md` §3 | 146/146 | `COMPANY/research-framework.md` |
| Verified exec contact sheets (A4) | `01-research/contact-sheet_<domain>.md` (+ older `contact_<domain>.md`) | ~95/146 (103 in in-progress batch-4) | `docs/assets/ASSET_CHECKLIST.md` |
| Outreach email packs (A5) | `02-outreach/email-pack_<domain>.md` | 100/146 | header block in any `email-pack_*.md` |
| Micro-messages (A6) | `02-outreach/micro-messages_<domain>.md` | **146/146 claimed — ⚠️ only 28 files verified in repo** | `docs/methodology/three-line-outreach-framework.md` |
| Outreach briefs (B1) | `02-outreach/brief_<domain>.md` | 145/146 (coldbeerportfolio n/a) | `COMPANY/campaign-playbook.md` |
| Google ad enrichment (B2) | embedded in `leads_<domain>.md` | 22 domains | — |
| Google Alerts (B3) | `google_alerts_v2.csv` | 127 domains | — |

> ⚠️ **Verification flags (do not propagate the audit's numbers blindly):** (1) A6 "146/146 per-domain files" is **not** reflected in the repo — only 28 `micro-messages_*.md` files exist; the full 146-domain micro-message content lives in `DOMAINS/CSV/TurnKeySold_Full_Portfolio_Ranked.csv` (col 5) + `DOMAINS/CSV/micro_messages_drafts.md`. (2) The email-pack body policy is **"<100 words"** (not "<60 words" — that was an earlier assumption; micro-messages are the short 150–220-char ones).

---

## 1. Repo Purpose & Current State

**TurnKeySold Domains** — a TurnKeySold venture. **Mission:** build the best agentic sales company in the world, starting with premium domains. **Revenue model:** 20% success-fee commission on closed sales; no upfront fees. **Tagline:** *Premium domains, sold on purpose.*

This repo is the **single canonical source of truth** (Architecture Principle P1). It holds the complete research-to-outreach pipeline for the domain portfolio: appraisals, DMPS-scored buyer lead lists, verified contact sheets, pricing-free outreach briefs, email packs, and micro-messages — plus the methodology/architecture that governs the work.

**Current coverage** (from `ASSET_AUDIT_2026-08-14.md`, which is the LIVE tracker updated as batches merge):

| Layer | Coverage |
|---|---|
| A1 Appraisal | 146/146 |
| A2 Buyer categories | 146/146 |
| A3 Buyer companies + execs (DMPS) | 146/146 |
| A4 Verified exec contact sheets | ~95/146 (103 in in-progress batch-4 branch) |
| A5 Outreach email packs | 100/146 |
| A6 Micro-messages | 146/146 claimed (⚠️ 28 verified — see flag above) |
| B1 Outreach briefs | 145/146 |
| B2 Google ad enrichment | 22 leads files |
| B3 Google Alerts | 127 domains |

**The research layer (A1–A3, B1) is complete. The execution layer (A4–A6) is still being backfilled** in ~25-domain batches ordered by value rank.

---

## 2. Directory Map

```
TurnKeySold/
├── README.md                      ← Stale index (says "131 domains" — WRONG). See REPO_INDEX.md (this file).
├── REPO_INDEX.md                  ← THIS FILE — canonical navigation
│
├── DOMAINS/                       ← 146 per-domain packages (145 domains + coldbeerportfolio)  ← CORE CONTENT
│   ├── CSV/                       ← Master ranked portfolio CSV + micro-message drafts
│   └── [domain]/                  ← lowercase, dot-included (e.g. agizent.com)
│       ├── 01-research/           ← leads, contact sheets, expansions
│       └── 02-outreach/           ← briefs, email packs, micro-messages
│
├── COMPANY/                       ← Brand + methodology (brand-identity, campaign-playbook, research-framework, seller-onboarding, website-brief)
├── OUTREACH/                      ← Master email templates + older alert/email CSVs
├── PORTFOLIO/                     ← Portfolio analysis + appraisal CSVs
├── WEBSITE/                       ← TurnKeySold.com HTML/CSS source
├── docs/                          ← Architecture, asset standards, methodology (see below)
├── contact-verification/          ← Batch contact-verification findings (2026-08-14)
│
└── (root CSVs + owner research .md + Genspark .xlsx exports — see §6)
```

**`docs/` subdirectories:**
- `docs/architecture/` — `DECISION_ARCHITECTURE.md`, `KNOWLEDGE_MODEL.md`, `METADATA_STANDARD.md`, `ARCHITECTURE_PRINCIPLES.md`, `knowledge-architecture-review.md`, `phase1-preparation.md`, `phase1-report.md`
- `docs/methodology/` — `three-line-outreach-framework.md`, `three-line-messages-36-domains.md`
- `docs/assets/` — `ASSET_CHECKLIST.md`, `GAP_ANALYSIS_2026-08-12.md`

---

## 3. Per-Domain Structure

For a domain dir, e.g. `DOMAINS/agizent.com/`:

### `01-research/` — WHAT WE KNOW
| File | Contains |
|---|---|
| `leads_<domain>.md` | §1 valuation (comparables, brandability /50, value range, anchor) · §2 buyer categories · §3 ranked DMPS lead table (Tier 1 = 80–100, Tier 2 = 60–79) · optional Google Search Enrichment · owner-file review notes |
| `contact-sheet_<domain>.md` | **NEW** Group-1 verified exec contact sheets — per-company blocks in DMPS order, H/M/L confidence, "best exec to reach", and **§0 MISSING-CONTACTS summary** (owner follow-up list) |
| `contact_<domain>.md` | **OLDER** naming for flagship domains (same content shape, being superseded by `contact-sheet_`) |
| `*-buyer-expansion.md`, `*-buyers.md`, `*-intel.md` | Expanded buyer universe (20–40+ companies) and corporate deep-dives (e.g. `trinity-healthcare-intel.md`) |

### `02-outreach/` — WHAT WE SAY
| File | Contains |
|---|---|
| `brief_<domain>.md` | Pricing-free positioning brief: overview, lead summary, messaging strategy, email/LinkedIn templates, objection handling, **internal pricing** (always behind a marker, never in copy) |
| `micro-messages_<domain>.md` | 150–220-char Three-Line one-liners per top-10 leads (signal → bridge → tiny ask). **A6 target: 146/146; only 28 files actually in repo** |
| `email-pack_<domain>.md` | **NEW canonical format**: header block (Domain/Anchor/Policy/Sources/Contacts) + 5 leads, each with Context / Subject / Email / Follow-up Day 3 + 7 + 14 / Motivation button |
| `outreach-<domain>.md` | **OLD format** (flagship domains) — being converted to the `email-pack_` format |

### `03-buyer-intel/` — brand research deep-dives
e.g. `slimmeds-brand-research.md` (companies already using "Slim Meds" phrasing + USPTO analysis). Also `03-results/` holds sale records for sold domains (LeanMeds.com).

**Naming-convention note:** the repo is mid-migration. `outreach-<domain>.md` (old, hyphen, ~26 files) is being replaced by `email-pack_<domain>.md` (new, underscore, 100 files). `contact_<domain>.md` (old, ~20 files) is being replaced by `contact-sheet_<domain>.md` (new, 75 files). Read the **new** format first; treat old files as legacy for flagship domains.

---

## 4. Asset Audit (LIVE coverage tracker)

`ASSET_AUDIT_2026-08-14.md` is the live coverage tracker, updated as batches merge. It defines 9 asset types:

| ID | Asset | Meaning |
|---|---|---|
| A1 | Appraisal | Defensible value (comparables + brandability + range) |
| A2 | Buyer categories | 3+ industry targets per domain |
| A3 | DMPS leads | Ranked buyer companies with execs |
| A4 | Verified contact sheets | Exec contact channels (H/M/L confidence, §0 missing list) |
| A5 | Email packs | Initial + Day 3/7/14 follow-ups, top-5 leads |
| A6 | Micro-messages | Short personalized one-liners |
| B1 | Briefs | Pricing-free positioning brief |
| B2 | Google ad enrichment | Paid/organic competitor landscape (embedded in leads) |
| B3 | Google Alerts | Buyer-signal monitoring queries |

Current status is quoted in §1. The gap-fill plan (dispatched 2026-08-14) is: micro-message split → contact sheets (researcher, value-ranked batches) → email packs (architect, ~25/batch).

---

## 5. Guiding Documents & Skills (one paragraph each)

- **`docs/architecture/DECISION_ARCHITECTURE.md`** — the decision protocol: tactical/operational/strategic/constitutional tiers; three authority zones (Agent → Lead → Founder); confidence model (HIGH/MEDIUM/LOW); assumption lifecycle; experiment discipline; belief revision. Read when you need to know *who decides what and how*.
- **`docs/architecture/KNOWLEDGE_MODEL.md`** — the conceptual vocabulary (Organization, Person, Domain, Source, Evidence, Market; Hypothesis, Opportunity, Contact, Learning, Pattern, Principle, Playbook, Bundle, Outcome, Campaign) and the core intelligence loop. Read first to understand the shared vocabulary.
- **`docs/architecture/METADATA_STANDARD.md`** — the YAML-frontmatter provenance standard (artifact_id, created_by, source, confidence). Proposed, not yet enforced. Read before creating/editing research artifacts.
- **`docs/architecture/ARCHITECTURE_PRINCIPLES.md`** — P1–P10, the non-negotiable rules (canonical source, structured data, relationships, templates, provenance, naming, delete-vs-duplicate, git reversibility, lifecycle, LLM navigation). Read before any structural change.
- **`Three-Line_Framework_for_Premium_Domain_Outbound.md`** (= `docs/methodology/three-line-outreach-framework.md`) — the core cold-outreach methodology: signal → bridge → tiny ask, ≤250 chars, no pricing/links/"I own". Governs all outreach copy.
- **`docs/methodology/three-line-messages-36-domains.md`** — pre-written Three-Line messages for 25–36 domain-buyer pairings (ranked strongest→weakest).
- **`docs/assets/ASSET_CHECKLIST.md`** — the "complete" bar for each asset type A1–A6/B1–B6. Read to know what "done" means.
- **`Domain_Buyer_Prospecting_Research_10_Domains.md`** — owner's buyer-prospecting research on 10 priority domains (NoBreak, NoFail, Automovil, KnowLaw, PayCar, HipotecaHispana, HispanoAbogado, LatinoMedico, OneGuy, PossibleAGI).
- **`domain_buyer_prospects.md`** — buyer prospecting report (YC/Product Hunt/TechCrunch/etc. sources), ranked by ability to pay.
- **`verdict_domain_buyer_prospects.md`** — the researcher's integration verdict: which prospects were ADDED to leads files, with source + H/M/L confidence ("add, don't remove" rule).
- **`coldbeer-portfolio-buyers.md`** — Cold Beer portfolio (6 beer domains) buyer universe + Google Search Enrichment (top advertisers with +10 DMPS signals).

---

## 6. Data Files

| File | Columns / Purpose |
|---|---|
| `DOMAINS/CSV/TurnKeySold_Full_Portfolio_Ranked.csv` | **The value-ranked master portfolio index.** 146 rows, ranked by value. Cols: `Domain, Approx Defensible Market Value, Main 3 Buyer Categories, Top-3 Companies, Sample Micro-Message` |
| `DOMAINS/CSV/micro_messages_drafts.md` | Pre-split source of all micro-messages (split into per-domain files — incomplete) |
| `docs/outreach-contact-list-complete.csv` | **Exec contact master.** Cols: `#, Priority (P1/P2/P3), Batch, Name, Title, Company, Domain, LinkedIn, Email, Confidence, Motivation, Micro-Message, Has Message` |
| `docs/outreach-contact-list-batch1.csv` | Batch-1 slice of the above (adds `Price`, `Twitter/X`, `Pitch Angle`) |
| `NameCheap_Domain_List.csv` | Raw registrar export. Cols: `Domain Name, privacy, status, auto-renew, expiration` |
| `domain-backlog-new.csv` (+ `PORTFOLIO/` copy) | 110 unprocessed domains. Cols: `Domain, Category, Est. Value, Priority, Notes` |
| `google_alerts_v2.csv` | 127 domains × 2-3 buyer-signal queries. Cols: `Domain, Value Range, Primary Query, Secondary Query, Market` |
| `OUTREACH/email-templates.md`, `outreach-email-list.csv`, `prospect-emails.md` | Reusable email frameworks + prospect lists (older) |
| `OUTREACH/google_alerts.csv` | Older 62-domain alert queries (superseded by v2) |
| `PORTFOLIO/full_appraisal.csv` | Appraisal spreadsheet. Cols: `Domain, Category, Est. Low/High, Brandability (1-10), Sale Potential, Top Buyer Industry, Priority` |
| `contact-verification/batch*-findings-2026-08-14.txt` | Raw contact-verification working notes (3 batches) |
| `Executive_contact_...xlsx`, `ViveMucho.com_...xlsx`, `Je7mTksY.xlsx` | Genspark AI Sheets research exports (owner source data) |

---

## 7. Workflow & Conventions

### Git / code workflow
From `/home/team/shared/WORKFLOW.md` (the managed code workflow):
1. Members push code to **feature branches** and open **pull requests**.
2. The team lead reviews and merges PRs.
3. Before starting new work, pull the latest default branch so you branch from up-to-date code.

- **Lead-side git ops** happen in `/home/agent-lead/TurnKeySold` (the lead's canonical working copy).
- **Members' concurrent workspace** is `/home/team/shared/repo-review`.
- Active feature branches (as of this writing): `research/contact-sheets-batch4`, `outreach/email-packs-batch5`, etc. — work is landed via PRs, not direct pushes to `main`.

### Batch convention
Gap-filling runs in **~25-domain batches ordered by CSV value rank** (most valuable first, alphabetical within the value tier):
- **Contact sheets (A4, researcher):** batches 1–3 merged (70→95/146); batch 4 in progress (+8 → 103). ~43 domains remain.
- **Email packs (A5, architect):** batches 1–4 merged (24+25+25+25 + putero.online = 100/146); batch 5 in progress. ~46 domains remain.
- **Micro-messages (A6):** claimed complete but per-domain split not fully committed (see flag in Quick Reference).

### Skip rules
- **`leanmeds.com`** — SOLD (Trinity HealthCare Supply). No further outreach assets needed.
- **`coldbeerportfolio`** — a portfolio bundle (6 beer domains), not a single domain; no leads/brief by design ($350K anchor, AB InBev top buyer).

### Content policies (verified from sample `email-pack_*.md` files)
- **Pricing-free** — no dollar figures in outreach copy (pricing lives only behind "Internal Reference" markers in briefs).
- **No "I own" framing** — use "the premium domain X" instead.
- **No links** in first-touch emails.
- **Email bodies <100 words** (note: *not* "<60 words" — that's the micro-message char range, which is 150–220 chars).
- **No invented emails** — unverifiable exec contacts are marked `MISSING` and listed for owner follow-up; H/M/L confidence applied per contact.

---

## 8. Future Work

From `ASSET_AUDIT_2026-08-14.md` + the business plan:
- **A4 contact sheets:** ~43 domains remaining (batches 5+).
- **A5 email packs:** ~46 domains remaining (batch 5+).
- **A6 micro-messages:** finish the per-domain `.md` split (28 done of 146 claimed).
- **§0 MISSING lists** in contact sheets are owner-research items (Tier-1 execs whose direct channels couldn't be verified).
- **Flagship pack review** in progress (old `outreach-*.md` → new `email-pack_*.md` conversion).
- **Long-term (Phase 2+, not yet built):** `_templates/`, `_data/*.json`, `_indexes/`, `_playbooks/` restructuring (see `docs/architecture/knowledge-architecture-review.md`). Do **not** assume these exist yet.

---

*This index is a living document. Update it when the repo structure changes, a new asset type lands, or a phase of the architecture roadmap is implemented. The canonical coverage numbers always live in `ASSET_AUDIT_2026-08-14.md` — this file points to it rather than duplicating it.*
