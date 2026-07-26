# TurnKeySold — Decision Architecture

**Version:** 1.0  
**Status:** PROPOSED — organizational judgment design  
**Purpose:** Define how an AI-native company makes, documents, and learns from decisions.  
**Prerequisite:** KNOWLEDGE_MODEL.md — defines what we know. This document defines how we act on it.

---

> "Knowledge exists to improve decisions. A company that knows more but decides no better has acquired information, not intelligence."

---

## Part 1 — The Decision Landscape

### What Kinds of Decisions Exist?

All decisions fall into one of four categories, defined by two dimensions: **stakes** (what's at risk if wrong) and **reversibility** (how costly to undo).

| Category | Stakes | Reversibility | Examples | Frequency |
|---|---|---|---|---|
| **Tactical** | Low individually, high in aggregate | Easily reversible | Which buyer to contact today? What subject line? When to follow up? | Hundreds/day |
| **Operational** | Medium | Reversible with effort | Which angle to pitch? Bundle or individual pricing? Which market to prioritize? | Dozens/week |
| **Strategic** | High | Costly to reverse | Cold Beer Portfolio bundle strategy. Entering a new buyer category. Pricing floor for premium domains. | Monthly |
| **Constitutional** | Existential | Very costly or impossible | Principles. Knowledge model changes. "We only sell domains we own." | Yearly or less |

### The Decision Gravity Principle

> **Decisions should be made at the lowest level that has the information and authority to make them correctly.**

As decisions rise in stakes and irreversibility, they should rise in authority level. As they rise in frequency and reversibility, they should descend to where speed matters more than deliberation.

---

### Decision Types by Domain

#### Pricing Decisions
- **Tactical:** What anchor price to mention in a reply? → AI recommends, human reviews (today), AI autonomous (future).
- **Operational:** Bundle pricing strategy? → AI proposes, lead decides.
- **Strategic:** Portfolio reserve price? → Lead proposes, founder decides.
- **Constitutional:** Do we ever auction domains? → Founder only.

#### Outreach Decisions
- **Tactical:** Which Person to contact first? → AI autonomous (within Playbook constraints).
- **Operational:** Which angle to use for this Organization? → AI proposes, lead reviews (today), AI autonomous after Pattern validation.
- **Strategic:** Should we contact a competitor of a current buyer? → Lead decides.
- **Constitutional:** Do we ever cold-contact without research? → Principle: never.

#### Research Decisions
- **Tactical:** Which Source to check next? → AI autonomous.
- **Operational:** Is this Organization worth adding to the lead list? → AI proposes, lead reviews for DMPS ≥ 80.
- **Strategic:** Should we expand into a new buyer category? → Lead proposes, founder decides.
- **Constitutional:** What qualifies as a Source? → Principle.

#### Relationship Decisions
- **Tactical:** Should I mention Bundle X when pitching Domain Y? → AI autonomous (within Playbook).
- **Operational:** Should we offer a discount for the full bundle? → Lead decides.
- **Strategic:** Should we break up a Bundle and sell individually? → Founder decides.
- **Constitutional:** Do we ever sell to a buyer we believe will harm the domain's value? → Founder only.

---

## Part 2 — Authority Boundaries

### The Three Zones

```
┌─────────────────────────────────────────────────────┐
│ ZONE 3: FOUNDER                                     │
│ Constitutional decisions. Principles. Model changes. │
│ "What kind of company are we?"                       │
├─────────────────────────────────────────────────────┤
│ ZONE 2: LEAD (Human Oversight)                      │
│ Strategic decisions. Pattern promotion.              │
│ Risk assessment. Cross-domain intelligence.          │
│ "What should we do, and how should we do it?"        │
├─────────────────────────────────────────────────────┤
│ ZONE 1: AGENT (AI Autonomous)                       │
│ Tactical decisions within Playbook constraints.      │
│ Evidence gathering. Hypothesis formation.            │
│ Contact execution. Learning extraction.              │
│ "Execute, observe, learn, repeat."                   │
└─────────────────────────────────────────────────────┘
```

### Zone 1: Agent Autonomy — Expanding Over Time

**Today (2026):** Agents operate within Playbooks. They research, draft, propose. The lead reviews all output before it reaches a buyer. This is correct for phase one — we're building the trust engine.

**Future (2027+):** As Patterns accumulate and Playbooks are validated by 500+ Contact Outcomes, the lead's review threshold rises. An agent can autonomously:
- Contact Organizations with DMPS ≥ 80 using proven angles with HIGH confidence
- Follow up on interested responses without review
- Extract Learning from Outcomes automatically

**Trigger for expansion:** When a Pattern is confirmed by 100+ Outcomes across 30+ Organizations with <5% negative deviation.

### Zone 2: Lead — The Judgment Layer

The lead is the bridge between operational reality and constitutional intent. They:
- Review agent output that falls outside validated Patterns
- Decide when a Pattern is strong enough to promote
- Resolve conflicting Evidence
- Escalate Strategic decisions to the founder
- Identify when a long-held belief may no longer be true

The lead should never be a bottleneck for decisions that have proven Patterns. If the lead reviews every email forever, the company has failed to learn.

### Zone 3: Founder — The Constitutional Layer

The founder decides what kind of company TurnKeySold is. Their decisions are:
- Rare (a few per year once established)
- High-ceremony (documented with rationale, assumptions, and expected outcomes)
- Reversible only through the same ceremony

Founder decisions include: new Principles, Principle changes, Knowledge Model changes, ethical boundaries, new vertical expansion.

### The Escalation Ladder

A decision starts at the lowest possible zone and escalates only when:

1. **Confidence is insufficient:** The agent has LOW confidence in a Hypothesis needed for the decision → escalates for more research or human judgment.
2. **Patterns conflict:** Two Patterns suggest different actions → escalates for resolution.
3. **Stakes exceed zone:** The potential downside of a wrong decision exceeds the zone's authority → escalates.
4. **Novel situation:** No Playbook, Principle, or Pattern covers this scenario → escalates.

---

## Part 3 — Uncertainty and Evidence

### The Confidence Model

Every Hypothesis carries confidence: **HIGH**, **MEDIUM**, or **LOW**.

| Confidence | Definition | Action Threshold |
|---|---|---|
| **HIGH** | Verified by 3+ independent Sources or confirmed by Contact Outcomes | Act autonomously (within Playbook) |
| **MEDIUM** | Supported by 1-2 Sources, logically sound, but not yet confirmed | Propose, human reviews |
| **LOW** | Plausible speculation. Single Source or logical inference only. | Flag for research. Do not act without escalation. |

Confidence is not static. A MEDIUM Hypothesis that receives no confirming Evidence for 3 months should decay to LOW. A LOW Hypothesis that accumulates supporting Evidence should rise to MEDIUM.

### Evidence Sufficiency

"When is evidence sufficient to act?" is the core question of organizational judgment. The answer depends on the stakes of the decision:

| Decision Stakes | Evidence Required |
|---|---|
| **Tactical** (which buyer to contact) | 1 Source identifying the Person + 1 Source confirming their role. MEDIUM confidence sufficient. |
| **Operational** (which angle to pitch) | 3+ Contact Outcomes with similar Organizations showing this angle works. Pattern-level confidence. |
| **Strategic** (bundle pricing) | Comparable sales data + buyer research across all Organizations in the Bundle. HIGH confidence on valuation, MEDIUM on willingness-to-pay. |
| **Constitutional** (new Principle) | 100+ Contact Outcomes, 30+ Organizations, multiple Markets. A Pattern that has survived deliberate attempts to disprove it. |

### The Evidence Quality Weight

Not all Evidence is equal. When Sources conflict, weight by:

1. **Primary > Secondary:** A company's own SEC filing > a TechCrunch article about them.
2. **Recent > Stale:** Evidence from this quarter > Evidence from 2 years ago.
3. **Multiple > Single:** 3 independent Sources agreeing > 1 Source.
4. **Contrary > Confirmatory:** Evidence that contradicts our current Belief deserves extra weight — it's rarer and more informative.

---

## Part 4 — Assumptions

### Assumptions as First-Class Citizens

An Assumption is a special type of Hypothesis: a belief we are acting on **without testing**. Assumptions are dangerous because they're invisible — they feel like facts. The decision architecture must make them explicit.

Every Strategic decision should declare its Assumptions:

```
Decision: Bundle Cold Beer Portfolio at $350K floor
Assumptions:
  1. AB InBev views domain acquisitions as marketing spend, not capex. [MEDIUM confidence — based on industry pattern, not AB InBev-specific Evidence]
  2. The "linguistic moat" narrative resonates with CMOs. [MEDIUM — confirmed for CMSO personas in other industries, not yet for beverage]
  3. A competitor acquiring these domains would create measurable brand damage. [HIGH — this is the core defensive thesis, supported by comparable domain blocking behavior]
Expires: These assumptions should be revisited if no Contact with AB InBev yields a response within 90 days.
```

### Assumption Lifecycle

1. **Declared:** Assumption is stated explicitly when a Strategic decision is made.
2. **Tested:** The first Contact that tests the Assumption produces Evidence.
3. **Confirmed:** Evidence supports the Assumption → becomes Evidence with HIGH confidence. The Assumption label is removed.
4. **Disproven:** Evidence contradicts the Assumption → the Assumption is flagged as disproven. The decision that depended on it is reviewed.
5. **Expired:** The Assumption was never tested within its validity window → the decision is flagged for review.

### The Assumption Audit

Before any Strategic decision is finalized, the lead should ask: "What are we assuming that, if wrong, would make this decision incorrect?" Every answer becomes a declared Assumption.

---

## Part 5 — Conflicting Evidence

### Conflict Is Intelligence

When Source A says X and Source B says Y, this is not a problem — it's a discovery. Something interesting is happening. Conflict resolution is where the company generates its most valuable Learning.

### Resolution Paths

1. **Seek a third Source.** The cheapest path. If Sources C, D, and E all align with A, B was an outlier. Learning: "Source reliability varies."

2. **Weight by Source quality.** A company's own website (saying they have a Spanish division) > a third-party directory (listing them as English-only). Primary Sources resolve most conflicts.

3. **Design an experiment.** "We're not sure if Organization X has a Spanish division. Let's contact them in Spanish and see if they respond." The Contact Outcome IS the resolution.

4. **Escalate to human judgment.** When Sources are equally credible and the conflict matters (e.g., conflicting information about a key decision-maker's role), human intuition and pattern-matching may resolve it.

5. **Accept and track.** Some conflicts cannot be resolved cost-effectively. Flag them as unresolved and revisit when new Evidence naturally arrives.

### Unresolved Conflicts as Knowledge Gaps

The company should maintain a visible list of unresolved conflicts. These are the frontier of our ignorance — the questions we know we can't answer yet. They should inform research priorities.

---

## Part 6 — Experiments

### Every Contact Is an Experiment

Before any Contact is sent, the agent should be able to state:

1. **What we're testing:** "We're testing whether the defensive framing angle resonates with large incumbent Organizations."
2. **What we predict:** "We predict a response rate of 15%+ for this angle with this Organization profile."
3. **How we'll know:** "A response within 14 days counts as a positive Outcome. No response counts as negative. A 'not interested' counts as informative — it tells us something about the angle or the buyer fit."
4. **What we'll learn either way:** "If it works, we have a Pattern. If it doesn't, we know this angle doesn't work for this Organization profile — which is equally valuable."

### Experiment Design Principles

1. **Test one variable at a time.** If we change the angle AND the timing AND the subject line, we can't attribute the Outcome to any of them. Isolate variables.

2. **Run experiments across different contexts.** A Pattern that holds for automotive may not hold for legal. Test across Markets before generalizing.

3. **Pre-register the hypothesis.** Write down what we expect before we test. This prevents hindsight bias ("I knew that would happen") and makes failure honest.

4. **Negative results are results.** A Contact that gets no response is not wasted effort — it produced Evidence. The only wasted Contact is one from which no Learning is extracted.

### From Experiment to Pattern

A single Outcome is an anecdote. Ten consistent Outcomes across different Organizations is a signal. Fifty Outcomes across different Markets is a Pattern.

The transition from "we're testing this" to "this is how we operate" should require:
- **Minimum sample:** 30+ Contact Outcomes testing the same hypothesis.
- **Cross-validation:** Confirmed across at least 3 different Markets or buyer categories.
- **Negative check:** Actively searched for disconfirming evidence and found none significant.

---

## Part 7 — Failure and Learning

### Failure Is a Knowledge Asset

A rejection. A non-response. A deal that falls through. These are not failures — they're Evidence with negative Outcomes. The company's intelligence grows faster from negative Outcomes than positive ones, because they constrain the possibility space more sharply.

**Positive Outcome:** "This angle works for this buyer type." → Narrow. One data point saying "this path is viable."

**Negative Outcome:** "This angle does NOT work for this buyer type." → Broad. Eliminates an entire branch of future attempts.

### The After-Action Review

Every Opportunity that resolves (won or lost) should produce an After-Action Review:

1. **What did we predict would happen?** (From the pre-registered hypothesis)
2. **What actually happened?** (The Outcome)
3. **What did we learn?** (The Learning extracted)
4. **What assumptions did we make that were wrong?** (Assumption audit)
5. **What would we do differently?** (Playbook update recommendation)

### When to Update a Pattern

A Pattern should be re-examined when:

1. **Disconfirming streak:** 5+ consecutive Outcomes contradict the Pattern.
2. **Context shift:** The Pattern was validated in Market A. We're now in Market B. Does it hold?
3. **Time decay:** The Pattern hasn't been confirmed by any Outcome in 12+ months. Market conditions may have changed.

A Pattern that fails re-examination is not deleted. It is archived with: "This Pattern held from [date] to [date] across [N] Outcomes. It appears to have stopped working around [date]. Possible cause: [hypothesis]. Replaced by [new Pattern or 'no replacement yet']."

---

## Part 8 — Principles as Pre-Made Decisions

### How Principles Influence Decisions

A Principle is a decision that has already been made, permanently, until explicitly revised. When an agent faces a choice, the relevant Principles should constrain the option space before the agent even begins deliberating.

**Without Principles:** Agent considers: "Should I include pricing in this email? What are the pros and cons? What happened last time?"

**With Principles:** Agent knows: Principle P5 states "Pricing-free in initial contact." Decision space is already constrained. Agent spends zero cognitive cycles on this question.

This is how Principles scale the company. They eliminate entire categories of decisions that would otherwise consume agent attention.

### When to Create a New Principle

A Pattern becomes a candidate for Principle status when:

1. **Volume threshold:** Confirmed by 50+ Outcomes across 20+ Organizations.
2. **Cross-Market validity:** Holds in at least 3 different Markets.
3. **Harm threshold:** Violating it would cause measurable harm (lost Opportunity, brand damage, regulatory risk).
4. **False-positive rate:** Confirmed in ≥95% of Outcomes where it was tested.

Not every Pattern should become a Principle. Most Patterns should remain Patterns — reliable but revisable. Principles should be rare and stable. The test: "Would we be embarrassed to discover we violated this five years from now?"

### The Principle Governance Process

1. **Proposal:** Any agent or the lead can propose a Principle candidate, citing the Pattern and supporting Evidence.
2. **Challenge period:** The proposal is shared. Any agent is invited to find disconfirming Evidence or counter-examples.
3. **Founder decision:** The founder ratifies or rejects. Ratification is documented with rationale.
4. **Propagation:** The new Principle is added to the Playbooks and agent instructions. All active Opportunities are re-evaluated against it.

---

## Part 9 — Belief Revision

### How the Company Changes Its Mind

Organizations, like individuals, suffer from confirmation bias — we seek Evidence that confirms what we already believe. The decision architecture must actively counteract this.

### Active Disconfirmation

Every quarter, the lead should ask: "What do we believe that might not be true?" This is not a rhetorical exercise. It should produce a list of the company's top 5 Beliefs, ranked by how catastrophic it would be if they were wrong.

For each Belief:
1. What Evidence supports it? (List with provenance)
2. What Evidence would disprove it? (Define the experiment that would change our mind)
3. When was it last confirmed? (Recency check)
4. Has any disconfirming Evidence been observed? (Honest inventory)

This exercise is uncomfortable. It should be. Comfortable organizations don't change their minds until forced to.

### The Belief Revision Threshold

A Belief should be flagged for revision when:

1. **Disconfirming streak:** 10+ Outcomes contradict the Belief after it was established.
2. **Expertise shift:** A new Source with higher authority contradicts the Belief.
3. **Environmental shift:** The market conditions that made the Belief true have changed.
4. **Assumption cascade:** An Assumption the Belief depends on has been disproven.

When a Belief is revised, the old Belief is archived with a clear statement: "We believed X from [date] to [date]. We now believe Y because [Evidence]. The revision was triggered by [event]."

---

## Part 10 — Decision Documentation

### Every Decision Leaves a Trail

A decision is not complete until it is recorded. The depth of recording scales with the stakes of the decision:

**Tactical decisions** (Contact sent, follow-up scheduled) → logged automatically. Minimal ceremony.

**Operational decisions** (Angle chosen, pricing offered) → recorded with: what was decided, based on what Pattern or Hypothesis, expected outcome.

**Strategic decisions** (Bundle pricing, new buyer category) → full Decision Record:

```
Decision: [What was decided]
Date: [When]
Decided by: [Who]
Authority zone: [Strategic]
Based on: [Evidence, Patterns, Learning cited]
Assumptions: [Declared Assumptions with confidence levels]
Expected outcome: [What we predict will happen]
Success criteria: [How we'll know if this was the right decision]
Review date: [When we'll revisit this decision]
Dissenting views: [Who disagreed and why — optional but valuable]
```

**Constitutional decisions** → same as Strategic, plus:
- Challenge period documentation (who challenged, what Evidence they cited)
- Ratification rationale
- Propagation plan

### The Decision Audit Trail

Any agent should be able to ask: "Why did we decide to price the Cold Beer Portfolio at $350K floor?" and trace the decision back through:
1. The Decision Record
2. The Evidence and Patterns it was based on
3. The Assumptions it declared
4. The Outcomes that followed

This audit trail is how the company learns from its own judgment — not just from Contact Outcomes, but from the quality of its decision-making process.

---

## Part 11 — CTO Critique of the Knowledge Model

The Knowledge Model (KNOWLEDGE_MODEL.md) was designed before the Decision Architecture. Now that we've designed how the company acts, three gaps emerge.

### Gap 1: Assumption Is Missing

**Problem:** The Knowledge Model treats Assumptions as a type of Hypothesis. But Assumptions are fundamentally different — they're beliefs we're acting on WITHOUT testing. They're the invisible scaffolding of every Strategic decision.

**Proposal:** Add **Assumption** as a fundamental concept in the Knowledge Model. It is not derived from Hypothesis — it's a distinct category of knowledge with its own lifecycle: Declared → Tested → Confirmed/Disproven → Expired.

**Why this matters:** The company's most expensive mistakes will come from Assumptions that felt like Facts but weren't. Making Assumptions explicit is the first line of defense.

### Gap 2: Experiment Is Missing

**Problem:** The Knowledge Model has Hypothesis → Contact → Outcome, but doesn't formalize the experimental method. A Hypothesis tested through Contact is an Experiment, but the concept doesn't exist.

**Proposal:** Add **Experiment** as a derived concept: a Group of Contacts designed to test a specific Hypothesis, with pre-registered predictions and success criteria.

**Why this matters:** Without Experiment as a concept, the company cannot distinguish between "we tried this and it happened to work" and "we systematically tested this across conditions and confirmed it works." The former produces anecdotes. The latter produces Patterns.

### Gap 3: Belief Is Missing

**Problem:** The Knowledge Model has Facts (individual verified truths) and Hypotheses (individual unverified guesses). But the company's internal state — "based on everything we know, what do we believe about Organization X?" — is not captured. Belief is the aggregation of Facts, Evidence, and Patterns into a coherent picture.

**Proposal:** Add **Belief** as a derived concept: the current best understanding of an entity (Organization, Market, Domain) based on all accumulated Evidence and Patterns. A Belief is not a Fact — it can be wrong. But it should be the company's honest answer to "what do we think?"

**Why this matters:** When a new agent asks "what do we know about AB InBev?" they should get a Belief — a synthesis, not a list of 47 individual Facts.

### What the Knowledge Model Got Right

The core loop (Source → Evidence → Hypothesis → Contact → Outcome → Learning → Pattern → Principle → Playbook) is sound. The spiral model of organizational learning is correct. The emphasis on Concepts over implementation is exactly right. These additions strengthen the model without changing its architecture.

---

## Part 12 — What Makes an AI-Native Company Decide Better Than Competitors

### The Competitive Advantage

TurnKeySold's decision advantage comes from three structural properties that traditional companies cannot easily replicate:

**1. Every decision leaves a trace.** In a traditional company, the CMO sends an email, gets a response, and moves on. No Learning is extracted. No Pattern is updated. The next CMO starts from zero. At TurnKeySold, every Contact Outcome feeds the Learning engine. The 1,000th Contact is informed by the previous 999.

**2. Principles scale judgment.** In a traditional company, every new hire must be trained on "how we do things here." That training is inconsistent, incomplete, and decays as people leave. At TurnKeySold, Principles are code. They constrain every agent's decision space without requiring the agent to understand why — though understanding why is always available through provenance.

**3. Assumptions are hunted, not hidden.** Traditional companies make decisions on implicit assumptions they don't know they're making. When those assumptions are wrong, the failure is mysterious — "we don't understand why the strategy didn't work." At TurnKeySold, Assumptions are declared, tested, and when disproven, the decision based on them is automatically flagged for review.

### The Gap to Close

The company currently cannot do any of this automatically. The Knowledge Model exists. The Decision Architecture exists. But the bridge between them — the operational system that extracts Learning from Outcomes, promotes Patterns, flags Assumptions, and surfaces Beliefs — does not exist. That is Phase 2 and beyond.

---

## Summary: The Reasoning Organization

```
                ┌──────────────────────────────────────┐
                │         PRINCIPLES (Pre-made)          │
                │    Constrain decision space a priori    │
                └──────────────────────────────────────┘
                                │
                                ▼
EVIDENCE ──→ BELIEF ──→ HYPOTHESIS ──→ DECISION ──→ ACTION ──→ OUTCOME
   │            │            │            │            │           │
   │            │            │            │            │           ▼
   │            │            │            │            └──→ LEARNING
   │            │            │            │                      │
   │            │            │            │                      ▼
   │            │            │            └──→ Documented       PATTERN
   │            │            │                 with Assumptions    │
   │            │            │                                     ▼
   │            │            └──→ Confidence gates              PRINCIPLE
   │            │                 action threshold                 │
   │            │                                                  ▼
   │            └──→ Assumptions made explicit               PLAYBOOK
   │                 before action is taken                      │
   │                                                             ▼
   └──→ Sources weighted, conflicts resolved          Future decisions
        before Belief is formed                          improved
```

**The company's intelligence is not in any agent, document, or database. It is in the accumulated Learning that crosses every Decision, every Outcome, every Contact — systematically extracted, generalized into Patterns, codified into Principles, and fed back into the next iteration.**

*This document describes how an organization reasons, not how software behaves. Implementation follows architecture, not the reverse.*
