# TurnKeySold — Repository Index (LLM & Human Onboarding)

> **Read this first.** This is the single canonical entry point to understand every asset in this repository, how the information is structured, and which guiding documents govern the work. A future LLM (or new team member) should be able to read **only this file** and reach full context — without exploring 600+ files.
>
> **Last updated:** 2026-08-27 · **Repo:** `cerebraino/TurnKeySold` · **Portfolio:** 145 domains + 1 bundle (coldbeerportfolio) = 146 dirs in `DOMAINS/`
>
> **For LLMs:** see **[§9. LLM Usage Playbook](#9-llm-usage-playbook)** — how to actually do work against this repo.

---

## Quick Reference (asset type → location → status → format doc)

| Asset | Location | Status | Defines the format |
|---|---|---|---|
| Appraisal / value (A1) | `01-research/leads_<domain>.md` §1 | **146/146** | `COMPANY/research-framework.md` |
| Buyer categories (A2) | `01-research/leads_<domain>.md` §2 | **146/146** | `COMPANY/research-framework.md` |
| DMPS-scored leads (A3) | `01-research/leads_<domain>.md` §3 | **146/146** | `COMPANY/research-framework.md` |
| Verified exec contact sheets (A4) | `01-research/contact-sheet_<domain>.md` | **146/146 COMPLETE** (126 new `contact-sheet_` + 20 legacy `contact_`) | `docs/assets/ASSET_CHECKLIST.md` |
| Outreach email packs (A5) | `02-outreach/email-pack_<domain>.md` | **145/146** (only sold `leanmeds.com` remains) | header block in any `email-pack_*.md` |
| Micro-messages (A6) | `02-outreach/micro-messages_<domain>.md` | **147/147** | `docs/methodology/three-line-outreach-framework.md` |
| Outreach briefs (B1) | `02-outreach/brief_<domain>.md` | **145/146** (coldbeerportfolio bundle n/a) | `COMPANY/campaign-playbook.md` |
| Google ad enrichment (B2) | embedded in `leads_<domain>.md` §"Google Search Enrichment" | **24 leads files** | — |
| Google Alerts (B3) | `google_alerts_v2.csv` | **127 domains** (audit); CSV now holds ~140 unique domains | — |

> **Source of truth:** all coverage numbers above live canonically in **`ASSET_AUDIT_2026-08-14.md`** (the live tracker updated as batches merge). This index points to it and records the *actual filesystem* counts verified 2026-08-27 — where the two differ (B2, B3, A4) the discrepancy is flagged below so the audit can be reconciled next.
>
> **Reconciliation notes (verified 2026-08-27):**
> - **A4** — audit says 146/146 ✓ confirmed on disk: 126 `contact-sheet_*.md` + 20 legacy `contact_*.md` = 146 files (100% of 146 domain dirs).
> - **A5** — audit says 145/146 ✓: 145 `email-pack_*.md` on disk; `leanmeds.com` is sold so it correctly has no pack. 26 legacy `outreach-*.md` coexist for flagship domains (see §3).
> - **A6** — audit says 147/147 ✓ confirmed (146 domains + coldbeerportfolio bundle).
> - **B2** — audit says 22; actual grep of `leads_*.md` for "Google Search Enrichment" returns **24** (2 enriched since the audit).
> - **B3** — audit says 127 domains; `google_alerts_v2.csv` on disk now holds **143 rows / ~140 unique domain tokens** (some domains have `-health` style secondary variants). The audit's 127 is stale relative to the CSV — treat the CSV as the live list.

---

## 1. Repo Purpose & Current State

**TurnKeySold Domains** — a TurnKeySold venture. **Mission:** build the best agentic sales company in the world, starting with premium domains. **Revenue model:** 20% success-fee commission on closed sales; no upfront fees. **Tagline:** *Premium domains, sold on purpose.*

This repo is the **single canonical source of truth** (Architecture Principle P1). It holds the complete research-to-outreach pipeline for the domain portfolio: appraisals, DMPS-scored buyer lead lists, verified contact sheets, pricing-free outreach briefs, email packs, and micro-messages — plus the methodology/architecture that governs the work.

**Current coverage** (from `ASSET_AUDIT_2026-08-14.md` + filesystem verify 2026-08-27):

| Layer | Coverage |
|---|---|
| A1 Appraisal | 146/146 |
| A2 Buyer categories | 146/146 |
| A3 Buyer companies + execs (DMPS) | 146/146 |
| A4 Verified exec contact sheets | **146/146 COMPLETE** |
| A5 Outreach email packs | **145/146** (sold leanmeds.com only gap) |
| A6 Micro-messages | **147/147** |
| B1 Outreach briefs | 145/146 (coldbeerportfolio bundle n/a) |
| B2 Google ad enrichment | 24 leads files |
| B3 Google Alerts | 127 domains (CSV ≈ 140 unique) |

**The research + execution layers are now COMPLETE for all actionable assets.** A4 contact sheets and A5 email packs reached full/effectively-full coverage as of 2026-08-20 (A5 = 145/146, the last gap being the sold domain). Remaining work is maintenance/expansion, not backfill (see §8).

**Sold:** `LeanMeds.com` → Trinity HealthCare Supply (via Spaceship). Its dir still holds research assets for reference/process reuse.

---

## 2. Directory Map

```
TurnKeySold/
├── README.md                      ← STALE ("131 domains" — WRONG). See REPO_INDEX.md (this file).
├── REPO_INDEX.md                  ← THIS FILE — canonical navigation
├── AGENTS.md                      ← LLM entry point (points here as mandatory first read)
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
├── contact-verification/          ← Batch contact-verification findings (2026-08-14 → 2026-08-20)
│
└── (root CSVs + owner research .md — see §6)
```

**`docs/` subdirectories:**
- `docs/architecture/` — `DECISION_ARCHITECTURE.md`, `KNOWLEDGE_MODEL.md`, `METADATA_STANDARD.md`, `ARCHITECTURE_PRINCIPLES.md`, `knowledge-architecture-review.md`, `phase1-preparation.md`, `phase1-report.md`
- `docs/methodology/` — `three-line-outreach-framework.md`, `three-line-messages-36-domains.md`
- `docs/assets/` — `ASSET_CHECKLIST.md`, `GAP_ANALYSIS_2026-08-12.md`
- `docs/` — `MISSING-CONTACT_2026-08-20.md` (canonical owner follow-up list, §5), `outreach-contact-list-complete.csv` (§6)

---

## 3. Per-Domain Structure

For a domain dir, e.g. `DOMAINS/agizent.com/`:

### `01-research/` — WHAT WE KNOW
| File | Contains |
|---|---|
| `leads_<domain>.md` | §1 valuation (comparables, brandability /50, value range, anchor) · §2 buyer categories · §3 ranked DMPS lead table (Tier 1 = 80–100, Tier 2 = 60–79) · optional "Google Search Enrichment" section · owner-file review notes / "Owner N-Domain Integration" section |
| `contact-sheet_<domain>.md` | **Canonical Group-1 verified exec contact sheets** — per-company blocks in DMPS order, **H/M/L confidence**, "best exec to reach", and **§0 MISSING-CONTACTS summary** (owner follow-up list) |
| `contact_<domain>.md` | **LEGACY naming for ~20 flagship domains** (same shape, being superseded by `contact-sheet_`). Check BOTH for those domains; newer buyers may be in either. |
| `*-buyer-expansion.md`, `*-buyers.md`, `*-intel.md` | Expanded buyer universe (20–40+ companies) and corporate deep-dives (e.g. `trinity-healthcare-intel.md`) |

### `02-outreach/` — WHAT WE SAY
| File | Contains |
|---|---|
| `brief_<domain>.md` | Pricing-free positioning brief: overview, lead summary, messaging strategy, email/LinkedIn templates, objection handling, **internal pricing** (always behind a marker, never in copy) |
| `micro-messages_<domain>.md` | 150–220-char Three-Line one-liners per top-10 leads (signal → bridge → tiny ask). **A6: 147/147 files.** |
| `email-pack_<domain>.md` | **Canonical active format**: header block (Domain/Anchor/Policy/Sources/Contacts) + 5 leads, each with Context / Subject / Email / Follow-up Day 3 + 7 + 14 / Motivation button |
| `outreach-<domain>.md` | **Legacy format** for ~26 flagship domains (some domains now have BOTH `outreach-` legacy AND `email-pack_` current — read the `email-pack_` one). |

### `03-buyer-intel/` — brand research deep-dives
e.g. `slimmeds-brand-research.md` (companies already using "Slim Meds" phrasing + USPTO analysis). Also `03-results/` holds sale records for sold domains (LeanMeds.com).

**Naming-convention note (verified 2026-08-27):** the repo is mid-migration and both namespaces coexist.
- `contact_<domain>.md` (old) = **20 files** · `contact-sheet_<domain>.md` (new) = **126 files**. Read `contact-sheet_` first; only fall back to `contact_` where no `contact-sheet_` exists (or to catch older flagship buyer blocks).
- `outreach-<domain>.md` (old) = **26 files** · `email-pack_<domain>.md` (new) = **145 files**. Read `email-pack_` first; treat `outreach-` as legacy (some flagship domains carry both).

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

**Status (2026-08-27):** the backfill that this audit dispatched on 2026-08-14 (micro-message split → contact sheets → email packs) is **complete.** A4 = 146/146, A5 = 145/146 (sold gap), A6 = 147/147. See §1 for the full table and reconciliation flags.

---

## 5. Guiding Documents & Skills (one paragraph each)

- **`docs/architecture/DECISION_ARCHITECTURE.md`** — the decision protocol: tactical/operational/strategic/constitutional tiers; three authority zones (Agent → Lead → Founder); confidence model (HIGH/MEDIUM/LOW); assumption lifecycle; experiment discipline; belief revision. Read when you need to know *who decides what and how*.
- **`docs/architecture/KNOWLEDGE_MODEL.md`** — the conceptual vocabulary (Organization, Person, Domain, Source, Evidence, Market; Hypothesis, Opportunity, Contact, Learning, Pattern, Principle, Playbook, Bundle, Outcome, Campaign) and the core intelligence loop. Read first to understand the shared vocabulary.
- **`docs/architecture/METADATA_STANDARD.md`** — the YAML-frontmatter provenance standard (artifact_id, created_by, source, confidence). Proposed, not yet enforced. Read before creating/editing research artifacts.
- **`docs/architecture/ARCHITECTURE_PRINCIPLES.md`** — P1–P10, the non-negotiable rules (canonical source, structured data, relationships, templates, provenance, naming, delete-vs-duplicate, git reversibility, lifecycle, LLM navigation). Read before any structural change.
- **`Three-Line_Framework_for_Premium_Domain_Outbound.md`** (= `docs/methodology/three-line-outreach-framework.md`) — the core cold-outreach methodology: signal → bridge → tiny ask, ≤250 chars, no pricing/links/"I own". Governs all outreach copy.
- **`docs/methodology/three-line-messages-36-domains.md`** — pre-written Three-Line messages for 25–36 domain-buyer pairings (ranked strongest→weakest).
- **`docs/assets/ASSET_CHECKLIST.md`** — the "complete" bar for each asset type A1–A6/B1–B6. Read to know what "done" means.
- **`docs/MISSING-CONTACT_2026-08-20.md`** — **the canonical MISSING/CONTACT-gap owner list.** One consolidated doc: Section A = Tier-1/Wave-1 buyer execs whose direct contact couldn't be publicly sourced (24 rows, priority-ordered); Section B = the 10 domains flagged in PR #35 with no H-verified public emails. The owner researches these; a connected LLM should CONSULT it before outreach and never fabricate the missing addresses.
- **`Domain_Buyer_Prospecting_Research_10_Domains.md`** — owner's buyer-prospecting research on 10 priority domains (NoBreak, NoFail, Automovil, KnowLaw, PayCar, HipotecaHispana, HispanoAbogado, LatinoMedico, OneGuy, PossibleAGI).
- **`verdict_domain_buyer_prospects.md`** — the researcher's integration verdict: which prospects were ADDED to leads files, with source + H/M/L confidence ("add, don't remove" rule).
- **`verdict_10domains_integration.md`** — the researcher's verdict on integrating the owner 10-domain doc into the 11 affected leads files: DMPS adaptation, per-domain highlights, site-verification results, and the Tier-1/Wave-1 exec list needing contact-sheet follow-up (now built — those blocks live in the affected domains' `contact-sheet_*.md` and in `docs/MISSING-CONTACT_2026-08-20.md`).
- **`domain_buyer_prospects.md`** — buyer prospecting report (YC/Product Hunt/TechCrunch/etc. sources), ranked by ability to pay.
- **`coldbeer-portfolio-buyers.md`** — Cold Beer portfolio (6 beer domains) buyer universe + Google Search Enrichment (top advertisers with +10 DMPS signals).
- **`contact-verification/tier1-wave1-findings-2026-08-20.txt`**, **`contact-verification/final-a4-findings-2026-08-15.txt`**, `contact-verification/batch*-findings-2026-08-14.txt` — raw per-batch live-verification logs proving which emails/LinkedIn were confirmed (H) vs not. Audit-trail for the contact sheets (§9.3).

---

## 6. Data Files

| File | Columns / Purpose |
|---|---|
| `DOMAINS/CSV/TurnKeySold_Full_Portfolio_Ranked.csv` | **The value-ranked master portfolio index.** 146 rows, ranked by value. Cols: `Domain, Approx Defensible Market Value, Main 3 Buyer Categories, Top-3 Companies, Sample Micro-Message` |
| `DOMAINS/CSV/micro_messages_drafts.md` | Pre-split source of all micro-messages (per-domain files now complete — 147/147) |
| `docs/outreach-contact-list-complete.csv` | **Exec contact master.** Cols: `#, Priority (P1/P2/P3), Batch, Name, Title, Company, Domain, LinkedIn, Email, Confidence, Motivation, Micro-Message, Has Message` |
| `docs/outreach-contact-list-batch1.csv` | Batch-1 slice of the above (adds `Price`, `Twitter/X`, `Pitch Angle`) |
| `NameCheap_Domain_List.csv` | Raw registrar export. Cols: `Domain Name, privacy, status, auto-renew, expiration` |
| `domain-backlog-new.csv` (+ `PORTFOLIO/` copy) | 110 unprocessed domains. Cols: `Domain, Category, Est. Value, Priority, Notes` |
| `google_alerts_v2.csv` | Buyer-signal monitoring queries. Cols: `Domain, Value Range, Primary Query, Secondary Query, Market`. **~140 unique domains (143 rows) — exceeds the audit's 127.** |
| `OUTREACH/email-templates.md`, `outreach-email-list.csv`, `prospect-emails.md` | Reusable email frameworks + prospect lists (older) |
| `OUTREACH/google_alerts.csv` | Older 62-domain alert queries (superseded by v2) |
| `PORTFOLIO/full_appraisal.csv` | Appraisal spreadsheet. Cols: `Domain, Category, Est. Low/High, Brandability (1-10), Sale Potential, Top Buyer Industry, Priority` |
| `contact-verification/*.txt` | Raw contact-verification working notes (batches 1–5, final A4, tier1-wave1) |
| `Executive_contact_...xlsx`, `ViveMucho.com_...xlsx`, `Je7mTksY.xlsx` | Genspark AI Sheets research exports (owner source data) |

---

## 7. Workflow & Conventions

### Git / code workflow
From `/home/team/shared/WORKFLOW.md` (the managed code workflow):
1. Members push code to **feature branches** and open **pull requests**.
2. The team lead reviews and merges PRs.
3. Before starting new work, pull the latest default branch so you branch from up-to-date code.

- **Lead-side git ops** happen in `/home/agent-lead/TurnKeySold` (the lead's canonical working copy) — the lead holds push credentials.
- **Members' concurrent workspace** is `/home/team/shared/repo-review`. **Push often requires the lead's credentials** — if `git push` prompts for a username, commit locally and notify the lead that the branch is ready to push (the lead recovers it and opens the PR). **Verify `git branch --show-current`** before committing, as multiple agents share this clone.
- **Verify against `origin/main` before trusting a dispatch** — batch lists can overlap prior batches, and a lead merge may contain only the first commit of a branch.

### Batch convention
Gap-filling ran in **~25-domain batches ordered by CSV value rank** (most valuable first, alphabetical within tier). This backfill is **complete** (A4 146/146, A5 145/146); future domain work is new-buyer expansion or multi-domain portfolios, not value-rank batches.

### Skip rules
- **`leanmeds.com`** — SOLD (Trinity HealthCare Supply). No outreach assets to re-open; dir retained as process reference.
- **`coldbeerportfolio`** — a portfolio bundle (6 beer domains), not a single domain; no leads/brief by design ($350K anchor, AB InBev top buyer). It DOES have micro-messages + contact sheet + email pack.
- **`DOMAINS/CSV/`** — meta-directory (ranked CSV + micro-message drafts); NOT a domain. Portfolio-walking scripts must skip it.
- **Leads-file scans should be case-insensitive** (`os.listdir`/`find -iname`) — some uppercase stems exist (e.g. `leads_Puticlub.online.md`, `leads_Dalai.co.md`). Bundle/shared-pool domains may reference companion leads files.

### Content policies (verified from sample `email-pack_*.md` files)
- **Pricing-free** — no dollar figures in outreach copy (pricing lives only behind "Internal Reference" markers in briefs).
- **No "I own" framing** — use "the premium domain X" instead.
- **No links** in first-touch emails.
- **Email bodies <100 words** (note: *not* "<60 words" — that's the micro-message char range, which is 150–220 chars).
- **No invented emails** — unverifiable exec contacts are marked `MISSING` in the contact sheets and consolidated in `docs/MISSING-CONTACT_2026-08-20.md` for owner follow-up; H/M/L confidence applied per contact.

---

## 8. Future Work

From `ASSET_AUDIT_2026-08-14.md` + the business plan (current as of 2026-08-27):
- **Owner resolves `docs/MISSING-CONTACT_2026-08-20.md`** — the outstanding exec contacts (Section A priority: NoBreak Security/Yuval Olsha, Supreme CASA CEO, Zócalo Health/Erik Cardenas, Kavak/Carlos García Ottati, KnowLaw AI founder; Section B: PR #35 domains). This is the main open owner-side item.
- **Reconcile `ASSET_AUDIT_2026-08-14.md`** with the 2026-08-27 deltas (B2 22→24; B3 CSAV ~140 unique; and confirm A4/A5/A6 stays as-is). The audit filename still says 2026-08-14 though its numbers were updated through 2026-08-20 — consider bumping the date/version.
- **Migrate lingering legacy files** to canonical names (`contact_`→`contact-sheet_` for the 20, `outreach-`→`email-pack_` for the 26) if the team wants single-namespace consistency (not required — both are readable).
- **New-buyer contact-sheet expansions** as new Tier-1 buyers surface (pattern established in `verdict_10domains_integration.md`).
- **Long-term (Phase 2+, not yet built):** `_templates/`, `_data/*.json`, `_indexes/`, `_playbooks/` restructuring (see `docs/architecture/knowledge-architecture-review.md`). **Do not** assume these exist yet.

---

## 9. LLM Usage Playbook

This section tells a connected LLM *how to actually do work* against this repo. If you're an LLM and you've read this far, start here for concrete operating steps.

### 9.1 How do I find everything about a domain?
Path convention: **`DOMAINS/<domain>/01-research/`** (what we know) + **`DOMAINS/<domain>/02-outreach/`** (what we say), where `<domain>` is all-lowercase with the TLD (e.g. `DOMAINS/topsex.ai/`). The authoritative per-domain order of reading:
1. `01-research/leads_<domain>.md` — valuation + buyer categories + ranked DMPS leads (start here for context).
2. `01-research/contact-sheet_<domain>.md` (fall back to `contact_<domain>.md` if absent) — verified exec contacts.
3. `02-outreach/brief_<domain>.md` — the positioning/messaging brief.
4. `02-outreach/micro-messages_<domain>.md` — short one-liners.
5. `02-outreach/email-pack_<domain>.md` — canonical outreach sequences.

**Case-insensitive lookup** for the `leads_*` / `contact-sheet_*` filenames — uppercase stems exist (e.g. `leads_KnowLaw.ai.md`). Use `find -iname` or case-insensitive globbing, not exact names.

### 9.2 How do I read a contact sheet / confidence / §0 MISSING?
Each `contact-sheet_*.md` has:
- **§0 MISSING-CONTACTS SUMMARY** — a table of execs whose direct email/LinkedIn could NOT be H-verified; this is the owner follow-up list. **Never fabricate these.** They are consolidated in `docs/MISSING-CONTACT_2026-08-20.md`.
- **Confidence levels:** **H** = verified from a public page live this session (lowest risk); **M** = likely per company convention, not independently confirmed (format-inferred — MUST verify before send); **L** = best available / needs owner LLM verification. Only H addresses are send-ready without further checks; any M/L "format-inferred" address must be confirmed against a second source before delivery.

### 9.3 How do I consume `docs/outreach-contact-list-complete.csv`?
Columns: `#, Priority (P1/P2/P3), Batch, Name, Title, Company, Domain, LinkedIn, Email, Confidence, Motivation, Micro-Message, Has Message`.
- **Priority** ranks buyer importance (P1 = top; P2/P3 = follow). Filter by `Domain` for a domain, sort by `Priority` (P1 first), then `Confidence` (H over M/L) when deciding who to contact first.
- Use `LinkedIn`/`Email` only where `Confidence` is **H**. Addresses marked L or blank are not send-ready — route them through the owner list (§9.2) instead.
- **Cross-check against the contact sheet's §0 / `MISSING-CONTACT`** before any outreach, so you never send to an unverified address.
- The CSV is a **subset/tabular view** — the per-domain `contact-sheet_*.md` is the richer source (exec rationale, intent signals).

### 9.4 How do I run/derive outreach without violating content policy?
Sources for copy: `brief_*.md` (positioning/angle), `micro-messages_*.md` (short signal→bridge→ask), `email-pack_*.md` (full sequences), and the **Three-Line framework** (`docs/methodology/three-line-outreach-framework.md`). **Hard rules (from §7 policies):**
- **Pricing-free** — no dollar figures/price in any outbound copy. Pricing lives only behind "Internal Reference" markers in briefs.
- **No "I own"** — say "the premium domain X", never "I own X".
- **No links** in first-touch emails.
- **Body <100 words** (micro-messages are the 150–220-char ones, separate).
- **No invented emails/recipients** — only contact H-verified addresses; every claim must be traceable (public info, existing messages, or real tool output). Never imply a prior relationship that didn't happen.

### 9.5 Where is the live coverage truth?
**`ASSET_AUDIT_2026-08-14.md`** is the canonical coverage tracker (defined in §4). Do not re-derive coverage from scratch — read it. This REPO_INDEX is a *map* that points to it, not a duplicate. Where you suspect drift (e.g. B2/B3 deltas flagged in §1), verify with `grep`/`ls` against the filesystem and reconcile the audit.

### 9.6 What conventions steer outreach copy?
- **Three-Line framework** = signal → bridge → tiny ask, ≤250 chars, no pricing/links/"I own" (see §5).
- **`COMPANY/campaign-playbook.md`** = end-to-end campaign methodology (positioning, sequences, objection handling).
- **`docs/assets/ASSET_CHECKLIST.md`** = what "done" means for each asset type.

---

*This index is a living document. Update it when the repo structure changes, a new asset type lands, or a phase of the architecture roadmap is implemented. The canonical coverage numbers always live in `ASSET_AUDIT_2026-08-14.md` — this file points to it rather than duplicating it.*
