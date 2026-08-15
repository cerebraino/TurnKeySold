# TurnKeySold — Repository Index (LLM & Human Onboarding)

> **Read this first.** This file is the single entry point to understand every asset in this repository, how the information is structured, and which guiding documents govern the work. It exists so a future LLM or team member can reach full context **without exploring 600+ files**.
>
> **Last updated:** 2026-08-15 · **Repo:** `cerebraino/TurnKeySold` · **Portfolio:** 145 domains + 1 bundle

---

## 1. What This Repository Is

TurnKeySold is an **agentic premium-domain sales operation**. This repository is its **single canonical source of truth** (see Principle P1) — it contains:

1. **Per-domain sales assets** — for 145+ domains, the full research-to-outreach pipeline: appraisals, buyer lead lists (DMPS-scored), verified executive contact sheets, outreach briefs, email packs, and micro-messages.
2. **Guiding documents** — the company's methodology, brand, playbooks, and the *decision/knowledge architecture* that defines how the organization thinks.
3. **Structured data** — CSVs of the full portfolio, domain values, Google Alert queries, and outreach contact lists.
4. **The website** — `WEBSITE/` (TurnKeySold.com source).

The **business model**: success-fee commission (20%) on domain sales. No upfront fees. The **founding bet**: if agents can systematically sell domains, they can sell anything.

---

## 2. The Mental Model (How to Think About This Repo)

The repository encodes one core loop (from `docs/architecture/KNOWLEDGE_MODEL.md`):

```
Source → Evidence → Hypothesis → Contact → Outcome → Learning → Pattern → Principle → Playbook
```

Every domain folder is a vertical slice of that loop, frozen at the "research → ready-to-outreach" stage. The **guiding documents** (`docs/`, `COMPANY/`) describe *how to keep running* the loop. The **CSVs** are the *queryable* projection of the narrative files.

**Key insight:** The repo is organized **per-domain** (content) + **cross-cutting** (governance + structured data). Do not look for a single "master file" — instead, learn the *file-type vocabulary* in §5, then navigate by type, not by browsing.

---

## 3. Top-Level Map

```
TurnKeySold/
├── README.md                      ← Older index (still useful; superseded by this file for detail)
├── REPO_INDEX.md                  ← THIS FILE — authoritative navigation
│
├── COMPANY/                       ← Brand + methodology (guiding docs)
│   ├── brand-identity.md          ← Brand guidelines, positioning, voice, tone
│   ├── campaign-playbook.md       ← Outreach campaign methodology (design framework)
│   ├── research-framework.md      ← Domain valuation + buyer research methodology (DMPS scoring)
│   ├── seller-onboarding.md       ← New client onboarding process
│   ├── website-brief.md           ← Original TurnKeySold.com requirements
│   └── website-final-copy.md      ← Final website copy & structure (what was built)
│
├── docs/                          ← Architecture, asset standards, methodology
│   ├── architecture/              ← HOW THE ORGANIZATION THINKS (see §4)
│   ├── assets/                    ← Asset completeness checklist + gap analysis
│   ├── methodology/               ← Three-Line outreach framework + messages
│   └── outreach-contact-list-*.csv/.md  ← Master exec contact lists (see §6)
│
├── DOMAINS/                       ← 146 per-domain packages (145 domains + 1 bundle)  ← CORE CONTENT
│   ├── CSV/                       ← Full-portfolio ranked CSV + micro-message drafts
│   └── [domain]/                  ← One folder per domain (lowercase, dot-included)
│       ├── 01-research/           ← Leads, valuations, contact sheets, expansions
│       └── 02-outreach/           ← Briefs, email packs, micro-messages, outreach
│
├── OUTREACH/                      ← Master outreach assets (email templates, old alert CSV)
├── PORTFOLIO/                     ← Portfolio-level analysis + appraisal CSVs
├── WEBSITE/                       ← TurnKeySold.com HTML/CSS (live site source)
├── contact-verification/          ← Batch contact-verification findings (2026-08-14)
│
└── (top-level CSVs, owner research docs, Genspark xlsx exports — see §6)
```

---

## 4. Guiding Documents (Read These to Understand "The Why")

### 4A. Architecture — *How the organization reasons* (`docs/architecture/`)

| File | Purpose | When to read |
|---|---|---|
| `KNOWLEDGE_MODEL.md` | The conceptual model: fundamental concepts (Organization, Person, Domain, Source, Evidence, Market) and derived concepts (Hypothesis, Opportunity, Contact, Learning, Pattern, Principle, Playbook, Bundle, Outcome, Campaign). Defines what knowledge must exist and how it compounds. | First, to understand the vocabulary |
| `DECISION_ARCHITECTURE.md` | How decisions are made: tactical/operational/strategic/constitutional tiers; three authority zones (Agent → Lead → Founder); confidence model; assumptions lifecycle; experiments; belief revision. | To understand *who decides what* |
| `ARCHITECTURE_PRINCIPLES.md` | **P1–P10** — the 10 non-negotiable principles governing all repo changes (canonical source, structured data, relationships, templates, provenance, naming, delete-vs-duplicate, git reversibility, lifecycle tracking, LLM navigation). **Ratified, founder-level.** | Before making *any* structural change |
| `METADATA_STANDARD.md` | The YAML-frontmatter provenance standard every knowledge artifact should carry (artifact_id, created_by, source, confidence, etc.). **Proposed** (not yet enforced). | When creating/editing research artifacts |
| `knowledge-architecture-review.md` | The Chief Knowledge Architect assessment: current gaps, entity model, proposed `_templates/`/`_data/`/`_indexes/`/`_playbooks/` restructuring, 5-phase roadmap. **Design doc, not yet implemented.** | To understand the *planned* target architecture |
| `phase1-preparation.md` | Pre-cleanup inventory + migration plan (what shared-vs-repo divergence looked like). Historical. | Context only |
| `phase1-report.md` | Phase 1 completion report (dedup, lowercase renaming, `v0.1-stable` tag). Historical. | Context only |

### 4B. Asset Standards (`docs/assets/`)

| File | Purpose |
|---|---|
| `ASSET_CHECKLIST.md` | Defines the "complete bar" for each asset type (A1–A6 core, B1–B6 supporting). The canonical reference for what a domain folder *should* contain. |
| `GAP_ANALYSIS_2026-08-12.md` | Mechanical gap scan (which domains lack which assets) + fill-the-gaps sequencing plan. |

### 4C. Methodology (`docs/methodology/` + top-level copies)

| File | Purpose |
|---|---|
| `three-line-outreach-framework.md` | The **Three-Line Framework** — the core cold-outreach methodology (signal → strategic bridge → tiny ask; ≤250 chars; no pricing, no "I own", no links). Authoritative. |
| `three-line-messages-36-domains.md` | Pre-written three-line messages for 36 domains. |

### 4D. Company (`COMPANY/`)

| File | Purpose |
|---|---|
| `brand-identity.md` | Brand guidelines, positioning ("Proactive vs. Passive"), voice ("boutique investment firm, not used car lot"). |
| `campaign-playbook.md` | Outreach campaign design framework. |
| `research-framework.md` | Domain valuation + buyer research methodology (the DMPS scoring system's home). |
| `seller-onboarding.md` | New client onboarding process. |
| `website-brief.md` / `website-final-copy.md` | Website requirements and final copy. |

---

## 5. Per-Domain Asset Vocabulary (The Heart of the Repo)

`DOMAINS/[domain]/` uses a **fixed subfolder + naming convention**. Learn these file types — they repeat across all 145 domains.

### Structure

```
DOMAINS/[domain]/                 e.g. DOMAINS/topsex.ai/
├── 01-research/                  ← WHAT WE KNOW (research layer)
│   ├── leads_[Domain].md         ← Primary lead list (ALWAYS present — the core file)
│   ├── contact-sheet_[Domain].md ← Verified exec contact sheet (present for ~75 domains)
│   ├── contact_[Domain].md       ← Older-format contact sheet (~20 domains)
│   ├── [domain]-buyer-expansion.md  ← Expanded buyer universe (optional, ~7-13 domains)
│   └── *-portfolio-*.md / *-buyers.md / *-intel.md  ← Cross-domain & corporate intel
│
└── 02-outreach/                  ← WHAT WE SAY (execution layer)
    ├── brief_[Domain].md         ← Outreach campaign brief (ALWAYS present)
    ├── email-pack_[Domain].md    ← Top-5 leads email pack: initial + Day 3/7/14 (~100 domains)
    ├── micro-messages_[Domain].md  ← 150-220 char LinkedIn/X messages (~27+ domains)
    └── outreach-[Domain].md      ← Personalized outreach messaging (~15 active-campaign domains)
```

### File-Type Reference (what each contains)

| Asset | Naming | Contains | Coverage |
|---|---|---|---|
| **Lead list** | `01-research/leads_[Domain].md` | §1 Domain valuation (comparables, brandability /50, value range, anchor) · §2 Industry targets/buyer categories · §3 ranked lead table (DMPS 0–100, company, decision-maker, role, intent signal) · Google Search Enrichment (top paid/organic competitors) on ~22 domains · owner-file review notes | 147 files / 145 domains (a few domains have 2 leads files, e.g. TopSex.ai + TopSex.ai-health) |
| **Outreach brief** | `02-outreach/brief_[Domain].md` | Domain overview · lead summary · messaging strategy · email/LinkedIn templates · objection handling · **internal pricing** (floor/target/ask — always behind a marker; never in outreach copy) | 146 files / 145 domains + coldbeerportfolio |
| **Email pack** | `02-outreach/email-pack_[Domain].md` | Top-5 leads, each with context, subject, email body, Day 3/7/14 follow-ups, "motivation button". Pricing-free, <100 words, no "I own" framing | 100 files |
| **Contact sheet** | `01-research/contact-sheet_[Domain].md` + `contact_[Domain].md` | Verified exec contact channels per company (email/LinkedIn/X), "best exec to reach", confidence levels (H/M/L), explicit missing-contact list | 95 total (75 `contact-sheet_` + 20 older-format `contact_`) |
| **Micro-messages** | `02-outreach/micro-messages_[Domain].md` | 150–220 char Three-Line messages per top-10 leads | 28 per-domain files; **full content for all 146 lives in the CSV** (`TurnKeySold_Full_Portfolio_Ranked.csv` col 5) + `DOMAINS/CSV/micro_messages_drafts.md` |
| **Personalized outreach** | `02-outreach/outreach-[Domain].md` | Deeper personalized first-touch + sequence for actively-campaigned domains | 26 files |
| **Buyer expansion** | `01-research/*-buyer-expansion.md`, `*-buyers.md` | 20–40+ additional buyer companies with named execs, verticals, acquisition rationale | 7+ file-based + 13 documented |

### The DMPS Scoring System

**Domain-Market-Prospect Score (0–100)** — how likely a company is to buy the domain.

| Range | Tier | Meaning |
|---|---|---|
| 90–100 | Hot | Direct category fit, high intent, budget likely |
| 70–89 | Warm | Adjacent category, growing into space |
| 50–69 | Lukewarm | Peripheral fit, speculative |
| <50 | Cold | Remote fit, unlikely without a trigger |

*(+10 bonus for companies already running paid ads on the domain's core keyword.)*

---

## 6. Structured Data & CSVs

The **queryable** projection of the narrative files. Read these instead of scanning 145 folders.

| File | Purpose | Columns / Notes |
|---|---|---|
| `DOMAINS/CSV/TurnKeySold_Full_Portfolio_Ranked.csv` | **THE master portfolio index.** All 146 rows ranked by value. | `Domain, Approx Defensible Market Value, Main 3 Buyer Categories, Top-3 Companies, Sample Micro-Message` |
| `DOMAINS/CSV/micro_messages_drafts.md` | Pre-split micro-message drafts (source of the per-domain micro-messages files). | — |
| `PORTFOLIO/full_appraisal.csv` | Full domain valuation spreadsheet. | — |
| `PORTFOLIO/domain-backlog-new.csv` + `domain-backlog-new.csv` (root) | 110 unprocessed domains (NameCheap portfolio). | Duplicate copies — see P7 |
| `PORTFOLIO/portfolio_analysis.md` | Cross-portfolio strategic analysis. | Narrative |
| `google_alerts_v2.csv` (root) + `OUTREACH/google_alerts.csv` | Google Alert buyer-signal queries. | v2 = 127 domains × 2-3 queries; OUTREACH copy = older 62-domain version |
| `NameCheap_Domain_List.csv` (root) | Original domain export. | Raw source |
| `docs/outreach-contact-list-complete.csv` / `-batch1.csv` / `-master.md` | Exec contact lists (verified emails/LinkedIn + micro-messages). | Master doc has H/M/L confidence + 20 execs |
| `OUTREACH/email-templates.md` | Reusable email frameworks. | Narrative |
| `OUTREACH/outreach-email-list.csv` / `prospect-emails.md` | Prospect contact + email strategy. | — |
| `contact-verification/batch*-findings-2026-08-14.txt` | Raw contact-verification findings (3 batches). | Working notes |

### Owner-Provided Research Inputs (top level)

| File | What it is |
|---|---|
| `Domain_Buyer_Prospecting_Research_10_Domains.md` | Owner's research on 10 priority domains (NoBreak, NoFail, Automovil, KnowLaw, PayCar, HipotecaHispana, HispanoAbogado, LatinoMedico, OneGuy, PossibleAGI) |
| `domain_buyer_prospects.md` + `verdict_domain_buyer_prospects.md` | Buyer prospects + the team's integration verdict |
| `coldbeer-portfolio-buyers.md` | Cold Beer portfolio (6 beer domains) buyer universe |
| `Three-Line_Framework_for_Premium_Domain_Outbound.md` | Top-level copy of the Three-Line methodology |
| `ASSET_AUDIT_2026-08-14.md` | Full-portfolio coverage audit (supersedes the 08-12 gap analysis) |
| `Executive_contact_...Genspark...xlsx`, `ViveMucho.com_...Genspark...xlsx`, `Je7mTksY.xlsx` | Genspark AI Sheets research exports (source data for leads) |

---

## 7. Domain Portfolios & Bundles

Domains are grouped into strategic portfolios. The per-domain files live in `DOMAINS/`, but the *grouping* is cross-cutting intelligence:

| Portfolio | Domains | Where documented |
|---|---|---|
| **Adult** (whorehouse.ai) | topsex.ai, whorehouse.ai, aisexshops.com, puticlub.ai, burdel.ai, putasexo.com, putero.ai, putero.online, puticlub.online | `DOMAINS/*/01-research` + `COMPANY` playbooks |
| **Weight Loss / Slim Meds** | buyslimmeds.com, bestslimmeds.com, cheapslimmeds.com, curebyketo.com, amoketo.com, tipsketo.com, bajapanza.com (+ LeanMeds.com SOLD) | leads + briefs + `slimmeds-brand-research.md` |
| **Cold Beer** | chelafria.com, chevefria.com, cervefria.com, birrafria.com, cervezahelada.com, umagelada.com | `DOMAINS/coldbeerportfolio/` + `coldbeer-portfolio-buyers.md` |
| **Apuesto Family** (7) | apuesto.ad/.ai/.casino/.xyz + teapuesto.bet/.casino/.xyz | `apuesto-family-bundle.md`, `apuesto-portfolio-buyers.md` |
| **Auto AI** | lavoiture.ai, automoviles.ai, automovil.ai, automoveis.ai, automovel.ai | `leads_LaVoiture.ai-quebec.md` |
| **Hispanic cluster** | hispanoabogado.com, hipotecahispana.com, latinomedico.com, oneguy.org, etc. | `*-buyer-expansion.md` files |
| **Core** | lavoiture.ai, knowlaw.ai, hispanoabogado.com, leanmeds.com | leads + briefs |

> **Sold:** `LeanMeds.com` (→ Trinity HealthCare Supply). See `DOMAINS/leanmeds.com/03-buyer-intel/trinity-healthcare-intel.md` + `03-results/sale-record.md`.

---

## 8. Status Snapshot (as of 2026-08-14)

From `ASSET_AUDIT_2026-08-14.md`:

| Layer | Coverage | Gap |
|---|---|---|
| Appraisal (A1) | 146/146 | — |
| Buyer categories (A2) | 146/146 | — |
| Buyer companies + execs (A3) | 146/146 | — |
| Verified contact sheets (A4) | ~95/146 | ~51 domains |
| Outreach email packs (A5) | 100/146 | ~46 domains |
| Micro-messages (A6) | 146/146 content (in CSV col 5) | only 28 per-domain `.md` files split so far |
| Outreach briefs (B1) | 145/146 | coldbeerportfolio (bundle) |
| Google ad enrichment (B2) | 22 embedded | in progress |
| Google Alerts (B3) | 127 domains | running/external |

**The research layer is complete; the execution layer (contacts + per-company messaging) is still being backfilled for the long tail.** See `docs/assets/GAP_ANALYSIS_2026-08-12.md` for the priority sequencing.

---

## 9. How to Do Common Tasks (LLM Navigation Recipes)

### "Show me everything about one domain"
1. `DOMAINS/[domain]/01-research/leads_[Domain].md` — valuation + leads
2. `DOMAINS/[domain]/02-outreach/brief_[Domain].md` — messaging + internal pricing
3. `DOMAINS/[domain]/01-research/contact-sheet_[Domain].md` — verified contacts (if present)
4. `DOMAINS/[domain]/02-outreach/email-pack_[Domain].md` — sendable emails (if present)

### "Rank all domains by value"
→ Read `DOMAINS/CSV/TurnKeySold_Full_Portfolio_Ranked.csv` (one file, 146 rows).

### "Which buyers haven't been contacted?"
→ There is **no outreach-log yet** (a known gap — see `knowledge-architecture-review.md` §Risk 4). The contact CSVs tell you *who to contact*, not *who was contacted*. Until `_data/outreach-log.json` exists, this must be inferred from git history or team channels.

### "What are the rules I must not violate?"
→ `docs/architecture/ARCHITECTURE_PRINCIPLES.md` (P1–P10).

### "How should I write a new lead list / brief?"
→ There are **no formal templates yet** (Phase 2 of the roadmap). Reverse-engineer from any existing file (e.g. `DOMAINS/topsex.ai/`), then check `docs/assets/ASSET_CHECKLIST.md` for the "complete" bar, and `docs/architecture/METADATA_STANDARD.md` for provenance.

### "I need to send outreach"
→ Use `email-pack_[Domain].md` / `micro-messages_[Domain].md` (pricing-free, Three-Line compliant). Follow `docs/methodology/three-line-outreach-framework.md`. **Never** include pricing in first contact (Principle: pricing-free).

---

## 10. Conventions & Gotchas (For Contributors)

1. **Single canonical source (P1):** the repo is authoritative. `/home/team/shared/` is an ephemeral workspace — never the permanent home of intelligence.
2. **Domain folder naming (P6):** lowercase, dot-included (`topsex.ai`, NOT `TopSex.ai`). Subfolders `01-research/` + `02-outreach/`.
3. **Pricing-free outreach:** dollar figures live only behind "Internal Reference" markers in briefs. Never in email/micro-message copy.
4. **Never invent contacts:** contact sheets flag "MISSING" for unverifiable execs; format-inferred emails are explicitly labeled, not asserted.
5. **Duplicates exist (known debt):** `domain-backlog-new.csv` (root + PORTFOLIO/), Google Alerts CSVs (root + OUTREACH/), some proof-of-human/outreach files appear twice. Per P7, prefer one canonical copy; do not add new duplicates.
6. **The target architecture (Phase 2+, not yet built):** `_templates/`, `_data/*.json`, `_indexes/`, `_playbooks/`, lowercase `domains/` + `research/`/`outreach/`/`history/` subfolders. See `knowledge-architecture-review.md`. Do **not** assume these exist yet — the current layout is `DOMAINS/` + `01-research/`/`02-outreach/`.

---

## 11. Where to Start (Suggested Reading Order)

1. This file (done).
2. `docs/architecture/ARCHITECTURE_PRINCIPLES.md` — the 10 rules.
3. `docs/architecture/KNOWLEDGE_MODEL.md` — the vocabulary.
4. `DOMAINS/CSV/TurnKeySold_Full_Portfolio_Ranked.csv` — the full portfolio at a glance.
5. One complete domain folder (e.g. `DOMAINS/topsex.ai/`) — see the asset types in action.
6. `docs/assets/ASSET_CHECKLIST.md` — what "done" means per asset.
7. `COMPANY/research-framework.md` + `docs/methodology/three-line-outreach-framework.md` — the how.

---

*This index is a living document. Update it when the repository structure changes, a new asset type is introduced, or a phase of the architecture roadmap lands.*
