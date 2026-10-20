# TurnKeySold — Repository Index (LLM & Human Onboarding)

> **Read this first.** This is the single canonical entry point to understand every asset in this repository, how the information is structured, and which guiding documents govern the work. A future LLM (or new team member) should be able to read **only this file** and reach full context — without exploring 600+ files.
>
> **Last updated:** 2026-09-21 · **Repo:** `cerebraino/TurnKeySold` · **Portfolio:** 145 domains + 1 bundle (coldbeerportfolio) = 146 dirs in `DOMAINS/` (plus the `DOMAINS/CSV/` data dir) · **main is current** — the latest merged wave is always visible at the bottom of §10 (wave log), so this pointer can never go stale
>
> **For LLMs:** see **[§9. LLM Usage Playbook](#9-llm-usage-playbook)** — how to actually do work against this repo.

---

## 0. Current State Snapshot (cold-start orientation — updated with the 2026-09-21 wave)

**What this repo is:** the complete research-to-outreach pipeline for a 146-domain premium domain portfolio (145 domains + 1 bundle), sold at a 20% success fee. All outreach copy is ready-to-fire but **FROZEN** — nothing is ever sent without the owner's explicit per-send instruction.

**Hot workstream — the payments family (13 owned domains):** payauto.ai · payquick.ai · paybud.ai · paycar.ai · paycarai.com · paybet.ai · paydeal.ai · jogpay.com · autopaga.com · pagacasa.com · pagatucasa.com · paguesucasa.com · suacasapaga.com. One ~31-company agentic-payments buyer system serves all thirteen. Research inputs: two external collaborator sets (PayAuto 19 companies, PayQuick 18) + an owner-commissioned contact map + team cross-fits. Verification state: PayAuto Tier-1 done (PR #73); PayQuick 18/18 graded (commit 6946838; citation-URL polish complete — PRs #82/#83); Tier-2/3 passes queued. Wave-1 first-touch packs are STAGED and HOLD-bannered (PRs #76/#84 — compliance pass merged; firing checklist in `docs/outreach/WAVE1-FIRING-CHECKLIST_2026-10-19.md`; firing-ready pending the owner's freeze-lift + per-send instructions). Own-research wave COMPLETE (commit 59685d6 — direct push to main, process deviation flagged; NOT a PR): master buyer CSV (`payments_family_buyers_master.csv`, 64 rows x 25 cols) + per-domain priority lists (`docs/PAYMENTS-FAMILY-PRIORITY_2026-09-21.md`) + 10 per-domain RESEARCH docs; exec re-sourcing for PENDING rows queued.

**Rules that bind every LLM working here (violations = rework):**
1. **SEND FREEZE** — research and prepare freely; NEVER send (no emails, no LinkedIn notes, no follow-ups) without the owner's explicit per-send instruction (§1, §7).
2. **Never-invent** — every factual claim needs a published source, URL recorded; only literally-published contacts are fireable (§9.7 defines the flag vocabulary).
3. **Multi-contact rule** — multiple contacts at the same company are PARALLEL outreach targets, not conflicts (verify each person's role independently).
4. **Full-field ingest** — external research is integrated field-by-field from the SOURCE FILE; summaries are maps, never the data.
5. **Index discipline** — every PR that adds/moves/changes artifacts carries its own `REPO_INDEX.md` update (Quick Reference row + §10 wave log) — see `WORKFLOW.md`.
6. **Live truth lives in data files** — coverage in `ASSET_AUDIT_2026-08-14.md` (§4); portfolio data in `PORTFOLIO/MASTER-DOMAIN-INVENTORY_2026-09-06.csv` (§6); verification evidence in the per-domain `PAY*-VERIFICATION-RESULTS_2026-09-21.md` docs. This index is the MAP, not the data.

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
| Google ad enrichment (B2) | embedded in `leads_<domain>.md` §"Google Search Enrichment" | **22 leads files** | — |
| Google Alerts (B3) | `google_alerts_v2.csv` | **127 domains** (audit); CSV now holds ~140 unique domains | — |
| **Master domain inventory** | `PORTFOLIO/MASTER-DOMAIN-INVENTORY_2026-09-06.csv` + `PORTFOLIO/build_master_inventory.py` | **146 rows × 13 cols** — full portfolio, machine-readable, regenerable via the script | CSV header (self-describing) |
| **Collaborator briefing** | `docs/COLLABORATOR-BRIEFING_TurnKeySold-Domains_2026-09-06.md` | Onboarding doc for external collaborator agents (system overview + integration path) | — |
| **Outreach tooling research** | `docs/OUTREACH-TOOLING-RESEARCH_2026-09-07.md` | Verified vendor prices/URLs ($0–$47/mo stack), UNVERIFIED flags, annual-billing traps | — |
| **Outreach tooling playbook** | `docs/OUTREACH-TOOLING-PLAYBOOK_2026-09-20.md` | Self-contained, action-ready: context → constraints → tools+signup URLs → phased sequence → $100 allocation → CTO.new operating-layer §7 → DO-NOT-BUY-YET → verification log | playbook §0–§11 structure |
| **Batch outreach archive** | `docs/outreach/` — `FIREABLE-OUTREACH_2026-08-30.md` (3-sent index) + `LINKEDIN-CONNECT-10_2026-09-04.md` + `LINKEDIN-CONNECT-10-BATCH2_2026-09-04.md` | **20 LinkedIn notes** (2 batches × 10) + 3-email sent index — all HOLD under freeze | — |
| **MuyGuay.com owner strategy (owner-authored, PRIORITY domain)** | root `MuyGuay_Strategy.txt` + `muyguay_contactos.xlsx` (owner originals) + `DOMAINS/muyguay.com/01-research/MUYGUAY-OWNER-STRATEGY-ES_2026-10-19.md` + `muyguay_owner_contact_map_61.csv` (canonical integration) | Owner's external research (branch cerebraino-patch-2, commit d2fe5b9): 3-layer Spain Gen Z buyer map (17 companies), 61 executive contacts with tactical roles + motivations + draft messages (only 4 public emails; zero invented — switchboards/LinkedIn routes), valuation ladder €8–15K central / €20–30K competing / €5K floor / €25K anchor, Afternic+Sedo exit plan. **Flags:** EXTERNAL-UNVERIFIED (fireable-gate pass queued) · pricing-in-first-touch conflict → owner ruling required · EUIPO/OEPM trademark check not yet done | owner originals are the authority (full-field standard) |
| **LaVoiture batch files** | `DOMAINS/lavoiture.ai/01-research/LAVOITURE-TOP10_2026-09-04.md` + `LAVOITURE-MTL-10_2026-09-05.md`; `02-outreach/LAVOITURE-MTL-10-MESSAGES_2026-09-05.md` | **10 FR-first Montreal messages** + TOP10 buyer lists — ready copy, HOLD | — |
| **PayAuto.ai acquisition targets (external collaborator research)** | root `payauto_ai_acquisition_targets.csv` (collaborator original, authoritative for contacts) + `DOMAINS/payauto.ai/01-research/payauto_ai_acquisition_targets.csv` (team verification workbench) + `PAYAUTO-EXTERNAL-RESEARCH-NOTE_2026-09-21.md` + `PAYAUTO-VERIFICATION-RESULTS_2026-09-21.md` | 19 companies × 13 cols original + 15-col team workbench (owner-audit FULL-FIELD ingest: every source column incl. 12 named individual contacts + 7 partnership-routed; motivations verbatim; Paybud_Crossfit + Team_Annotations columns). **Provenance:** external collaborator research; **Tier-1 (rows 1–8) team-verified as of PR #73** — 5 VERIFIED / 2 funding CORRECTED / 1 PARTIAL / 1 KILL (Nekuda dead, contact + funding unverifiable); Tier-2/3 (rows 9–19) remain EXTERNAL-UNVERIFIED pending second pass. Payman multi-contact maintained per owner directive | verification results doc `PAYAUTO-VERIFICATION-RESULTS_2026-09-21.md` (per-company detail + 8 follow-up flags) + note file |
| **Payments-family cross-fit (portfolio-wide)** | `docs/PAYMENTS-FAMILY-CROSSFIT_2026-09-21.md` | Live-site extract (paybud.ai landing page: 7 core + 4 ES/PT payment domains) cross-fit against the 19-buyer agentic-payments set — per-contact PRIMARY/secondary domain matrix (payauto ~16, payquick ~12, paybud 6, paydeal 3-4), 4 bundle plays, inventory grouping flags, paybot.ai ownership question | see doc §D for records to fix |
| **PayBud.ai cross-fit (vs PayAuto buyer set)** | `DOMAINS/paybud.ai/01-research/PAYBUD-CROSSFIT_2026-09-21.md` | **5 of 19 (Nekuda KILLED 2026-10-16 — 6→5)**; remaining fit: Payman ×2, Crossmint ×2, Natural, Catena, PayPal-P2P; verification reuse; inventory grouping flag (paybud under Betting/Gambling, research says budgeting) | family cross-fit doc has the portfolio-wide matrix |
| **PayQuick.ai external contact map (owner-commissioned)** | `DOMAINS/payquick.ai/01-research/PAYQUICK-CONTACT-MAP_2026-09-21.md` + `payquick_ai_contact_map.csv` | 10 of 18 companies: 12 named contacts (4 Tier-1 startups × 3 founders/execs), corporate routes for PayQuicker/Stripe/Mastercard/Visa, 2 Fragment candidates, Tempo founder to source; priority order SolvaPay→Causa Prima→GrailPay→Tensec→PayQuicker→megacaps. **TEAM-VERIFIED 2026-10-16 (commit 6946838):** Causa Prima founders VERIFIED (causaprima.com/about); GrailPay Messina CEO VERIFIED (Pulse 2.0), Jones/Bykov NOT-VERIFIED, **william@grailpay.com NOT-FIREABLE** (not literally published); SolvaPay founders NOT-VERIFIED (published FIREABLE contact@solvapay.com); Tensec founders NOT-VERIFIED (site bot-walled); Fragment candidates NOT-VERIFIED (fragment.so parked-for-sale); Tempo CEO NOT-VERIFIED ($500M/$5B funding VERIFIED) | results doc `PAYQUICK-VERIFICATION-RESULTS_2026-09-21.md` |
| **Wave-1 firing checklist (lead-compiled)** | `docs/outreach/WAVE1-FIRING-CHECKLIST_2026-10-19.md` (+ shared copy) | Gate + one-time pre-flight (sender identity, from-address, infrastructure) + 6-step per-message checklist + 13-target fireable-status/route/flags table + per-send log format. **B6 Fragment = DO-NOT-SEND** (site parked-for-sale) until re-verified. Compiled 2026-10-19 after the architect's compliance pass (PR #84) | pack route data (PR #84) |
| **PayAuto.ai wave-1 first-touch pack** | `DOMAINS/payauto.ai/02-outreach/PAYAUTO-WAVE1-FIRST-TOUCH_2026-09-21.md` (+ combined shared copy) | 7 ready-copy messages for verified Tier-1 targets (Natural, Payman ×2 parallel, Basis Theory company-level [Luce unverified], Catena, Crossmint, Paid, Skyfire) — HOLD-bannered under freeze; <100-word doctrine (74–89w verified 2026-10-16), no pricing, never-invent routes; owner-verbatim angle "Payments on autopilot" adopted as copy anchor; ES variants: none (rationale scan) | repo copies split from combined pack (PR #76); compliance pass (architect) |
| **PayQuick.ai wave-1 first-touch pack** | `DOMAINS/payquick.ai/02-outreach/PAYQUICK-WAVE1-FIRST-TOUCH_2026-09-21.md` (+ combined shared copy) | 6 ready-copy messages for Tier-1 targets (Causa Prima, GrailPay, SolvaPay, Tensec, PayQuicker defensive, Fragment) — greetings now VERIFIED-personal for Causa Prima (Maex Ament; Gebbing/Stanislaus parallel) + PARTIAL for GrailPay (Will Messina); company-level greetings stand for SolvaPay/Tensec/Fragment; **william@grailpay.com NOT-FIREABLE** (commit 6946838 gate failed — not literally published); Fragment flagged (fragment.so parked-for-sale); owner-verbatim angle "Speed wins. Get paid faster." as copy anchor; ES variants: none (rationale scan) | repo copies split from combined pack (PR #76); compliance pass (architect) |
| **PayQuick.ai acquisition targets (external collaborator research)** | root `payquick_ai_acquisition_targets.csv` + `DOMAINS/payquick.ai/01-research/payquick_ai_acquisition_targets.csv` (workbench) + `PAYQUICK-EXTERNAL-RESEARCH-NOTE_2026-09-21.md` | 18 companies (T1 ×6 incl. PayQuicker defensive angle; T2 ×6; T3 ×6) — agentic/instant-payments layer; **Verification COMPLETE 2026-10-16 (commit 6946838): 18/18 graded** — 2 RECONCILED (Causa Prima $30M; GrailPay $17.2M), 3 CORRECTED (Kite AI $18M, Skyfire $8.5M, Natural $30M+$10M), 1 RESOLVED (Payman $13M), Tempo $500M/$5B VERIFIED, 3 funding-NOT-VERIFIED (PayQuicker/JustPaid/Koywe); contacts verdicts in results doc + Contact_Name/Verification_Status columns | results doc `PAYQUICK-VERIFICATION-RESULTS_2026-09-21.md` (per-company evidence + fireable-status summary) |
| **Payments-family own research (all 13 domains)** | `DOMAINS/<domain>/01-research/*-RESEARCH_2026-09-21.md` x10 + root `payments_family_buyers_master.csv` + `docs/PAYMENTS-FAMILY-PRIORITY_2026-09-21.md` | Own buyer research for the 10 under-mapped domains (DMPS leads + owner positioning copy + verified external sets); master buyer CSV 64 rows x 25 cols (contacts+status, routes, P1/P2/P3, family rank, ESTIMATED $ willingness + basis, provenance); honest-fit flags (paybet thin, jogpay low-value, ES trio mortgage) | wave log commit 59685d6 (direct push, process deviation flagged) |

> **Source of truth:** all coverage numbers above live canonically in **`ASSET_AUDIT_2026-08-14.md`** (the live tracker updated as batches merge). This index points to it and records the *actual filesystem* counts verified 2026-08-27 — where the two differ (B2, B3, A4) the discrepancy is flagged below so the audit can be reconciled next.
>
> **Reconciliation notes (verified 2026-08-27):**
> - **A4** — audit says 146/146 ✓ confirmed on disk: 126 `contact-sheet_*.md` + 20 legacy `contact_*.md` = 146 files (100% of 146 domain dirs).
> - **A5** — audit says 145/146 ✓: 145 `email-pack_*.md` on disk; `leanmeds.com` is sold so it correctly has no pack. 26 legacy `outreach-*.md` coexist for flagship domains (see §3).
> - **A6** — audit says 147/147 ✓ confirmed (146 domains + coldbeerportfolio bundle).
> - **B2** — audit says 22; precise grep of `leads_*.md` for the "Google Search Enrichment" section header returns **22** ✓ (confirmed, matches audit).
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
| B2 Google ad enrichment | 22 leads files |
| B3 Google Alerts | 127 domains (CSV ≈ 140 unique) |

**The research + execution layers are now COMPLETE for all actionable assets.** A4 contact sheets and A5 email packs reached full/effectively-full coverage as of 2026-08-20 (A5 = 145/146, the last gap being the sold domain). Remaining work is maintenance/expansion, not backfill (see §8).

**Sold:** `LeanMeds.com` → Trinity HealthCare Supply (via Spaceship). Its dir still holds research assets for reference/process reuse.
**⏸️ SEND FREEZE (owner directive 2026-09-04 — still in effect):** NO emails or sends of any kind without the owner's explicit per-send instruction — no first-touches, no D3/D7/D14 follow-ups, no replies to inbound. All outreach copy in this repo is **ready-only** (research/prepare freely; never send). This supersedes any earlier "outreach is LIVE" framing.
**Sends to date (2026-09-03, pre-freeze):** **3 lifetime emails sent, 0 replies** — Zócalo Health (Erik Cardenas), Taskade (John Xie), Founder Institute (Adeo Ressi); provenance `docs/EXEC-CONTACT-RESEARCH_2026-08-31.md` rows 3/17/18; index `docs/outreach/FIREABLE-OUTREACH_2026-08-30.md`. Their D3/D7/D14 cadences are **PAUSED**; inbound replies (none yet) are surfaced to the owner before any response.
**Ready copy on hold (nothing sent since the freeze):** 4 expansion email packs (`docs/outreach-pack_{curebyketo.com,fusebot.ai,weputt.com,paretobuddy.com}.md`, ~19 fireable leads, PRs #48–#50) + **20 LinkedIn connect notes** (`docs/outreach/LINKEDIN-CONNECT-10*_2026-09-04.md`, 2 batches × 10) + **10 Montreal FR-first messages** (`DOMAINS/lavoiture.ai/02-outreach/LAVOITURE-MTL-10-MESSAGES_2026-09-05.md`).
**Earlier context kept current:** Scale run on 15 domains merged (PR #45: ~53–55 NEW vs ~197 baseline); superseded RUN-1 archived per owner directive (PR #46). Operational rules unchanged: never-invent, no autonomous sending, no pricing in first-touch copy.

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
├── PORTFOLIO/                     ← Portfolio analysis + appraisal CSVs + **`MASTER-DOMAIN-INVENTORY_2026-09-06.csv`** (146×13 full inventory + `build_master_inventory.py`)
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
- `docs/outreach/` — **Batch outreach archive**: `FIREABLE-OUTREACH_2026-08-30.md` (3-sent first-touch index), `LINKEDIN-CONNECT-10_2026-09-04.md` + `LINKEDIN-CONNECT-10-BATCH2_2026-09-04.md` (20 LinkedIn notes; ready-only under freeze)
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
- **`docs/COLLABORATOR-BRIEFING_TurnKeySold-Domains_2026-09-06.md`** — **reader-friendly system overview** for onboarding an external collaborator agent: business context, domains/portfolios, operating rules, integration path, where resources live. **Governance:** COLLABORATOR-BRIEFING is the *narrative* overview; **this REPO_INDEX.md remains the canonical file-level map** — when they drift, REPO_INDEX wins for file locations, the briefing wins for "how the business works".
- **`docs/OUTREACH-TOOLING-RESEARCH_2026-09-07.md`** — outreach tooling research: verified vendor prices/URLs ($0–$47/mo stack), UNVERIFIED flags, annual-billing traps. **`docs/OUTREACH-TOOLING-PLAYBOOK_2026-09-20.md`** — self-contained action-ready playbook (context → constraints → tools+signup URLs → phased sequence → $100 allocation → CTO.new operating layer §7 → DO-NOT-BUY-YET → verification log). Both indexed in the Quick Reference table above.
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
| `docs/PAYBUD-LANDING-PAGE-VERBATIM_2026-09-21.md` | **Owner's own landing-page positioning copy for the 7 core payment domains** (verbatim extract pasted by the owner) — the authoritative "Ideal for" buyer taxonomy; scoring standard for all payments-family fit work. The ES/PT "International" section is NOT in this paste (owner may supply later) |
| `payauto_ai_acquisition_targets.csv` (root) | **PayAuto.ai external collaborator research — canonical cleaned copy** (19×13; contacts authoritative). Team workbench + provenance note live in `DOMAINS/payauto.ai/01-research/`. ⚠️ EXTERNAL-UNVERIFIED until verification pass lands |
| `payquick_ai_acquisition_targets.csv` (root) | **PayQuick.ai external collaborator research — canonical copy** (18×10; Contact_Name + Verification_Status columns carry team verdicts + source refs). Workbench + note + **results doc** in `DOMAINS/payquick.ai/01-research/`. ✅ Verified 2026-10-16 (commit 6946838) |
| `payments_family_buyers_master.csv` (root) | **Payments-family master buyer CSV** (long format, 25 cols, 64 rows across 13 domains): domain_role, tier/category, build/fit/motivation, contact 1+2 name-title-status, route, P1/P2/P3, family_priority_rank, est_willingness low/high + price_basis (anchor x tier, ESTIMATES), provenance (DMPS/EXTERNAL/CONTACT-MAP/CROSSFIT/NEW), verification_status, source_urls, bundle_flag |
| `DOMAINS/CSV/TurnKeySold_Full_Portfolio_Ranked.csv` | **The value-ranked master portfolio index.** 146 rows, ranked by value. Cols: `Domain, Approx Defensible Market Value, Main 3 Buyer Categories, Top-3 Companies, Sample Micro-Message` |
| `DOMAINS/CSV/micro_messages_drafts.md` | Pre-split source of all micro-messages (per-domain files now complete — 147/147) |
| `docs/outreach-contact-list-complete.csv` | **Exec contact master.** Cols: `#, Priority (P1/P2/P3), Batch, Name, Title, Company, Domain, LinkedIn, Email, Confidence, Motivation, Micro-Message, Has Message` |
| `docs/outreach-contact-list-batch1.csv` | Batch-1 slice of the above (adds `Price`, `Twitter/X`, `Pitch Angle`) |
| `docs/outreach-contact-list-master.md` | **Contact-research master (owner lineage).** Compiled 2026-07-30 by the owner's executive-contact-research specialist; origin of the P1/P2/P3 prioritization that `outreach-contact-list-complete.csv` extends. Read for lineage/precedent; prefer `complete.csv` + per-domain contact sheets for current data. |
| `docs/OWNER-RESEARCH-PROMPT_2026-08-29.md` | **Reusable research prompt** the owner runs against an external agent to fill gaps in `docs/MISSING-CONTACT_2026-08-20.md`. Never-invent applies to its outputs: only literally-published contacts are fireable. |
| `docs/EXEC-CONTACT-RESEARCH_2026-08-31.md` | **Owner-supplied exec-contact research, pass 1** (external agent's own verification; treat as candidate-H until spot-validated). **Provenance source for the 3 fireable first-touch emails SENT 2026-09-03** — Zócalo Health / Taskade / Founder Institute (rows 3, 17, 18). |
| `docs/EXEC-CONTACT-RESEARCH-2ND_2026-08-30.md` | **Owner-supplied exec-contact research, pass 2** (10 high-potential contacts; folded into contact sheets + `MISSING-CONTACT` §E via PR #44). Aggregator-sourced rows (ContactOut/RocketReach) are NOT literally published — lower confidence, never fireable as-is. |
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
**PayAuto verification follow-ups (from PR #73 — tracked):**
- **Nekuda KILLED** (site dead, no Wayback; $5M + Ayal Karmi unverifiable) → ripple: PayBud cross-fit count drops 6→5 companies (remove Nekuda/Karmi row); family-doc references to Nekuda need the same sweep.
- **Skyfire funding CORRECTED to $8.5M seed** (not $9.5M/Coinbase/a16z) → sweep any family-doc/crossfit copy citing the old figure; DCVC mention in TC 2026-07-20 suggests a possible later round — follow up.
- **Basis Theory Colin Luce** title NOT verified (no public team page) — verify via LinkedIn/PR before any outreach naming him.
- **PayAuto Tier-2/3 rows 9–19** (Arcade, HappyRobot, Rye, ReFiBuy, Ramp, Brex, Visa, Mastercard, Stripe, PayPal, Coinbase) still EXTERNAL-UNVERIFIED — second verification pass queued.
- **Natural funding conflict resolved:** $30M Series A (Forerunner) + $10M seed verified; PayQuick-set's $9.8M figure should be reconciled in the PayQuick verification pass.
- Nekuda Wayback CDX was intermittently offline — retry archive check when stable.

**2026-09-21 wave items (payments family — added by owner directive):**
- **Verification passes:** PayAuto Tier-1 COMPLETE (task 1ba44884, PR #73) + **PayQuick COMPLETE (task 45a948e2, commit 6946838 — 18/18 graded)**. FIREABLE published contacts now: contact@solvapay.com, Contact@/Sales@UNIPaaS.com, Causa Prima via site-form/LinkedIn (founders verified), Eynat Guez (Papaya). **NOT-FIREABLE: william@grailpay.com** (gate failed). Follow-ups: Kite AI CEO name (TheStreet body), LinkedIn gates (GrailPay Jones/Bykov, SolvaPay founders, Tensec founders, Fragment candidates), official-domain confirmations (Fragment/Koywe/Tensec), titles (Anelya Grant, David Avgi), PayAuto Tier-2/3 second pass (queued). Wave-1 pack (#76) HOLD-bannered under freeze — owner per-send instruction still the gate.

- **Payments-family own research COMPLETE (task 6e8dcea2, commit 59685d6 — direct push, process deviation flagged):** 10 domains researched + master buyer CSV + priority doc; follow-ups: exec re-sourcing for PENDING-EXTERNAL rows (LinkedIn/site), wave-1 copy enrichment per domain, owner freeze-lift decision
- **Owner confirmations pending:** paybot.ai ownership (absent from inventory + site + NameCheap list); SuaCasaPaga.com exact spelling in inventory.
- **Inventory regrouping (next `build_master_inventory.py` build):** paybud.ai Betting/Gambling → budgeting/agent-wallet; autopaga/pagacasa/pagatucasa Real Estate/Mortgage → Payments (site sells them as payments); paybot.ai to be added if owned.
- **Site polish:** paybud.ai landing page nav/meta says "Six Names" vs H1 "Seven Premium Domains" — stale count.
- **Owner resolves `docs/MISSING-CONTACT_2026-08-20.md`** — the outstanding exec contacts (Section A priority: NoBreak Security/Yuval Olsha, Supreme CASA CEO, Zócalo Health/Erik Cardenas, Kavak/Carlos García Ottati, KnowLaw AI founder; Section B: PR #35 domains). This is the main open owner-side item.
- **Reconcile `ASSET_AUDIT_2026-08-14.md`** with the 2026-08-27 deltas (B2 confirmed 22 ✓; B3 CSV grew ~127→~140 unique domain tokens). The audit filename still says 2026-08-14 though its numbers were updated through 2026-08-20 — consider bumping the date/version.
- **Migrate lingering legacy files** to canonical names (`contact_`→`contact-sheet_` for the 20, `outreach-`→`email-pack_` for the 26) if the team wants single-namespace consistency (not required — both are readable).
- **New-buyer contact-sheet expansions** as new Tier-1 buyers surface (pattern established in `verdict_10domains_integration.md`).
- **Long-term (Phase 2+, not yet built):** `_templates/`, `_data/*.json`, `_indexes/`, `_playbooks/` restructuring (see `docs/architecture/knowledge-architecture-review.md`). **Do not** assume these exist yet.

---

## 9. LLM Usage Playbook

This section tells a connected LLM *how to actually do work* against this repo. If you're an LLM and you've read this far, start here for concrete operating steps.

### 9.0 Start-here reading path for a NEW LLM / collaborator agent
Read in this order — each step is self-contained, and each points to the next:
1. **`REPO_INDEX.md`** (this file) — the canonical file-level map you are reading now.
2. **`docs/COLLABORATOR-BRIEFING_TurnKeySold-Domains_2026-09-06.md`** — system overview + integration path (business context, operating rules, where things live — the narrative companion to this map).
3. **`docs/OUTREACH-TOOLING-PLAYBOOK_2026-09-20.md`** — the outreach tooling stack + phased spend sequence + how the CTO.new platform works in tandem with those tools (§7 of the playbook).
4. **`PORTFOLIO/MASTER-DOMAIN-INVENTORY_2026-09-06.csv`** — the full 146-domain inventory in machine-readable form (13 columns: value ranges, buyer categories, top buyers with DMPS, sample micro-message).
5. **For the active payments-family workstream (13 domains, in progress):** `DOMAINS/payauto.ai/01-research/PAYAUTO-VERIFICATION-RESULTS_2026-09-21.md` + `DOMAINS/payquick.ai/01-research/PAYQUICK-VERIFICATION-RESULTS_2026-09-21.md` (verification evidence) → `DOMAINS/payquick.ai/01-research/PAYQUICK-CONTACT-MAP_2026-09-21.md` (contacts + priority order) → `docs/PAYMENTS-FAMILY-CROSSFIT_2026-09-21.md` (per-contact domain matrix) → `docs/PAYBUD-LANDING-PAGE-VERBATIM_2026-09-21.md` (owner's own positioning = the fit standard) → wave-1 packs in `DOMAINS/pay{auto,quick}.ai/02-outreach/` (HOLD-bannered). Flag meanings: §9.7.
**⏸️ Freeze rule (applies to every workstream):** you may **research and prepare** freely, but you may **NEVER send** — no emails, no LinkedIn notes, no follow-ups of any kind — until the owner gives an explicit per-send instruction. Treat every draft in this repo as ready-only.

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

## 10. Outbound-Lead-Research Methodology & Reports
- **`docs/domain-outbound-lead-researcher.md`** — the owner-supplied outbound buyer-identification methodology (exact-match > sibling-TLD > use-case > timing prioritization; qualification gate; scoring tiers; provenance/never-invent rules). Read before running any outbound-lead-research task.
- **`docs/OUTBOUND-PILOT_8DOMAINS_2026-08-30.md`** — pilot validation of the methodology on 8 top-25% domains (29 NEW surfaced / 28 live-verified). Baseline that justified scaling.
- **`docs/OUTBOUND-SCALE-15DOMAINS_2026-08-30.md`** — owner-approved scale-up: NEW-lead report across the authoritative 15 top-25% domains (~53–55 NEW, live-verified). Self-contained methodology + per-domain tables + yield summary + constraints + recommendations.
- **`docs/CONTACT-RESEARCH-LIST_15DOMAINS_2026-08-30.md`** — flat contact-research list (domain / company / website / category / tier / confidence / contact-research hints) for the owner's contact-research agent to find decision-makers & verified paths. No emails — every row traces to the scale report.
- **`docs/OUTBOUND-SCALE-RUN1-WRONGSET_2026-08-30.md`** — ARCHIVED run-1 scale-up report (mis-specified domain set: 6 re-piloted + 15 self-selected; 9 priority domains missing). Preserved per owner directive for lead value (BNPL, adult-creator, kids-ed, payments leads remain valid NEW targets for their own domains). NOT the active deliverable.
- **`docs/CONTACT-RESEARCH-LIST-RUN1-WRONGSET_2026-08-30.md`** — ARCHIVED run-1 flat contact-research list (traces to the run-1 report above; no emails; every row follows never-invent).
- **`docs/SCALE-FOLLOWUP_2026-09-03.md`** — phase-1 expansion follow-up: WAF-flag re-verification (curl + real-browser) + contact paths for NEW leads on the 4 expansion domains (fireable = literally published w/ source URL; 2 invalid-lead flags).
- **`docs/outreach-pack_curebyketo.com.md`, `outreach-pack_fusebot.ai.md`, `outreach-pack_weputt.com.md`, `outreach-pack_paretobuddy.com.md`** — phase-2 expansion email packs (2026-09-04): drafts for the ~19 fireable NEW leads + DM/form strategy notes, D3/D7/D14 cadences, exclusions documented (Ketoned Bodies, Routine). DRAFTS — nothing sent; firing requires lead/owner sign-off.

### Post-Sep-3 merge waves (PRs #51–#77) — repo state evolution after the freeze
- **PR #51** — LaVoiture.ai contact sheets: 5 sourced CEO-change corrections (Filosa, Provost, Debrue, Swan, Charli/Einride).
- **PR #52** — stale-exec row fixes from sourced research: PagerDuty CEO → John DiLullo (nofail/nobreak leads), Stripchat CEO → Breeze Dennis (burdel leads).
- **PR #53** — LaVoiture batch files: TOP-10 + Montreal round-2 buyer lists and 10 FR-first outreach messages (paths in §3 / Quick Reference).
- **PR #54** — batch outreach archive: LinkedIn connect-note batches 1–2 (20 notes) + FIREABLE-OUTREACH index into `docs/outreach/`.
- **PR #55** — `docs/COLLABORATOR-BRIEFING_TurnKeySold-Domains_2026-09-06.md` (collaborator onboarding; see §5).
- **PR #56** — `PORTFOLIO/MASTER-DOMAIN-INVENTORY_2026-09-06.csv` + `build_master_inventory.py` (146 × 13; see Quick Reference).
- **PR #57** — `docs/OUTREACH-TOOLING-RESEARCH_2026-09-07.md` (tooling research; see §5/§6).
- **PR #58** — `docs/OUTREACH-TOOLING-PLAYBOOK_2026-09-20.md` (self-contained playbook incl. CTO.new operating-layer §7).
- **PR #59 + #60** — REPO_INDEX.md modernization: freeze state superseding "outreach is LIVE", 3-sends/0-replies record, six-class Quick Reference, §9.0 start-here path for new LLM/collaborator agents.
- **PR #61** — `DOMAINS/aikillswitch.org/01-research/AIKILLSWITCH-BUYERS_2026-09-21.md`: refreshed + expanded verified buyer list (3 placeholders filled, 4 leadership changes caught incl. Open Philanthropy→Coefficient Giving rebrand, 2 leads honestly killed, 18 new orgs probed).
- **PR #62** — payauto.ai external collaborator research integrated: root original CSV (19×13, authoritative for contacts) + DOMAINS workbench + provenance note (EXTERNAL-UNVERIFIED; Payman multi-contact flagged per owner directive).
- **PR #63** — owner multi-contact directive applied: same-company contacts = parallel targets, not conflicts; Payman Bicakcic + Farman-Farmaian reframed as multi-threading.
- **PR #64** — owner-supplied cleaned CSV export ingested as canonical root payauto file (content identical, comma-free parse-safe; old version in history).
- **PR #65** — paybud.ai cross-fit analysis vs PayAuto target set (6 of 19 companies also fit PayBud) + payments-family portfolio view + inventory grouping flag.
- **PR #66 + #67** — owner-audit full-field ingest: PayAuto workbench rebuilt carrying ALL 13 source columns × 19 rows (contacts incl. Sarhangi/Salazar/Palafox/Bhargava/Wingo + Rawitz secondary; motivations verbatim) + Paybud_Crossfit + Team_Annotations; 12 named contacts + 7 partnership-routed verified.
- **PR #68** — payments-family portfolio-wide cross-fit: live paybud.ai landing-page extract (11 payment domains) vs the buyer set; per-contact PRIMARY/secondary matrix; 4 bundle plays; inventory grouping flags; paybot.ai ownership question.
- **PR #69** — payquick.ai external research integrated: 18-company agentic/instant-payments buyer set (12 new to family, 6 shared with PayAuto); root CSV + workbench + note; outreach doctrine updated in family cross-fit; verification queued behind PayAuto pass.
- **PR #73** — PayAuto Tier-1 external-research verification COMPLETE (task 1ba44884): rows 1–8 graded with 15 published source URLs — 5 VERIFIED (Natural $30M Series A Forerunner + Lalji CEO; Payman $13M + Bicakcic Co-Founder & CEO [conflict resolved, Teymour kept as parallel target]; Catena $30M Series A + Neville CEO; Crossmint $23.6M + Touza; Paid $21.6M/$33.3M + Medina CEO; Skyfire $8.5M seed CORRECTED from $9.5M + Sarhangi CEO via skyfire.xyz); Basis Theory $33M raise PARTIAL (Luce NOT verified — LinkedIn follow-up); Nekuda KILLED (site dead). New per-company doc + workbench/leads/contact updates. Tier-2/3 rows 9–19 remain EXTERNAL-UNVERIFIED (second pass queued).
- **PR #74** — payquick.ai external contact map integrated (owner-commissioned): 12 named contacts across the 4 Tier-1 startups + corporate routes for PayQuicker/megacaps + 2 Fragment candidates; verbatim authority copy + machine-readable CSV + workbench pointers + verification-pass scope update; priority order + <100-word outreach guidance adopted.
- **PR #76** — wave-1 first-touch copy packs (13 messages: PayAuto ×7, PayQuick ×6) authored by outreach-architect, HOLD-bannered ready-copy; repo placement + index rows applied by lead after the architect's rework pass did not land (md5-identical resubmission).
- **Commit 6946838** (direct push to main — process deviation flagged in review feedback; NOT a PR) — PayQuick external-research verification COMPLETE (task 45a948e2): **18/18 rows graded** — RECONCILED Causa Prima $30M ($10M pre-seed Creandum + $20M seed Base10) + GrailPay $17.2M ($6.7M + $10.5M Series A) · CORRECTED Kite AI $18M PayPal+GC (Fortune), Skyfire $8.5M seed, Natural $30M Series A Forerunner + $10M seed ($9.8M stale) · RESOLVED Payman $13M total (Coinbase Ventures unverified) · Tempo $500M/$5B VERIFIED (Fortune exclusive) · funding-NOT-VERIFIED PayQuicker/JustPaid/Koywe. Contacts: Causa Prima founders VERIFIED (causaprima.com/about, Taulia-SAP verbatim) · GrailPay Messina CEO VERIFIED (Pulse 2.0) + **william@grailpay.com NOT-FIREABLE** · Papaya Eynat Guez VERIFIED (Forbes) · JustPaid Anelya Grant + UNIPaaS David Avgi PARTIAL · SolvaPay/Tensec/Fragment/Tempo/Kite CEOs NOT-VERIFIED (flagged w/ next steps). Ripple: Nekuda removed from PayBud cross-fit (6→5), Skyfire $8.5M + skyfire.xyz swept into family docs, Tempo mark verified. REPO_INDEX updated in-PR (standing rule). Files: `PAYQUICK-VERIFICATION-RESULTS_2026-09-21.md` + workbench/root CSV verification columns + contact-map statuses.
- **PR #81 (this PR)** — lead label-precision pass on the own-research wave: researcher's commit 59685d6 was mislabeled "PR #81" across the index (3 spots) + paybet research doc ("PayQuick PR #77" → commit 6946838); process deviation (second direct-to-main push) flagged in task feedback; PayQuick citation-URL fix (task 45a948e2) remains outstanding and now gates the freeze-lift decision.
- **PR #83 (this PR)** — PayQuick citation-URL polish COMPLETE (task 45a948e2, PR #82): every claim in PAYQUICK-VERIFICATION-RESULTS now carries a literal published source URL (PayAuto 15-URL standard met) + URL columns added to workbench/contact-map/root CSVs; delivered via branch→PR (process compliance restored). Index wave-log entry applied by lead (researcher omitted it from PR #82). **The PayQuick citation-polish gate for the owner's wave-1 freeze-lift decision is now CLOSED — wave-1 firing readiness depends only on the architect's no-pressure-close standardization + firing checklist (task f18d4c0f).**
- **PR #77 (this PR)** — comprehensive-readability pass (owner directive): new §0 cold-start snapshot; §9.7 verification/provenance flag vocabulary (EXTERNAL-UNVERIFIED/VERIFIED/RECONCILED/CORRECTED/PARTIAL/NOT-VERIFIED/KILL/FIREABLE/corporate-route); §9.0 payments-family reading path; wave-log duplicate PR #69 line removed + section title corrected to #51–#77; `docs/PAYBUD-LANDING-PAGE-VERBATIM_2026-09-21.md` added to repo (was shared-only); README.md staleness fixed (now points here).
- **Compliance pass (architect, wave-1 packs, 2026-10-16; on `feat/wave1-first-touch-copy-compliance`)** — both wave-1 first-touch packs updated against the merged verification (commit 6946838): (1) **owner-verbatim positioning anchors adopted** — PayAuto "Payments on autopilot — set it, forget it, never miss.", PayQuick "Speed wins. Get paid faster." (from `docs/PAYBUD-LANDING-PAGE-VERBATIM_2026-09-21.md`); (2) **PayQuick greetings verification-gated** — personalized only for VERIFIED contacts (B1 Maex Ament + Gebbing/Stanislaus parallel; B2 Will Messina), company-level for NOT-VERIFIED (SolvaPay/Tensec/Fragment); (3) **`william@grailpay.com` NOT-FIREABLE** removed from routes; (4) **SolvaPay `contact@solvapay.com` FIREABLE** (site footer) adopted as first-choice route; (5) **Fragment flagged** (fragment.so parked-for-sale — verify before any send); (6) **Crossmint Rawitz NOT-VERIFIED** (never-invent: not named in copy); (7) **Basis Theory Luce title still unverified** — company-level held; (8) **ES-variant decision documented in both packs** ("none — rationale scan"); (9) QA sweep re-verified by script: all 13 bodies 72–89w, no pricing tokens, opt-out in all. Shared copies md5-verified vs repo. REPO_INDEX rows 50–51 updated in-PR. Push + PR pending GitHub credential refresh.

- **PR #81** — payments-family OWN RESEARCH wave COMPLETE (task 6e8dcea2): 10 under-mapped domains researched — paycar.ai, paycarai.com, paybet.ai, paydeal.ai, jogpay.com, autopaga.com, pagacasa.com, pagatucasa.com, paguesucasa.com, suacasapaga.com — per-domain `*-RESEARCH_2026-09-21.md` (DMPS leads + owner positioning copy PAYBUD-LANDING-PAGE-VERBATIM + verified external sets PR #73/commit 6946838; exec names w/ status; honest-fit flags: paybet thin agentic overlap, jogpay low-value fitness, ES trio mortgage). Consolidated root **`payments_family_buyers_master.csv`** (long format 25 cols, 64 rows): domain_role, contacts+status, routes, P1/P2/P3, family priority rank, ESTIMATED willingness-to-pay (anchor x affordability tier, basis stated), provenance (DMPS/EXTERNAL/CONTACT-MAP/CROSSFIT/NEW), verification_status, source refs, bundle flags. `docs/PAYMENTS-FAMILY-PRIORITY_2026-09-21.md`: per-domain P1/P2/P3 + family top-25. Family cross-fit docs UPDATE 4 (paydeal/autopaga cross-fits incl. ReFiBuy/Paid/Skyfire/Stripe/Causa Prima; ES/PT + suacasapaga share ES-mortgage pool; quitesuacasa.com sibling noted). REPO_INDEX rows + wave log in-PR (standing rule). Freeze honored — research only, no sends.
- **PR <this-PR>** — PayAuto Tier-2/3 second verification pass COMPLETE (task eb45d140, this PR): rows 9–19 graded — Tier-2 VERIFIED ×4 (Arcade.dev $60M Series A + prior $12M headline-verified [Business Wire/WSJ/TC via GN] with '$72M total' marked inferred-sum + SYN/MS/Wipro investor names NOT confirmed; HappyRobot $150M Series C @ $1.2B [company blog + PYMNTS URL]; Rye $14M a16z [CoinDesk headline; identity resolved — Justin Kan co-founder on rye.com/about]; ReFiBuy $13.6M seed [Axios/Hypepotamus headlines]) · Tier-3 CORRECTED ×2 (Ramp valuation path $32B→$44B→$60B [TC + PYMNTS URLs; '$700M raise' = revenue figure, NOT-VERIFIED; IPO prep NOT-VERIFIED]; Stripe '~$90B+' → $159B post-tender [CNBC/Yahoo headlines]) · corporate-route existence/program VERIFIED (Brex; Visa Intelligent Commerce [PRN URL]; Mastercard agentic [PYMNTS URL; 'Agent Pay/Start Path' = internal notes]; PayPal; Coinbase x402 [PYMNTS ×2 URLs]; coinbase.com 403 bot-wall noted) · PR #73 follow-ups RESOLVED: Basis Theory Colin Luce = 'Co-Founder and CEO' verbatim in PR Newswire Crossmint release (URL; A3 greeting may now personalize — architect call); Skyfire DCVC line VERIFIED (TC 2026-07-20 Natural article verbatim; no new round amount published — keep $8.5M seed); Nekuda Wayback CDX retried → no snapshots, KILL confirmed. Known quirks flagged: workbench rows 1/3/6/7 pre-existing unescaped-quote malformation (cleanup recommended); root payauto CSV still pre-verification snapshot (Payman $13.8M stale).
### 9.7 Verification & provenance flag vocabulary (used across workbenches, CSVs, and results docs)
| Flag | Meaning | Action for an LLM |
|---|---|---|
| `EXTERNAL-UNVERIFIED` | Produced by an external LLM/collaborator; team has NOT confirmed | Treat as candidate data; do not build outreach on it until verified |
| `VERIFIED` | Confirmed against a published source, URL recorded | Safe to use for research/copy (still never send) |
| `RECONCILED` | Two research sets disagreed; a verified figure subsumes both | Use the reconciled figure only |
| `CORRECTED` | A published source CONTRADICTS the collaborator claim | Use the corrected figure; never quote the old one |
| `PARTIAL` | Name/company published; exact title/role still unconfirmed | Usable in copy WITHOUT personalizing the title; verify before send |
| `NOT-VERIFIED` | No accessible published source; next steps flagged | Do not use in outreach; may continue research |
| `KILL` | Company/contact defunct (dead site, parked domain, no archive) | Remove from active lists; keep the row for the record |
| `FIREABLE` / `NOT-FIREABLE` | The owner's literal-publication gate for CONTACTS: an address is fireable ONLY if it appears verbatim on an official channel (URL recorded) | `NOT-FIREABLE` = never send to it, no matter how plausible |
| `corporate-route` | Megacap / no-named-exec rows: approach via brand/corp-dev/site-form | Never route through sales; strategic domain brief, long cycle |
- **PR #85 (this PR)** — wave-1 firing checklist (lead-compiled, task f18d4c0f completion): the architect's compliance pass itself merged as PR #84 (push recovered by lead — member's platform token expired mid-loop; finish_task hit platform errors); greetings verification-aligned (VERIFIED personalized, NOT-VERIFIED company-level), NOT-FIREABLE routes stripped, no-pressure closes on all 13; the checklist (gate + pre-flight + per-message steps + 13-target status table + per-send log) was completed by the lead from the packs' route data per the established lead-completion pattern. **Wave-1 is now FULLY FIRING-READY pending only the owner's freeze-lift + per-send instructions.**
- **Owner strategy branch merged (cerebraino-patch-2, commit d2fe5b9 — owner-authored) + integration PR (this PR):** MuyGuay.com owner strategy integrated per full-field standard — verbatim canonical copy + 61-contact machine-readable CSV + leads-file UPDATE (buyer map, valuation ladder, 3 honest conflict flags incl. pricing-in-first-touch → owner ruling) + Quick Reference row. Verification pass on the 61 contacts queued (backlog, after eb45d140).
