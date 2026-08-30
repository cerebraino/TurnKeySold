---
name: domain-outbound-lead-researcher
description: Autonomously evaluate one domain name and produce a short, evidence-backed, ranked list of likely end-user buyers for targeted outbound sales. Prioritizes exact product/company matches, sibling-domain upgrades, precise use-case matches, and commercial timing signals over broad industry prospecting.
allowed-tools:
  - web_search
  - web_crawl
  - write_file
---

# Domain Outbound Lead Researcher

## Purpose

Given one domain name, identify a small, ranked list of real companies that have a specific, evidence-backed reason to buy it. Optimize for probability of sale and sale potential, not prospect volume.

The system must be willing to reject a domain and return zero or very few leads. Do not search for "anyone in the industry." Search for companies that already use the name, a close name, the same name on a weaker TLD, or a highly specific commercial use case.

Reference methodology and examples:

- [Aladey thread](https://x.com/aladey/status/2093234219350630717?s=46)
- [Grok thread summary](https://x.com/grok/status/2093566718803063252?s=46)

## Inputs / Arguments

Required:

```json
{
  "domain": "string"
}
```

Optional:

```json
{
  "asking_price": "number|null",
  "preferred_market": "string|null",
  "allowed_contact_channels": ["email", "contact_form", "linkedin", "x", "phone"],
  "maximum_primary_leads": 12,
  "maximum_backup_leads": 5,
  "previously_contacted_entities": [],
  "suppression_list": []
}
```

Defaults:

```text
maximum_primary_leads = 12
maximum_backup_leads = 5
allowed_contact_channels = all supported channels
```

## Preconditions

1. Confirm that exactly one domain is provided.
2. Normalize the domain to lowercase.
3. Separate the second-level domain (SLD) and top-level domain (TLD).
4. Do not assume availability, ownership, trademark rights, funding, launch dates, or contact details without evidence.
5. Do not fabricate email addresses, decision-makers, company facts, URLs, or timing signals.
6. If the domain is unavailable, do not infer that it is available; continue only if the task is explicitly about an owned/available domain.
7. Use official pages and primary evidence whenever possible.

## Operating Principles

1. A lead must have a specific buyer-logic sentence.
2. Industry membership alone is not a valid match.
3. Exact product/company matches outrank broad use-case matches.
4. A short list of strong leads is better than a long generic list.
5. Stop when further research produces only weaker matches.
6. Do not include pricing in first-touch copy unless explicitly requested.
7. Do not send messages autonomously; produce research and drafts for review unless an approved sending workflow is explicitly provided.
8. Preserve an auditable source URL for every factual claim.

## Step 1 — Normalize and Decompose the Domain

### Actions

1. Extract:
   - `full_domain`
   - `sld`
   - `tld`
   - `normalized_name`
2. Split the SLD into tokens.
3. Classify tokens as brandable, descriptive, geographic, industry-specific, product-specific, action-oriented, technical, AI-related, surname, foreign-language, or potentially trademarked.
4. Identify modifiers such as `AI`, geographic terms, industry terms, verbs, and product types.
5. Generate possible interpretations:
   - company/brand name
   - product name
   - category term
   - use case
   - surname or language meaning
   - slang or ambiguous meaning
6. Generate likely buyer types:
   - SaaS company
   - software product team
   - funded startup
   - incumbent with a weaker domain
   - local service business
   - media or creator brand
   - personal/surname brand

### Pass criteria

- SLD, TLD, tokens, meanings, and likely buyer types are populated.
- Ambiguity and trademark risks are explicitly recorded.

## Step 2 — Apply the Domain Qualification Gate

Score each dimension from 0 to 5.

| Dimension | 5-point signal | 0-point signal |
|---|---|---|
| Brandability | Credible company/product name | Random, awkward, or confusing |
| Specificity | Points to a defined buyer group | Means everybody or nobody |
| Commercial intent | Connected to a valuable business problem | Noncommercial or hobby-oriented |
| Extension quality | Strong `.com`, `.ai`, or relevant premium extension | Weak/mismatched TLD |
| Buyer density | 5–30 plausible buyers | No identifiable buyer class |
| Upgrade logic | Clear reason for a current user to buy | No reason to change domains |
| Memorability | Easy to say, spell, and remember | Difficult or ambiguous |
| Brand expansion | Supports a company/platform brand | Traps buyer in an undesirable feature |

Base maximum: 40.

Apply these penalties:

| Condition | Penalty |
|---|---:|
| Random four-letter string | -15 |
| Nonprofit/organizational tone without an obvious commercial buyer | -10 |
| Functional phrase that sounds like a feature rather than a brand | -7 |
| Extremely broad category word | -7 |
| Trademark-sensitive name with no clear authorized buyer | -10 |
| Extension conflicts with likely buyer market | -5 |
| Ambiguous spelling or pronunciation | -5 |

Clamp the final score to 0–40.

### Verdicts

| Score | Verdict | Action |
|---:|---|---|
| 30–40 | `OUTBOUNDABLE` | Full research |
| 22–29 | `PASS` | Focused research; stop quickly without exact matches |
| 14–21 | `BUILD` | Consider development, repositioning, or passive listing |
| 0–13 | `HARD` | No broad outbound research |

Override a low score only for an exceptionally strong exact-match buyer.

### Buyer-logic test

Write exactly one sentence:

> A company that already operates as `[brand/product/use case]` and currently uses `[current property or positioning]` could buy `[domain]` because `[specific commercial or branding benefit]`.

If this sentence cannot be written without vague language, mark the domain `BUILD` or `HARD` unless an exact-match buyer is found.

## Step 3 — Search for Exact Company/Product Matches (Tier A)

This is the highest-priority search.

### Query templates

```text
"[TOKEN]"
"[TOKEN]" product
"[TOKEN]" software
"[TOKEN]" platform
"[TOKEN]" app
"[TOKEN]" startup
"[TOKEN]" company
"[TOKEN]" AI
"[TOKEN]" SaaS
"[TOKEN]" tool
```

```text
site:linkedin.com/company "[TOKEN]"
site:producthunt.com "[TOKEN]"
site:github.com "[TOKEN]"
site:apps.apple.com "[TOKEN]"
site:play.google.com "[TOKEN]"
site:chromewebstore.google.com "[TOKEN]"
```

For multi-token domains:

```text
"[TOKEN_1] [TOKEN_2]" product
"[TOKEN_1] [TOKEN_2]" platform
"[TOKEN_1] [TOKEN_2]" startup
```

### Actions

1. Search official websites first.
2. Inspect product pages, app listings, official documentation, and official social profiles.
3. Record exact spelling and whether the name is used for a company, product, feature, or unrelated entity.
4. Record the current domain.
5. Keep only live, commercially credible entities.
6. Return no more than 15 raw Tier A candidates.

### Pass criteria

A Tier A lead requires direct evidence that the company or product uses the relevant name or a close spelling.

## Step 4 — Search Sibling Domains (Tier B)

Check the SLD and close variants across:

```text
.com, .ai, .io, .app, .co, .dev, .so, .gg, .xyz, relevant ccTLDs
```

Also check common prefixes and suffixes:

```text
get[SLD].com
try[SLD].com
use[SLD].com
hey[SLD].com
[SLD]app.com
[SLD]ai.com
[SLD]hq.com
```

### Actions

1. Verify that the property resolves to a live business or product.
2. Identify the entity using it.
3. Verify that the proposed domain is a credible upgrade.
4. Reject parked, for-sale, inactive, unrelated, or redirect-only results.
5. Do not treat domain registration alone as buyer intent.

## Step 5 — Search Keyword-in-Brand and Precise Use-Case Matches (Tier C)

### Query templates

```text
"[TOKEN]" startup
"[TOKEN]" SaaS
"[TOKEN]" platform
"[TOKEN]" agency
"[TOKEN]" software
"[TOKEN]" company
"[TOKEN]" founder
"built for [USE_CASE]"
"[USE_CASE]" platform
"[USE_CASE]" software
```

### Actions

1. Find companies whose legal or marketing name contains the token.
2. Find companies whose central product directly corresponds to the domain’s use case.
3. Verify that the domain would sound credible as their brand or product.
4. Reject companies that merely operate in the same broad industry.
5. Record the exact evidence supporting the match.

## Step 6 — Search Commercial and Timing Signals (Tier D)

Search for:

```text
"[TOKEN]" sponsored
"[TOKEN]" advertisement
"[TOKEN]" launch
"[TOKEN]" rebrand
"[TOKEN]" funding
"[TOKEN]" raises
"[TOKEN]" hiring
"[TOKEN]" product update
"[TOKEN]" expansion
```

For use cases:

```text
"[USE_CASE]" funding
"[USE_CASE]" startup funding
"[USE_CASE]" product launch
"[USE_CASE]" platform
```

### Valid signals

- Active search advertising
- Recent product launch
- Rebranding
- Fundraising
- Relevant hiring
- New-market expansion
- Active marketing investment

Timing signals improve ranking but do not replace name or use-case relevance.

## Step 7 — Search Inferior Current Domains (Tier E)

Look for relevant companies using:

- long multi-word domains
- hyphenated domains
- weak or confusing TLDs
- country-code domains used internationally
- product names buried on a path or subdomain
- a clear mismatch between public brand and domain

A weak current domain is relevant only when the proposed domain is also a credible brand or strategic upgrade.

Do not target directories, generic marketplaces, registrars, brokers, or lead lists unless explicitly requested.

## Step 8 — Qualify and Reject Candidates

Score every candidate from 0 to 100.

| Factor | Weight |
|---|---:|
| Exact brand/product match | 25 |
| Domain upgrade opportunity | 15 |
| Use-case relevance | 15 |
| Commercial maturity | 10 |
| Timing signal | 10 |
| Brand-extension logic | 10 |
| Decision-maker accessibility | 5 |
| Evidence quality | 5 |
| Trademark and conflict safety | 5 |

### Score interpretation

| Score | Status |
|---:|---|
| 85–100 | Primary A |
| 70–84 | Primary B |
| 55–69 | Backup |
| 40–54 | Watchlist; normally do not contact |
| 0–39 | Reject |

### Reject if

- The match is based only on industry.
- The company is inactive or unverifiable.
- The domain would inaccurately describe the company.
- The entity is nonprofit, governmental, or unrelated to a commercial sale.
- There is a high trademark or impersonation risk.
- The name would box the company into an unwanted feature.
- The only evidence is an unverified directory listing.
- No reliable contact path exists.
- The company is already using the obvious domain and has no upgrade logic.

## Step 9 — Enrich Surviving Leads

For every surviving lead, collect:

```text
company_name
brand_or_product_name
official_website
current_domain
likely_buyer_role
verified_contact_path
timing_signal
why_they_might_buy
evidence_urls
risk_flags
```

### Likely roles

- Founder
- CEO
- CMO
- Head of Brand
- Head of Growth
- Product lead
- Marketing lead

### Allowed contact paths

- Official contact page
- Company LinkedIn page
- Public professional profile
- Public business email, only when verified
- Official social account

Do not guess email addresses or private contact information. If no reliable path exists, downgrade the lead.

## Step 10 — Rank Leads

Rank in this order unless evidence supports a different order:

1. Exact product name on an inferior current property
2. Exact company/product name on another TLD
3. Active product using the same name on a subdomain or path
4. Company with a precise, central use-case match
5. Company with strong timing and budget signals
6. Large incumbent with an obvious strategic reason
7. Generic industry participant — normally exclude

Optional expected-close heuristic:

```text
expected_close_score = candidate_score * evidence_confidence * contactability_factor * timing_factor
```

```text
evidence_confidence:
  high = 1.00
  medium = 0.80
  low = 0.60

contactability_factor:
  direct_decision_maker = 1.00
  identifiable_role = 0.85
  generic_contact_path = 0.65

timing_factor:
  active_launch_or_rebrand = 1.15
  recent_funding_or_hiring = 1.10
  no_timing_signal = 1.00
```

Cap the final score at 100.

## Step 11 — Apply Deduplication and Suppression

Deduplicate by:

- canonical company name
- parent company
- official domain
- product name
- redirects
- duplicate sources

Normally list a company once and nest multiple possible contact roles under it.

Suppress:

- previously contacted entities
- entities that declined
- people who opted out
- invalid or bounced addresses
- inactive companies
- generic directories and marketplaces
- high-risk trademark targets
- entities without evidence

## Step 12 — Compliance Guardrails

The agent prepares research and drafts; it does not send autonomously without explicit authorization.

For commercial email, preserve the following CAN-SPAM requirements from FTC guidance:

- Do not use false or misleading header information.
- Do not use deceptive subject lines.
- Identify the message as an advertisement where required.
- Include a valid physical mailing address.
- Provide a simple opt-out mechanism.
- Suppress future messages after an opt-out.

Source: [FTC CAN-SPAM compliance guide](https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide)

For UK outreach, consult PECR guidance in addition to applicable data-protection requirements: [ICO direct marketing guidance](https://ico.org.uk/for-organisations/direct-marketing-and-privacy-and-electronic-communications/)

For EU outreach, respect the right to object to direct marketing: [EUR-Lex GDPR text](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02016R0679-20160504)

Do not:

- imply affiliation with the target
- claim the target owns or legally controls the domain
- claim trademark rights without evidence
- encourage impersonation or cybersquatting
- fabricate contact data
- continue contacting suppressed recipients

## Step 13 — Generate Outreach Angles

Do not include a price in first-touch copy unless requested.

### Exact product-name angle

```text
Subject: [DOMAIN] for [PRODUCT]

Hi [NAME] — I noticed that [COMPANY] already uses “[PRODUCT]” for [SPECIFIC PRODUCT DESCRIPTION]. I own [DOMAIN], which may be a cleaner direct-match domain for the product. Would it be useful to discuss?
```

### Sibling-domain upgrade angle

```text
Subject: Possible domain upgrade for [BRAND]

Hi [NAME] — I noticed that [COMPANY] operates on [CURRENT_DOMAIN]. [TARGET_DOMAIN] is the matching [TLD] version and may be a stronger home for the brand. Is domain acquisition something you are considering?
```

### Precise-use-case angle

```text
Subject: A domain aligned with [USE_CASE]

Hi [NAME] — [COMPANY] focuses on [SPECIFIC USE CASE], and [TARGET_DOMAIN] closely describes that positioning. I thought it might be relevant if you are evaluating brand or domain upgrades.
```

### Outreach rules

- Mention one specific observation from the prospect’s site.
- Keep the message short.
- Avoid hype, urgency, and mail-merge language.
- Do not say “amazing opportunity.”
- Do not claim the domain is “obviously theirs.”
- Offer an easy way to decline.

## Step 14 — Follow-Up Sequence

Recommend, but do not send, three or four touches over approximately two to three weeks:

```text
Touch 1: Specific relevance and domain fit
Touch 2: Brief direct-upgrade reminder
Touch 3: Brand clarity or customer memorability benefit
Touch 4: Polite close-the-loop message
```

Stop when the recipient declines, opts out, bounces, becomes irrelevant, or is suppressed.

## Stop Conditions

Stop early when:

- Three or more Tier A leads are found.
- Five or more candidates score at least 85.
- The next search round produces only generic industry matches.
- Two consecutive search rounds produce no new qualified candidates.
- The domain is `HARD` and no exact-match buyer exists.
- Remaining candidates require speculative reasoning.
- The list already contains enough leads for a focused campaign.

Default research limits:

```text
maximum search rounds: 5
maximum search queries: 35
maximum raw candidates: 50
maximum fully enriched candidates: 20
maximum primary leads: 12
maximum backup leads: 5
```

If fewer than three qualified leads remain, return the smaller list and explicitly state that lead density is insufficient. Recommend only one or more of:

- test the strongest lead
- wait for a timing signal
- monitor sibling domains
- reposition the domain
- list passively
- develop the asset
- discontinue outbound

## Failure Handling

### Missing or invalid domain

Return:

```json
{
  "status": "blocked",
  "reason": "A single valid domain is required.",
  "required_input": "domain"
}
```

### Search failure

Record:

```text
failed_tool_or_source
query_attempted
error_summary
what_was_not_verified
```

Do not replace unavailable evidence with inference.

### Conflicting evidence

1. Prefer the official source.
2. Record the conflict.
3. Downgrade confidence if unresolved.
4. Do not include the lead as Primary A solely on conflicting evidence.

### No qualified leads

Return the domain verdict, research performed, rejection reasons, and an empty lead list. Do not manufacture prospects.

### Incomplete contact data

Keep the company only if it is otherwise qualified, but set:

```text
contact_path = []
confidence = lower confidence
risk_flags += ["no_verified_contact_path"]
```

## Required JSON Output Schema

```json
{
  "status": "complete | blocked | partial",
  "domain": "string",
  "normalized_name": "string",
  "sld": "string",
  "tld": "string",
  "qualification": {
    "verdict": "OUTBOUNDABLE | HARD | PASS | BUILD",
    "score": 0,
    "score_max": 40,
    "dimension_scores": {
      "brandability": 0,
      "specificity": 0,
      "commercial_intent": 0,
      "extension_quality": 0,
      "buyer_density": 0,
      "upgrade_logic": 0,
      "memorability": 0,
      "brand_expansion": 0
    },
    "penalties": [
      { "reason": "string", "points": 0 }
    ],
    "buyer_logic": "string",
    "likely_buyer_types": ["string"],
    "risk_flags": ["string"],
    "confidence": "high | medium | low"
  },
  "analysis": {
    "tokens": ["string"],
    "modifiers": ["string"],
    "possible_meanings": ["string"],
    "search_strategy": ["string"]
  },
  "primary_leads": [
    {
      "rank": 1,
      "company_name": "string",
      "brand_or_product_name": "string",
      "official_website": "https://example.com",
      "current_domain": "example.com",
      "match_type": "exact_product | exact_company | sibling_tld | close_spelling | use_case | commercial_signal | inferior_domain",
      "tier": "A | B | C | D | E",
      "why_they_might_buy": "string",
      "likely_buyer_roles": ["founder", "CEO"],
      "contact_path": [
        {
          "type": "official_contact_page | company_linkedin | public_profile | public_business_email | official_social_account",
          "url": "https://example.com",
          "verified": true
        }
      ],
      "timing_signals": [
        {
          "type": "launch | funding | rebrand | hiring | advertising | expansion | none",
          "description": "string",
          "source_url": "https://example.com",
          "date": "YYYY-MM-DD|null"
        }
      ],
      "evidence": [
        {
          "claim": "string",
          "source_url": "https://example.com",
          "source_type": "official | app_store | social | database | news | directory",
          "strength": "high | medium | low"
        }
      ],
      "score": 0,
      "score_breakdown": {
        "exact_match": 0,
        "domain_upgrade": 0,
        "use_case_relevance": 0,
        "commercial_maturity": 0,
        "timing_signal": 0,
        "brand_extension": 0,
        "decision_maker_access": 0,
        "evidence_quality": 0,
        "safety": 0
      },
      "confidence": "high | medium | low",
      "risk_flags": [],
      "recommended_angle": "string"
    }
  ],
  "backup_leads": [],
  "rejected_candidates": [
    {
      "name": "string",
      "reason": "industry_only | inactive | weak_match | nonprofit | trademark_risk | no_evidence | no_contact_path | other",
      "evidence_url": "https://example.com|null"
    }
  ],
  "suppression_checks": {
    "duplicate_companies_removed": 0,
    "inactive_entities_removed": 0,
    "generic_industry_matches_removed": 0,
    "trademark_risk_flags": 0,
    "opt_out_matches": 0
  },
  "outreach_recommendation": {
    "recommended_sequence": "focused_manual | small_batch_manual_review | do_not_outbound",
    "primary_angle": "string",
    "avoid_saying": ["string"],
    "suggested_touch_count": 3,
    "suggested_window": "2–3 weeks"
  },
  "limitations": ["string"],
  "research_metadata": {
    "search_rounds": 0,
    "queries_run": 0,
    "candidates_reviewed": 0,
    "retrieved_at": "YYYY-MM-DD"
  }
}
```

## Final QA Checklist

Before returning, verify all of the following:

- [ ] Exactly one domain was processed.
- [ ] Qualification verdict and score are present.
- [ ] Buyer-logic sentence is specific.
- [ ] Every included lead has an evidence URL.
- [ ] Every included lead has a specific reason to buy.
- [ ] Every included lead has a match type and score.
- [ ] Generic industry-only matches were removed.
- [ ] Duplicate companies were removed.
- [ ] Inactive and parked entities were removed.
- [ ] No email address or identity was fabricated.
- [ ] Timing claims have supporting sources.
- [ ] Trademark and impersonation risks are recorded.
- [ ] Suppression checks were applied.
- [ ] Lead count is within configured limits.
- [ ] Primary leads are ranked in descending order.
- [ ] Search limitations are disclosed.
- [ ] Output is valid JSON before the human-readable rendering is generated.
