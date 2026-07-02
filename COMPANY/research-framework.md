# DomainMatch Pro — Research Framework
## Domain Evaluation, Buyer Identification, Lead Scoring & Decision-Maker Research

> **Author:** domain-researcher  
> **Purpose:** Structured methodology for evaluating premium domains and identifying qualified buyers.  
> **System Alignment:** This framework feeds into the Outreach Playbook (`playbook.md`) with scored, researched leads.  
> **Version:** 1.0

---

## Table of Contents

1. [Domain Evaluation Criteria](#1-domain-evaluation-criteria)
2. [Buyer Identification Methodology](#2-buyer-identification-methodology)
3. [Lead Scoring System](#3-lead-scoring-system)
4. [Decision-Maker Research Process](#4-decision-maker-research-process)
5. [Step-by-Step Workflow](#5-step-by-step-workflow)
6. [Handoff to Outreach](#6-handoff-to-outreach)

---

## 1. Domain Evaluation Criteria

### 1.1 Five-Factor Valuation Model

Each domain is scored across **five weighted dimensions** to determine its market value:

| Factor | Weight | What It Measures |
|--------|--------|-----------------|
| **Comparable Sales** | 35% | Recent sales of similar domains (same TLD, keywords, length) |
| **Keyword Market Value** | 25% | Industry demand, advertiser competition, keyword CPC |
| **Brandability** | 20% | Memorability, pronounceability, spelling clarity, aesthetic value |
| **Traffic & Type-in** | 10% | Direct navigation traffic, backlinks, domain authority |
| **Extension & Length** | 10% | Length in characters, TLD prestige (.com > .io > .co) |

### 1.2 Comparable Sales Research

**Primary data sources:**
- **NameBio** (namebio.com) — Largest public domain sales database. Filter by TLD, keyword, length, sale date.
- **DNJournal** — Weekly/monthly curated premium sales reports.
- **Sedo Marketplace** (sedo.com) — Real-time and completed sales.
- **Afternic** (afternic.com) — GoDaddy marketplace completed sales.
- **GoDaddy Domain Auctions** — Close-out and expired auction prices.

**Minimum requirements for a reliable estimate:**
- At least **3 comparable sales**
- Sales within the **last 18 months** (12 months preferred)
- Same TLD tier (.com for .com, .io/.co for .io/.co)
- Within ±3 characters in length
- Shares at least one meaningful keyword

**Adjustment factors for comparables:**

| Condition | Multiplier |
|-----------|-----------|
| .com vs .io/.co | .com × 1.0, .io/.co × 0.4–0.6 |
| Dictionary word vs compound | Dictionary × 1.5–3.0 |
| 3–5 char vs 6–8 vs 9+ | Short × 2–5× of longer equivalents |
| Exact-match domain (EMD) | EMD × 1.5–2.5× modified term |

### 1.3 Brandability Assessment

Score each domain on five attributes (1–10 scale, max 50):

| Attribute | 1–3 (Poor) | 4–6 (Average) | 7–10 (Excellent) |
|-----------|------------|---------------|------------------|
| **Pronounceability** | Hard to say, awkward clusters | Clear, one interpretation | Effortless, rolls off the tongue |
| **Spellability** | Ambiguous (ph/f, c/k/s) | One common variant | No alternative spellings |
| **Memorability** | Forgettable | Recognizable after hearing | Immediately sticky |
| **Visual Aesthetic** | Numbers/hyphens | Clean, no special chars | Beautiful word pattern |
| **Category Fit** | Unclear what it's for | Vaguely suggests industry | Instantly conveys the niche |

**Brandability Tiers:**

| Score | Tier | Description |
|-------|------|-------------|
| 40–50 | Tier 1 — Premium Brandable | "Uber," "Zoom," "Stripe" equivalents. Maximum outreach priority. |
| 30–39 | Tier 2 — Good Brandable | Solid startup names. Strong outreach candidates. |
| 20–29 | Tier 3 — Functional | Works but lacks spark. Moderate priority. |
| < 20 | Tier 4 — Commodity | Keyword-focused only. Lowest priority. |

### 1.4 Traffic & Authority Signals

| Signal | Free Tool | What to Look For |
|--------|-----------|-----------------|
| Estimated type-in traffic | Estibot, DomainTools | > 100 monthly visits = noteworthy |
| Domain Authority (DA) | Moz Bar, Ahrefs | DA > 20 = existing backlink profile |
| Backlinks | Ahrefs, Majestic | Quality backlinks from real sites |
| Wayback Machine history | archive.org | Previous legitimate use (not parked-only) |
| Search volume (domain as phrase) | Google Keyword Planner | > 1,000 monthly searches = strong intent |

### 1.5 Final Value Range

```
Estimated Value = (ComparableScore × 0.35) + (KeywordScore × 0.25) +
                  (BrandabilityScore × 0.20) + (TrafficScore × 0.10) +
                  (ExtensionScore × 0.10)
```

| Score | Value Range | Campaign Suitability |
|-------|-------------|---------------------|
| 90–100 | $50,000+ | High-touch, VIP campaign. CEO-level outreach only. |
| 75–89 | $10,000–$49,999 | Priority campaign. Multi-channel sequence. |
| 55–74 | $3,000–$9,999 | Standard campaign. Good for testing process. |
| 35–54 | $500–$2,999 | Lite campaign or portfolio bundle. |
| < 35 | < $500 | Not suitable for premium outreach. |

---

## 2. Buyer Identification Methodology

### 2.1 The Five Buyer Personas (Aligned with Outreach Playbook)

#### Persona A: The Visionary (Founder/CEO)
- **Profile:** Startup founders, CEOs of growth companies
- **Need:** Brand authority, category leadership, long-term asset value
- **Best for:** Brandable .com domains, category-killer keywords
- **Price sensitivity:** Moderate ($5K–$50K)
- **Conversion:** Moderate — slower decision, higher ASP
- **Outreach playbook reference:** "The Visionary" template (playbook.md §2A)

#### Persona B: The Strategist (CMO / VP Marketing)
- **Profile:** Marketing leaders in established companies
- **Need:** Campaign efficiency, brand recall, direct traffic, lower CAC
- **Best for:** Keyword-match domains, geo domains, niche-specific names
- **Price sensitivity:** Moderate ($3K–$25K)
- **Conversion:** Moderate — needs internal buy-in, but has budget
- **Outreach playbook reference:** "The Strategist" template (playbook.md §2B)

#### Persona C: The Opportunist (Investor / Strategic Acquirer)
- **Profile:** Domain investors, corporate development, competitors
- **Need:** Resale value, defensive acquisition, portfolio synergy
- **Best for:** Premium generics, short domains, category leaders
- **Price sensitivity:** Low — market-aware, negotiates hard
- **Conversion:** Lower — wants wholesale prices (30–50% of retail)
- **Outreach playbook reference:** "The Opportunist" template (playbook.md §2C)

#### Persona D: Individual Entrepreneurs / Solopreneurs
- **Profile:** Indie hackers, newsletter writers, content creators, SAAS builders
- **Need:** Affordable brand identity, project launching
- **Best for:** Mid-tier brandables, .io/.co domains
- **Price sensitivity:** High ($500–$5K ceiling)
- **Conversion:** Moderate — love domains but budget-constrained

#### Persona E: Marketing Agencies & Freelancers
- **Profile:** Digital agencies, PR firms, SEO consultants
- **Need:** Microsites, campaign landing pages, client projects
- **Best for:** Descriptive domains, geo + keyword combos
- **Price sensitivity:** Moderate ($1K–$10K)
- **Conversion:** Low-Moderate — opportunistic

### 2.2 Keyword-to-Industry Mapping

Extract primary keywords from the domain and map to industries:

| Domain Keywords | Primary Industries | Buyer Personas |
|----------------|-------------------|----------------|
| Financial (lend, pay, bank, fin, invest, fund) | Fintech, Banking, Payments, Investments | A, B, C |
| Health (med, care, health, fit, doc, wellness) | Healthcare, Fitness, Telemedicine, Wellness | A, B, D |
| Tech (cloud, data, code, dev, ai, digit, tech) | SaaS, Enterprise Software, AI/ML, DevOps | A, B, D |
| Legal (law, legal, suit, settle, court) | LegalTech, Law Firms, Legal Services | A, B, E |
| Real Estate (home, rent, estate, house, prop) | Real Estate, PropTech, Mortgages | A, B |
| E-commerce (buy, shop, deal, cart, store) | E-commerce, RetailTech, Marketplaces | A, B, D |
| Travel (fly, trip, go, travel, stay, book) | TravelTech, Hospitality, Airlines | A, B, C |
| Education (learn, edu, study, course, teach) | EdTech, Online Learning, Universities | A, B, D |
| Green (eco, green, solar, clean, sustain) | CleanTech, Renewables, ESG | A, C, E |
| Security (safe, guard, shield, sec, protect) | Cybersecurity, Insurance, Monitoring | A, B, C |

### 2.3 Company Discovery Process

**Step 1:** Extract 1–3 primary keywords from the domain name.
- Example: `PetInsurance.com` → "pet insurance" (primary), "pet," "insurance" (secondary)

**Step 2:** Map to 1–2 primary industries using the table above.

**Step 3:** Find companies in each industry using:
- **Crunchbase** — Search by industry tag; filter by funding stage (Seed–Series C is ideal), employee count, HQ location
- **LinkedIn** — Search companies by industry, company size, and keyword in description
- **G2 / Capterra** — Software categories; find companies in matching verticals
- **Google Search** — `"keyword" + "company" + "funding"` or `"best [industry] companies"`

**Step 4:** Prioritize companies at the right stage:

| Company Stage | Buying Likelihood | Reasoning |
|--------------|-------------------|-----------|
| Pre-seed / Idea | Low | No budget for premium domains |
| Seed / Angel | Medium | Budget limited but open to brand-building |
| Series A | High | Funded, needs credibility, has brand budget |
| Series B–C | Highest | Growth mode, established, can afford $10K+ |
| Enterprise (500+ emp) | Medium-High | Budget exists but decision process is slow |
| Bootstrapped profitable | Medium | Might spend if they see clear ROI |

**Target:** 15–25 candidate companies per domain.

---

## 3. Lead Scoring System

### 3.1 The DomainMatch Pro Score (DMPS)

Each prospect is scored 0–100 across four dimensions:

#### Dimension 1: Domain Fit (0–35 points)

| Criterion | Max | Scoring |
|-----------|-----|---------|
| Exact keyword match to company's core offering | 15 | 15 = exact match; 10 = partial; 5 = adjacent; 0 = none |
| Industry alignment | 10 | 10 = same vertical; 5 = adjacent; 0 = different |
| Brandability appeal to this company | 10 | 10 = fits brand identity; 5 = moderate; 0 = doesn't fit |

#### Dimension 2: Prospect Quality (0–30 points)

| Criterion | Max | Scoring |
|-----------|-----|---------|
| Decision-making authority | 10 | 10 = CEO/Founder/CMO; 7 = VP/Director; 3 = Manager; 0 = IC |
| Contact info verified | 10 | 10 = email + LinkedIn confirmed; 5 = email only; 2 = LinkedIn only; 0 = none |
| Intent signal present | 10 | 10 = strong (funding+launch+rebrand); 7 = moderate (one signal); 3 = weak; 0 = none |

#### Dimension 3: Company Fit (0–20 points)

| Criterion | Max | Scoring |
|-----------|-----|---------|
| Company stage | 10 | 10 = Series A–C (growth); 7 = Seed/Enterprise; 5 = Early/Bootstrapped; 2 = Micro |
| Budget capacity | 10 | 10 = raised capital or $50M+ revenue; 5 = profitable modest; 2 = bootstrapped |

#### Dimension 4: Purchase Urgency (0–15 points)

| Criterion | Max | Scoring |
|-----------|-----|---------|
| Timeline signal | 8 | 8 = active need (hiring brand team, competitor domain acquisition); 4 = possible; 0 = none |
| Current domain quality | 7 | 7 = bad domain (hyphenated, long, wrong TLD); 4 = mediocre; 0 = good current domain |

### 3.2 Lead Tiers

| DMPS Range | Tier | Action | Outreach Sequence |
|------------|------|--------|-------------------|
| 80–100 | **Hot** | Immediate personalized outreach. High-touch campaign. | Full Domain-14 flow (playbook §3) |
| 60–79 | **Warm** | Standard outreach sequence. | Domain-14 with less personalization |
| 40–59 | **Lukewarm** | Batch outreach or nurture sequence. | Abbreviated sequence, lower cadence |
| 20–39 | **Cool** | Long-term nurture only. | Quarterly check-in only |
| 0–19 | **Cold** | Skip. Deprioritize. | — |

### 3.3 Intent Signals (Priority Boosters)

| Signal | Source | DMPS Boost |
|--------|--------|-----------|
| Recent funding round ($1M+) | Crunchbase, TechCrunch | +3 |
| New product launch | PR, Product Hunt, company blog | +3 |
| Rebranding underway | New logo, "brand" in job posts | +4 |
| Job posting: Brand/Marketing VP | LinkedIn Jobs | +2 |
| Recent .com domain change | Wayback, DN history | +5 |
| Competitor acquired a domain | Industry news | +3 |
| Expanding to new geography | Press releases, job locations | +2 |
| Current domain is awkward | Hyphens, length, wrong TLD | +4 |

### 3.4 Domain-Level Priority

For campaign prioritization across multiple domains:

```
Domain Priority Score = Average(DMPS of top 10 leads) × DomainValueMultiplier
```

Where `DomainValueMultiplier = min(estimated_value / 5000, 5)`.

---

## 4. Decision-Maker Research Process

### 4.1 Role Targeting by Company Size

| Company Size | Target Role | Rationale |
|-------------|-------------|-----------|
| Startup (1–10) | CEO / Co-founder | They own brand decisions directly |
| Small (10–50) | CEO, CMO, Head of Product | CEO delegates; CMO is ideal target |
| Medium (50–500) | VP Marketing, Brand Director, CMO | Brand/marketing owns naming |
| Large (500+) | SVP Brand, Head of Digital, Chief Innovation Officer | Needs champion; slower process |

### 4.2 Prospecting Tool Stack

**Free tools:**
- **LinkedIn** — `"Company" + "People" + filter by title`
- **Crunchbase** — Company profile includes team, funding, competitors
- **Company Website** — "About" / "Team" / "Leadership" pages
- **Twitter/LinkedIn Company Page** — Key hires often listed

**Paid tools (recommended for campaigns):**
- **LinkedIn Sales Navigator** — Advanced search by title, function, seniority, company size
- **Apollo.io** — Email + LinkedIn discovery with verified contacts
- **Hunter.io** — Email pattern discovery by domain
- **Clay.com** — Waterfall enrichment; merges multiple data sources

### 4.3 Verification Checklist

Before adding a prospect to the lead list, verify:

- [ ] Role matches decision-making authority
- [ ] LinkedIn profile is active (posted or engaged within 3 months)
- [ ] Currently employed at the target company
- [ ] Tenure > 6 months (enough influence)
- [ ] Email is found and verified (or LinkedIn InMail available)
- [ ] Job description mentions branding, naming, or domain decisions

### 4.4 Contact Enrichment Workflow

```
1. IDENTIFY → LinkedIn Sales Navigator / Company website
2. FIND EMAIL → Hunter.io / Apollo.io / Clay waterfall
3. VERIFY → NeverBounce / ZeroBounce / MillionVerifier
4. LINKEDIN → Match name + company, note URL
5. INTENT SIGNALS → Check Crunchbase, Google News, company blog
6. RECORD → Add to lead list with role, company, contact, signals, source URLs
```

---

## 5. Step-by-Step Workflow

### Per-Domain Research Workflow

```
□ PHASE 1 — DOMAIN EVALUATION (est. 30–60 min)
  □ Run 3+ comparable sales on NameBio
  □ Run Estibot for directional reference
  □ Score brandability (1–50) with tier classification
  □ Check traffic/DA/backlinks/Wayback Machine
  □ Calculate estimated value range
  □ Log all data in domain summary

□ PHASE 2 — BUYER DISCOVERY (est. 45–90 min)
  □ Extract keywords and map to industries
  □ Search Crunchbase for 15–25 candidate companies
  □ Classify each company by buyer persona (A–E)
  □ Note company stage, size, and funding status
  □ Rank by buying likelihood

□ PHASE 3 — DECISION-MAKER RESEARCH (est. 30–60 min per company)
  □ For top 10 companies: find decision-maker
  □ Verify role, LinkedIn, and email contact
  □ Check for intent signals
  □ Score each lead (DMPS 0–100)
  □ Complete verification checklist

□ PHASE 4 — LEAD PRIORITIZATION (est. 15 min)
  □ Rank all leads by DMPS
  □ Tag Hot (80+) and Warm (60–79) leads
  □ Pass top 10 to outreach-architect
  □ Save remainder as nurture list

□ PHASE 5 — DOCUMENTATION (est. 15 min)
  □ Write domain summary (valuation, brandability, value range)
  □ Prepare lead list (scored, verified, with source URLs)
  □ Add context notes per lead (funding, recent news, triggers)
  □ Place output in /home/team/shared/ for outreach-architect
```

### Estimated Time Per Domain

- **Thorough research:** ~2–4 hours
- **With practice:** ~1–2 hours for standard domains

---

## 6. Handoff to Outreach

### 6.1 Lead List Output Format

When delivering to the outreach-architect, use this format:

```csv
DMPS,Tier,Company,Persona,DecisionMaker,Role,Email,LinkedIn,IntentSignal,Notes
88,Hot,AcmeCorp,B,Jane Doe,CMO,jane@acme.com,linkedin.com/in/jane,Series B $12M,Exact product match
75,Warm,BetaInc,A,John Smith,CEO,john@beta.com,linkedin.com/in/john,New product launch,Strong brand fit
...
```

### 6.2 Domain Summary Format

```markdown
## Domain: [DOMAIN]

**Valuation:** $X–$Y | **Brandability:** Z/50 (Tier N)
**Comparables:** [domain1: $A, domain2: $B, domain3: $C]
**Primary Industries:** [industry1], [industry2]

**Top Leads:**
1. [Company] — [DMPS] — [Decision-Maker] — [Role] — [Signal]
2. ...

**Outreach Recommendations:**
- Best persona to target: [Visionary / Strategist / Opportunist]
- Suggested angle: [value proposition hook]
- Urgency angle: [scarcity or timeline reason]
- Price anchoring: [suggested opening price per playbook negotiation]
```

### 6.3 Cross-System Alignment

| System Element | Where | Purpose |
|----------------|-------|---------|
| Buyer Personas A–C | This framework §2.1 + playbook §2 | Researcher identifies the persona → Outreach uses matching template |
| Intent Signals | This framework §3.3 | Researcher flags signals → Outreach uses as hook in messaging |
| Lead Tiers | This framework §3.2 + playbook §3 | Hot/Warm → Full Domain-14; Lukewarm → Abbreviated |
| Domain Value Range | This framework §1.5 + playbook §4 §5 | Researcher provides anchor → Outreach uses in negotiation |
| Seller Info | seller_onboarding.md | Researcher uses seller answers to enrich domain summary |

---

*Document maintained by domain-researcher (agent-domain-researcher). Last updated: 2026-06-24. Compliments the Outreach Playbook (`playbook.md`) and Seller Onboarding (`seller_onboarding.md`) as part of the DomainMatch Pro system.*