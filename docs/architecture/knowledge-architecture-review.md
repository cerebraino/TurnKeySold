# TurnKeySold — Knowledge Architecture Review

**Chief Knowledge Architect Assessment**
Date: July 2026
Reviewer: agent-lead acting as CKA
Scope: Full repository audit for long-term organizational intelligence

---

## 1. Executive Assessment

The current repository is a **prototype that succeeded**. It was built for speed — generate leads, write briefs, move fast. That was correct for phase one. But it is not suitable as permanent organizational memory.

### What's working
- The per-domain `01-research/` / `02-outreach/` pattern is intuitively correct
- Lead lists and briefs are consistently produced with high quality
- The README is genuinely useful for LLM navigation
- Google Alerts CSV and domain inventory are valuable structured artifacts
- The Cold Beer Portfolio and buyer expansion documents represent our deepest strategic thinking

### What's failing
- There is no single source of truth — `/home/team/shared` (288 files) and the repo diverge
- Knowledge is trapped in narrative markdown that cannot be queried, compared, or reused
- Relationships between domains (bundles, families, same buyer across domains) are invisible
- Duplicate files, empty folders, and naming inconsistencies are accumulating
- There is no way to answer "which buyers should we contact this week?" without reading 130 files
- The architecture has no opinion about what knowledge should persist vs. what's ephemeral

**Repository Health Score: 42/100**

| Dimension | Score | Notes |
|---|---|---|
| Structure clarity | 55/100 | Per-domain pattern works, but top-level organization is ad-hoc |
| Naming consistency | 35/100 | Mixed case, inconsistent suffixes, duplicate old formats |
| Single source of truth | 25/100 | Shared directory vs. repo diverge; sandbox recovery proved fragility |
| Queryability | 10/100 | All narrative markdown — no structured data access |
| Relationship modeling | 5/100 | No cross-domain links, no buyer-domain matrix |
| Maintainability | 40/100 | Adding a domain is easy; updating 130 domains is not |
| LLM navigability | 60/100 | README helps, but scale will break this |
| Human navigability | 35/100 | 132 domain folders with inconsistent naming |
| Reusability | 30/100 | Copy-paste is the only reuse mechanism |

---

## 2. Biggest Risks

### Risk 1: Knowledge Fragility (CRITICAL)
The `/home/team/shared` directory is the actual working memory of the company — but it's ephemeral. Sandbox recovery already lost files once. The repo is a lagging copy, not the source of truth. If the sandbox is reset, **288 files of generated intelligence disappear**.

### Risk 2: Scale Breaks Navigation (HIGH)
At 132 domain folders and growing, a human cannot browse. An LLM cannot read 130 files per query. We've already hit the point where "what's the status of everything?" requires a summary document rather than direct inquiry. This will only worsen.

### Risk 3: Knowledge Silos (HIGH)
Cold Beer Portfolio intelligence is in `DOMAINS/ColdBeerPortfolio/`. Proof of Human intelligence is duplicated in two domain folders. The apuesto family (7 domains) has no central index. When a buyer like AB InBev is relevant to both Cold Beer AND apuesto, there's no way to surface this.

### Risk 4: No Contact/Status Tracking (HIGH)
We have 300+ companies, 100+ named executives, 35+ personalized outreach messages — and no record of who was contacted, when, or what happened. Every future attempt will start from zero.

### Risk 5: Duplicate Decay (MEDIUM)
20 `leads.md` files and 19 `campaign-brief.md` files are old-format duplicates. 41 empty `03-results/` folders exist. These are noise that an LLM must parse through, consuming context window for no value.

---

## 3. Biggest Opportunities

### Opportunity 1: Structured Buyer Graph
Instead of 130 leads files, a single structured entity: **Buyer**, linked to **Domain**, with **DMPS score**, **Contact**, **Status**, and **Last Updated**. This would enable queries like "show me all buyers with DMPS > 90 not contacted in 30 days" — impossible today.

### Opportunity 2: Cross-Domain Intelligence
When we identify AB InBev as a buyer for Cold Beer, that intelligence should automatically surface for apuesto domains (same company, different product). When Martín Mazza is identified as World's LATAM head, every LATAM-relevant domain should know he exists.

### Opportunity 3: Templated Repeatability
Every lead list follows the same structure. Every brief follows the same structure. Every buyer expansion follows the same structure. These should be templates with schemas, not ad-hoc markdown. A new agent should receive a template, not an example to reverse-engineer.

### Opportunity 4: Knowledge Lifecycle
Research → Brief → Outreach → Contact → Response → Negotiation → Closed. Each stage should capture learnings that feed back into the research engine. "Buyer X didn't respond to angle Y but responded to angle Z" is gold that's currently lost.

### Opportunity 5: LLM-Native Access
The repo should be structured so an LLM can query "what are the top 10 highest-DMPS buyers we haven't contacted?" and get an answer in one operation, not 130 file reads.

---

## 4. Knowledge Architecture Review

### What information is duplicated?

| Duplicate Pattern | Count | Severity |
|---|---|---|
| leads.md (old format, often empty or redundant) | 20 files | Low — noise, not conflict |
| campaign-brief.md (old format) | 19 files | Low — noise |
| proof-of-human-spanish-buyers.md (identical in 2 folders) | 2 copies | High — divergence risk if one is edited |
| outreach-nofail-nobreak.md (identical in 2 folders) | 2 copies | Medium — same document, two owners |
| Google Alerts CSV (repo root + OUTREACH/ + /shared) | 3 copies | High — which is authoritative? |
| domain-backlog-new.csv (PORTFOLIO/ + repo root) | 2 copies | Medium |
| 03-results/ folders (empty) | 41 folders | Low — cruft |

### What information is fragmented?

- **DMPS scores**: Spread across 130 leads files. No single list of all scores.
- **Decision-maker names**: Trapped in narrative tables inside leads files. No searchable contact directory.
- **Bundle strategies**: Mentioned in briefs but never indexed. The apuesto 7-domain bundle exists only in a markdown file, not as a structured relationship.
- **Domain values**: In business plan, leads files, and briefs — three different places, potentially diverging.
- **Buyer expansions**: 13 expansion documents with 300+ companies. No unified buyer index.

### Which concepts should become structured entities?

1. **Domain** — name, TLD, category, value range, status, portfolio/bundle membership
2. **Buyer (Company)** — name, industry, DMPS aggregate, domains they're relevant to
3. **Contact (Person)** — name, role, company, LinkedIn, email, domains they're a buyer for
4. **Relationship** — "Domain X is bundled with Domain Y" / "Buyer A is relevant to Domain B, C, D"
5. **Contact Event** — who was contacted, when, via what channel, what was the response
6. **Domain Status** — unresearched → researched → briefed → outreach-ready → contacted → negotiating → sold

### Which documents should become templates?

1. Lead list template: defined fields (Domain, DMPS, Company, Decision-Maker, Role, Rationale, Signal), not free-form markdown tables
2. Outreach brief template: sections that are always present (Overview, Leads, Strategy, Email, LinkedIn, Objections, Internal Pricing)
3. Buyer expansion template: categories, company tables, executive profiles
4. Domain valuation template: comparables, brandability, anchor/floor/ask
5. Contact outreach record template: date, channel, message sent, response received

---

## 5. Recommended Information Architecture

### Principle: Documents for narrative, structured data for facts

**What should be structured data (JSON/database):**
- All DMPS scores and buyer-company information
- All domain valuations, statuses, and bundle relationships
- All executive contacts and outreach history
- All cross-domain relationships (bundles, same-buyer links)
- Google Alert queries (already CSV — keep structured)

**What should remain narrative markdown:**
- Outreach messaging (email/LinkedIn templates) — they require human voice
- Buyer expansion analysis (the "why" narrative, not just the "who" table)
- Corporate intelligence reports (Trinity HealthCare — deep context)
- Selling strategies and playbooks
- Domain-specific positioning and messaging angles

**What should be templates with schemas:**
- Lead list format (enforce fields: Domain, DMPS, Company, Person, Role, Rationale)
- Brief format (enforce sections: Overview, Leads summary, Strategy, Templates, Objections)
- Domain onboarding checklist

### Folder Structure Proposal

```
TurnKeySold/
├── _templates/                    ← All reusable templates
│   ├── lead-list-template.md
│   ├── outreach-brief-template.md
│   ├── buyer-expansion-template.md
│   └── domain-valuation-template.md
│
├── _data/                         ← Structured data (single source of truth)
│   ├── domains.json               ← All domains: name, value, status, portfolio
│   ├── buyers.json                ← All buyer companies: name, DMPS, domains
│   ├── contacts.json              ← All executives: name, role, company, LinkedIn
│   ├── relationships.json         ← Bundles, cross-domain links
│   └── outreach-log.json          ← Contact history (who, when, what happened)
│
├── _playbooks/                    ← Strategic knowledge (was COMPANY/ + OUTREACH/)
│   ├── research-framework.md
│   ├── dmps-scoring-guide.md
│   ├── outreach-methodology.md
│   ├── selling-strategies.md
│   └── brand-identity.md
│
├── _indexes/                      ← Navigation aids for humans and LLMs
│   ├── domain-inventory.md        ← Ranked, filterable
│   ├── buyer-index.md             ← All 300+ companies, cross-referenced
│   └── outreach-status.md         ← Contact pipeline
│
├── domains/                       ← Per-domain (renamed lowercase, consistent)
│   └── [domain-name]/
│       ├── research/              ← Was 01-research
│       │   ├── valuation.md       ← Domain valuation (from template)
│       │   ├── leads.md           ← Lead list (from template)
│       │   └── expansion/         ← Optional: deep buyer expansions
│       ├── outreach/              ← Was 02-outreach
│       │   ├── brief.md           ← Campaign brief (from template)
│       │   └── messaging.md       ← Personalized outreach copy
│       └── history/               ← Was 03-results (only if sold/contacted)
│           └── sale-record.md     ← If sold
│
├── portfolios/                    ← Cross-domain groups
│   ├── cold-beer/                 ← All 6 domains indexed
│   ├── apuesto-family/            ← All 7 domains indexed
│   └── adult/                     ← All 9+ domains indexed
│
├── website/                       ← Unchanged
├── README.md                      ← LLM navigation index
└── .github/                       ← Agent instructions
    └── AGENTS.md                  ← How agents should use this repo
```

### Key changes from current:
1. **Underscore-prefixed top-level folders** (`_templates`, `_data`, `_playbooks`, `_indexes`) — signals "system" vs. "content"
2. **No more COMPANY/, OUTREACH/, PORTFOLIO/** — content merged into _playbooks/ and _indexes/
3. **Per-domain folders lowercase** (`domains/topsex.ai/`, not `DOMAINS/TopSex.ai/`)
4. **Simpler subfolder names** (`research/`, `outreach/`, `history/` vs `01-research/`, `02-outreach/`, `03-results/`)
5. **No duplicate files** — proofs, leads.md, campaign-brief.md are eliminated
6. **New `portfolios/` folder** for cross-domain bundles
7. **New `_data/` folder** for structured, queryable information
8. **`.github/AGENTS.md`** for LLM-native instructions

---

## 6. Entity Model

```
Domain
  ├── name: string (unique, lowercase)
  ├── tld: string (.com, .ai, .org, etc.)
  ├── category: string (adult, legal, healthcare, etc.)
  ├── language_market: string (ES, EN, PT, FR, bilingual)
  ├── value_range_low: number
  ├── value_range_high: number
  ├── anchor_price: number
  ├── status: enum (unresearched, researched, briefed, outreach-ready, contacted, negotiating, sold)
  ├── portfolio: string|null (cold-beer, apuesto-family, adult, etc.)
  ├── bundle_partners: [string] (related domain names)
  ├── has_buyer_expansion: boolean
  ├── has_outreach_messaging: boolean
  ├── google_alert_queries: [{query: string, market: string}]
  ├── last_updated: datetime
  └── created: datetime

Buyer (Company)
  ├── id: string
  ├── name: string
  ├── industry: string
  ├── funding_stage: string|null
  ├── relevant_domains: [{domain: string, dmps: number, rationale: string}]
  ├── priority: number (highest DMPS across all relevant domains)
  └── last_updated: datetime

Contact (Person)
  ├── id: string
  ├── name: string
  ├── title: string
  ├── company_id: string (links to Buyer)
  ├── linkedin: string|null
  ├── email: string|null
  ├── is_primary: boolean
  └── last_updated: datetime

Outreach Event
  ├── id: string
  ├── contact_id: string
  ├── domain: string
  ├── channel: enum (email, linkedin, other)
  ├── date: datetime
  ├── message_sent: string (summary or reference to messaging file)
  ├── response: string|null
  ├── outcome: enum (no_response, interested, declined, negotiating, sold)
  └── notes: string

Relationship
  ├── type: enum (bundle, same_buyer, companion, competitor_block)
  ├── domain_a: string
  ├── domain_b: string
  └── description: string
```

---

## 7. Metadata Model

Every domain should carry metadata, ideally in a structured header (YAML frontmatter or JSON sidecar):

```yaml
---
domain: topsex.ai
status: outreach-ready
value_range: [25000, 45000]
anchor: 45000
portfolio: adult
bundled_with: []
top_buyer_dmps: 95
buyer_expansion: false
outreach_messaging: false
google_alerts: 2
last_researched: 2026-07-22
last_briefed: 2026-07-22
---
```

This metadata would populate `_data/domains.json` and enable filtering, sorting, and LLM queries without reading the full file.

---

## 8. Template Strategy

**Lead list template** should enforce:
- Domain valuation section (comparables, brandability score, range, anchor)
- Lead table with required columns: Rank, Company, DMPS, Persona, Decision-Maker, Role, Website, Signal
- Bundle section (optional, only if domain has bundles)
- Google enrichment section (optional)
- Status footer with last-updated timestamp

**Outreach brief template** should enforce:
- Domain overview (standard fields)
- Lead research summary (auto-generated from leads.md or _data/domains.json)
- Messaging strategy (primary angle, talking points, bundle)
- Email templates (subject + body, pricing-free)
- LinkedIn approach (connection + follow-up)
- Objection handling (3-5 common objections)
- Internal pricing reference (locked behind clear marker)
- Tone & cultural considerations

**Every template includes:** last-updated field, author, and a standardized filename convention.

---

## 9. Human Navigation Strategy

1. **`_indexes/domain-inventory.md`**: Primary entry point — ranked, filterable table of all domains with status
2. **`_indexes/buyer-index.md`**: "I have a buyer in mind — which domains are relevant?" — cross-referenced
3. **`README.md`**: LLM-first but human-readable overview with links to key sections
4. **Per-domain `research/leads.md`**: When focusing on one domain, everything is in one place
5. **`portfolios/`**: When thinking in bundles, see the whole group at once

A human should be able to answer "what should I work on today?" from `_indexes/domain-inventory.md` alone.

---

## 10. AI Navigation Strategy

1. **`README.md`** is the primary entry — provides structure overview and links
2. **`_data/` files (JSON)** are the query layer — an LLM reads one file to get all domains, not 130
3. **`_templates/`** tell the LLM exactly what format to produce
4. **`.github/AGENTS.md`** provides agent-specific instructions (output format, constraints, anti-patterns)
5. **`_indexes/`** provide pre-computed cross-references that save the LLM from computing them

An LLM should be able to answer "show me the top 10 highest-DMPS buyers we haven't contacted" by reading `_data/domains.json` + `_data/contacts.json` + `_data/outreach-log.json` — three files total.

---

## 11. Knowledge Lifecycle

```
Discovery → Research → Briefing → Outreach → Contact → Negotiation → Closed
    │           │          │          │          │           │          │
    ▼           ▼          ▼          ▼          ▼           ▼          ▼
  CSV       leads.md   brief.md   messaging   outreach    sale-      lessons-
  import    valuation  strategy   templates   log update  record     learned
                                                             .md
```

**Key principle:** Every stage produces knowledge that feeds back. When a buyer responds positively to a specific angle, that should update the leads.md rationale for similar buyers. When a sale closes, the entire path should be documented for pattern extraction.

---

## 12. Long-term Scalability Recommendations

1. **Structured data first, narrative second.** The entity model (domains, buyers, contacts) should live in JSON where it can be queried, sorted, and cross-referenced. Narrative markdown should reference structured data, not duplicate it.

2. **Automated indexing.** Every time a domain's leads.md is updated, a script should regenerate `_data/domains.json` and `_data/buyers.json`. The indexes should never be manually maintained.

3. **Template enforcement.** New agents should never see an example and be told "do something like this." They should receive a template with required fields and produce output that matches a schema.

4. **Contact history is infrastructure.** The outreach log is not optional — it's the nervous system of the sales organization. Without it, every contact attempt is the first contact attempt.

5. **Portfolio-first thinking.** Many of our domains are stronger as bundles. The architecture should reflect this at the top level, not bury it in per-domain files.

6. **Deprecate `/home/team/shared` as working memory.** The repo should be the single source of truth. Changes should flow repo → shared, not shared → repo.

---

## 13. Prioritized Refactoring Roadmap

### Phase 1: Stabilize (Week 1)
- [ ] Clean duplicate files: remove 20 leads.md + 19 campaign-brief.md duplicates
- [ ] Clean empty folders: remove 41 empty 03-results/ directories
- [ ] Standardize domain folder naming: all lowercase, consistent TLD suffix
- [ ] Create `.github/AGENTS.md` with agent instructions
- [ ] Update README with clean navigation

### Phase 2: Structure (Week 2)
- [ ] Create `_templates/` with lead-list, brief, and expansion templates
- [ ] Create `_data/domains.json` (extract from existing leads files)
- [ ] Create `_data/buyers.json` (cross-reference all 300+ buyers across domains)
- [ ] Create `_indexes/domain-inventory.md` (ranked, status-tracked)
- [ ] Migrate COMPANY/ and OUTREACH/ content into `_playbooks/`

### Phase 3: Connect (Week 3)
- [ ] Create `_data/relationships.json` (bundles, cross-domain buyer links)
- [ ] Create `portfolios/` folder with indexes for Cold Beer, Apuesto, Adult
- [ ] Create `_data/contacts.json` (extract all named executives)
- [ ] Create `_data/outreach-log.json` (empty — ready for use)

### Phase 4: Automate (Week 4)
- [ ] Build script to regenerate `_data/` files from per-domain sources
- [ ] Add template enforcement to agent instructions
- [ ] Create `_indexes/outreach-status.md` (pipeline dashboard)

### Phase 5: Evolve (Ongoing)
- [ ] Add structured YAML frontmatter to all per-domain files
- [ ] Build knowledge lifecycle feedback loops
- [ ] Expand entity model as new use cases emerge

---

## 14. What Should NOT Change

- **Per-domain folder structure** — the pattern of one folder per domain is correct and scalable
- **README.md quality** — already good, needs minor updates for new structure
- **Quality of research and briefs** — the content is excellent; only the organization needs work
- **Google Alerts CSV** — already structured, keep and enrich
- **Cold Beer Portfolio strategy document** — our best work, preserve exactly
- **DMPS scoring system** — proven methodology, document it in _playbooks/

---

*This review is a design document, not an implementation. No changes have been made. The recommendations above are architectural guidance for the next phase of TurnKeySold's evolution as an organization whose intelligence compounds.*
