# TurnKeySold — Metadata & Provenance Standard

**Version:** 1.0  
**Status:** PROPOSED — pending founder approval before enforcement  
**Applies to:** All knowledge artifacts (lead lists, briefs, expansions, corporate intel, outreach messaging)

---

## Why Provenance Matters

In our current repository, a reader cannot answer:
- Who created this lead list? When?
- What sources did they use? What's the confidence level?
- Has this been reviewed? By whom? When?
- Was this domain provided by the owner, or hallucinated by a researcher?
- Which version of this file is authoritative?

Without provenance, plausible-sounding speculation is indistinguishable from verified intelligence. Six hallucinated domains entered our research because there was no origin tracking.

---

## Provenance Standard

Every important knowledge artifact must carry a **provenance block** at the top of the file using YAML frontmatter.

### Required Fields

```yaml
---
artifact_id: [unique identifier, e.g., "leads-topsex.ai-v3"]
artifact_type: [leads | brief | expansion | intel | messaging | valuation]
domain: [domain name, lowercase]
created: [ISO 8601 datetime]
created_by: [agent role]
source: [web-research | external-llm | owner-provided | agent-browser | derived-from-research]
confidence: [HIGH | MEDIUM | LOW]
---
```

### Optional Fields

```yaml
reviewed_by: [who reviewed]
reviewed_date: [ISO 8601 datetime]
review_decision: [APPROVED | REJECTED | REVISED]
replaces: [previous artifact_id]
sources_used: [list of URLs or document paths]
evidence_quality: [VERIFIED | LIKELY | SPECULATIVE]
owner_provided: [true | false]
hallucination_checked: [true | false]
notes: [free-text context]
revisions:
  - date: [ISO 8601]
    by: [agent role]
    change: [description]
    reason: [why]
```

### Confidence Levels

| Level | When to Use |
|---|---|
| **HIGH** | Verified against primary sources (company websites, SEC filings, LinkedIn) |
| **MEDIUM** | Reasonable inference from secondary sources or domain knowledge |
| **LOW** | Speculative — plausible but unverified |

### Evidence Quality

| Level | When to Use |
|---|---|
| **VERIFIED** | Confirmed by primary source or multiple independent secondary sources |
| **LIKELY** | Supported by credible source but not independently confirmed |
| **SPECULATIVE** | Reasonable hypothesis not yet confirmed |

---

## Examples

### Lead List Provenance

```yaml
---
artifact_id: leads-automoviles.ai-v2
artifact_type: leads
domain: automoviles.ai
created: 2026-07-22T19:07:00Z
created_by: agent-domain-researcher
source: web-research
confidence: HIGH
owner_provided: true
hallucination_checked: true
reviewed_by: agent-lead
reviewed_date: 2026-07-22T19:10:00Z
review_decision: APPROVED
sources_used:
  - https://mercadolibre.com
  - https://linkedin.com/in/marcosgalperin
  - /home/team/shared/domain-backlog-new.csv
evidence_quality: VERIFIED
---
```

### Outreach Messaging Provenance

```yaml
---
artifact_id: messaging-proof-of-human-v1
artifact_type: messaging
domain: humanoreal.com, pruebadehumanidad.com
created: 2026-07-24T17:49:00Z
created_by: agent-outreach-architect
source: derived-from-research
confidence: MEDIUM
based_on: /home/team/shared/proof-of-human-spanish-buyers.md
reviewed_by: agent-lead
reviewed_date: 2026-07-24T17:50:00Z
review_decision: APPROVED
notes: Pricing-free per company policy. Martín Mazza quote verified from Forbes Argentina.
---
```

---

## Anti-Patterns

| Anti-Pattern | Correct Approach |
|---|---|
| "I think this company would be interested" without evidence | Mark confidence LOW, note as hypothesis |
| Copying another domain's lead list without verification | Fresh research per domain; cite if reused |
| No created/created_by fields | Always include provenance block |
| "Based on my knowledge" as source | Cite specific URLs, documents, or search results |
| Skipping hallucination_check | Always verify against owner-provided domain lists |

---

*Provenance is not optional — it is the foundation of trust in our organizational knowledge.*
