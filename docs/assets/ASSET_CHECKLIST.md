# TurnKeySold — Asset Completeness Checklist

**Version:** 1.0 · **Date:** 2026-08-12 · **Owner:** agent-lead (working doc — to be ratified)
**Scope:** Every domain in the portfolio must carry a defined set of sales assets. This checklist defines each asset type and the "complete" bar. It is used to audit all domains and to plan gap-filling work.

---

## Core Assets (owner-specified)

### A1. Appraisal / Valuation
**What:** Comparable-sales analysis, brandability score, estimated value range, anchor (asking) price.
**File:** `01-research/leads_<domain>.md` §1 (Comparable Sales, Brandability, Value Range)
**Complete when:** ≥4 comparables with prices/dates · brandability scored (e.g. /50) · value range + anchor price stated.
**Status:** ✅ 145/145 domains

### A2. Buyer Categories / Industry Targets
**What:** The distinct buyer categories (industries/personas) that could derive value from the domain, with rationale per category.
**File:** `01-research/leads_<domain>.md` §2 (Industry Targets)
**Complete when:** ≥3 named categories, each with a one-line strategic rationale.
**Status:** ✅ 145/145 domains

### A3. Specifically Identified Buyer Companies
**What:** Ranked table of real companies, scored (DMPS/BMS), with decision-maker, role, contact/channel, and intent signal per row.
**File:** `01-research/leads_<domain>.md` §3 (Lead List, Tier 1/2/3)
**Complete when:** Tier 1 (DMPS 80+) has ≥3 companies · every row names a decision-maker and role · intent signal present.
**Status:** ✅ 145/145 domains (Tier-1 depth varies — see A4/A5 for contact quality)

### A4. Executive Contact Information (verified)
**What:** Verified direct contact channels (email / LinkedIn / X / phone) for the top decision-makers; named "best executive to reach" per company; explicit list of what is still missing.
**Files:** `01-research/contact_<domain>.md` (verified contact sheet) + `01-research/<domain>-missing-contact-priority.md` (gaps)
**Complete when:** top-10 execs have verified channels · per-company best-exec noted · missing-contact list exists where gaps remain. **Never invent emails — flag M/L format-inferred explicitly.**
**Status:** ⚠️ Contact sheets: 3/145 (autopaga.com, nofail.ai, payauto.ai) · Missing-contact lists: 3/145 (apuesto.ad, gastropub.casino, hipotecahispana.com)

### A5. Outreach Messages (per company)
**What:** Personalized first-touch emails (and follow-up sequence) designed per specific company, pushing their motivation button — not generic templates.
**File:** `02-outreach/outreach-<domain>.md`
**Complete when:** ≥3 top leads have individual messages · each references a real, traceable signal about that company · follow-up sequence included.
**Status:** ❌ 7 domains (hipotecahispana.com, hispanoabogado.com, humanoreal.com, latinomedico.com, nobreak.ai, oneguy.org, pruebadehumanidad.com) + coldbeerportfolio

### A6. Micro-Messages (per company)
**What:** LinkedIn/X short messages (150–220 chars, Three-Line Framework) customized per company, pushing their motivation button.
**File:** `02-outreach/micro-messages_<domain>.md`
**Complete when:** ≥10 top leads each have a micro-message · each within char band · signals traceable · no pricing/links/"I own".
**Status:** ❌ 10 domains (agizent.com, aquexa.com, autopaga.com, lavoiture.ai, nofail.ai, payauto.ai, paybud.ai, payquick.ai, vivamucho.com, vivemucho.com)

---

## Supporting Assets (generated where campaigns are active)

### B1. Outreach Brief (per domain)
Pricing-free positioning brief: value proposition, persona targets, suggested angles, talking points. `02-outreach/brief_<domain>.md`
**Status:** ✅ 145/145 domains

### B2. Buyer Deep-Dives / Expansions
Expanded buyer universe beyond the initial list — additional qualified companies with named executives and triggers. `01-research/<domain>-buyer-expansion.md`
**Status:** ⚠️ 7 domains (hipotecahispana.com, hispanoabogado.com, infancia.ai, latinomedico.com, muyguay.com, oneguy.org ×2, roiboss.com)

### B3. Competitor / Google Ads Enrichment
Structured Google ad competitor + organic landscape data for the domain's category (embedded in leads file "Google Search Enrichment" section).
**Status:** ⚠️ 22 domains embedded (adult portfolio, keto/slimmeds portfolio, core domains, infancia.ai, automoviles.ai, apuesto.ai)

### B4. Monitoring Alerts
Google Alerts v2 per domain for buyer/intent signals.
**Status:** ⚠️ 127 domains covered (external, not in repo)

### B5. Verdict / Integration Docs
Verdict files from integrating external research (owner's LLM docs) — e.g. `verdict_domain_buyer_prospects.md`.
**Status:** ⚠️ 1 (7-domain doc); integration of 10-domains doc pending (backlog)

### B6. Deal Records & Buyer Intel
Post-sale records (e.g. `sale-record.md`, Trinity HealthCare intel for LeanMeds.com).
**Status:** ✅ 1 (LeanMeds.com sold)

---

## Coverage Summary (2026-08-12 audit)

| Asset | Coverage | Gap |
|---|---|---|
| A1 Appraisal | 145/145 | — |
| A2 Buyer categories | 145/145 | — |
| A3 Buyer companies + execs | 145/145 | depth varies |
| A4 Verified contacts | 3/145 | **142 domains** |
| A5 Outreach messages | 7/145 | **138 domains** |
| A6 Micro-messages | 10/145 | **135 domains** |
| B1 Briefs | 145/145 | — |
| B2 Expansions | 7/145 | 138 domains |
| B3 Google enrichment | 22/145 | 123 domains |
| B4 Alerts | 127/145 | 18 domains |
| B5 Verdicts | 1 | 1 pending (10-domains) |
| B6 Deal records | 1 | n/a |

**Portfolio size:** 145 domains + 1 portfolio folder (coldbeerportfolio) = 146 dirs in DOMAINS/.
**Core finding:** Research layer (A1–A3, B1) is complete for the entire portfolio. The execution layer (A4–A6) — verified contacts, per-company outreach messages and micro-messages — exists for only the actively campaigned domains. The gap is not knowledge; it is packaging contacts + messages per company at scale.
