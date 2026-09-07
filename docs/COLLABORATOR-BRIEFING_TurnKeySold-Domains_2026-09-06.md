# TurnKeySold Domains — Agentic System Briefing
**Prepared for:** an external LLM agentic system being onboarded as a collaborator
**Date:** 2026-09-06 · **Author:** agent-lead (team lead/operator) · **Owner:** Juan L. Aguirre
**Status of this doc:** factual summary of the system as it stands. No revenue figures are claimed anywhere — the domain sale (LeanMeds.com) closed outside Stripe, and no reliable number has been verified.

---

## 0. Quick Summary (TL;DR)

**TurnKeySold Domains** is an AI-native sales operation that sells premium domain names (146 owned domains, asking prices $3K–$45K) on a 20% success-fee model. A small agent team (1 lead + 3 specialist agents) runs the full agentic sales pipeline: buyer research → scoring → outreach copy → review → owner-executed sends. In ~10 weeks it has produced 146 researched domains with DMPS-scored buyer lists, 146 outreach briefs, 147 short-message sets, verified exec contact sheets, two buyer-identification methodologies (homegrown + owner-supplied), ~100 net-new verified buyer targets, 30 ready LinkedIn notes, 4 held email packs (~19 leads), 3 real first-touch emails (no replies yet), and 1 completed sale (LeanMeds.com, via marketplace).

**The single most important operational fact right now: the owner has ordered a send-freeze (2026-09-04). Nothing is sent — email, DM, or form — without the owner's explicit per-send instruction. All output is "ready copy" until then.** The funnel has effectively zero measured reply-rate data so far; the methodology is proven at the research level, unproven at the response level.

A second agentic system is being onboarded as a collaborator (this doc). Suggested integration: start read-only against the shared repo/folder, take one bounded workstream first (best candidates: response-handling playbook, per-campaign landing pages, or send/outcome tracking), and only then converge on shared repo conventions. Hard rules any collaborator must honor: never-invent sourcing, the send-freeze, no pricing in first-touch copy, and members don't push to main (lead reviews and merges).

---

## 1. What Is TurnKeySold Domains

TurnKeySold Domains is the first vertical of **TurnKeySold**, a parent brand building an "agentic sales OS" — AI agents that handle the entire sales process autonomously: buyer research, strategic positioning, personalized outreach, objection handling, and negotiation.

The domain vertical was chosen deliberately as the proving ground because:
1. **Inventory already exists** — the owner holds 146 domains.
2. **Domains are a hard sales problem** — no physical form, no obvious buyer, prices from $1K to $600K. Selling them systematically requires exactly the skills that transfer to anything else (SaaS, consulting, M&A).
3. **Every sale exercises the full pipeline** — deep buyer intelligence and strategic framing, not just listing and waiting.

The business thesis: *"If we can build agents that systematically sell domain names, we can sell anything."*

Future planned verticals: TurnKeySold SaaS, TurnKeySold Consulting, TurnKeySold M&A — same research frameworks, scoring systems, and outreach pipelines applied to new inventory.

**Commercial model:** 20% success fee per domain sold, no upfront fees. Internal qualification: domains valued $5K+, brandable, clear industry use.

## 2. Goal and Purpose

**Business goal:** sell the 146-domain portfolio by proactively finding and contacting the *exact right buyer* for each domain — companies for whom the domain is a brand upgrade, a category-defining name, or a defensive necessity — rather than passively listing on marketplaces.

**System goal (the real one):** develop and prove a repeatable agentic sales methodology. Each campaign is a test of the machine, not just an attempt at one sale. KPIs being tracked:
- Reply rate (% of outreaches answered)
- Qualified leads per domain
- Conversion rate (domains sold ÷ campaigns run)
- Average sale price vs. initial asking
- Revenue per campaign
- New-lead yield (% of buyers surfaced that were absent from prior sheets — pilot avg ~3.6/domain)

**Positioning vs. incumbents:** marketplaces (Sedo, Afternic, Dan) are passive — they wait for a buyer to search. TurnKeySold runs proactive, researched, personalized outreach to named decision-makers, with human (owner) review before anything is sent. Tagline: *Premium domains, sold on purpose.*

## 3. What We've Built So Far — and the Steps

**Timeline: business created 2026-06-24; plan now at Rev 13. All code/docs live in `cerebraino/TurnKeySold` (main `a7b7e72`, 54 merged PRs); shared work files in `/home/team/shared/`.**

### Step 1 — Foundation (late June–July)
- Business plan drafted and owner-ratified; team assembled (see §4).
- All **146 domains** inventoried and researched: comparable-sales appraisals, buyer categories, and **DMPS-scored lead lists** (Domain-Market-Persona-Score, our fit-scoring rubric) — 146/146 complete.
- Top 25% by value identified: **36 domains, cutoff $15K** — these get priority campaigns.

### Step 2 — Outreach assets (July–August)
- **146/146 outreach briefs** — per-domain pitch context, bilingual (FR/ES/EN) where relevant, strictly pricing-free.
- **147/147 micro-messages** — three-line short messages (150–300 chars): hook tied to the buyer's real work → what the domain is → light ask. Machine-verified length, no links, no pricing.
- **Email packs 145/146** (the one gap is the already-sold leanmeds.com).
- **Verified exec contact sheets** — named decision-makers with source URLs. Rule: *fireable* = literally published + real source. Guessing patterns (first@, flast@) is forbidden.
- **Google Alerts v2** for 140 domains (timing signals: funding, launches, leadership changes).
- 8 domains enriched with structured Google-ads competitor data.
- 13 deep-dive buyer expansions; **300+ companies identified with named executives.**

### Step 3 — Methodology #2 (2026-08-30)
- Owner supplied a second methodology skill: **`domain-outbound-lead-researcher`** — prioritizes exact company/product-name matches, sibling-domain upgrades, precise use-case matches, and commercial timing signals over broad industry prospecting.
- Decision: **both methods run; the new one is additive, not a replacement.** Hardened rules adopted the same day: never-invent (every claim needs a source URL), no autonomous sending, no pricing in first-touch copy.

### Step 4 — Validation runs (Aug 30 – Sep 3)
- **Pilot:** 8 top-25% domains → **29 NEW buyer targets, 28 live-verified** (~3.6/domain). Strongest: knowlaw.ai (7), nofail.ai (6). Weakest: payauto.ai, hispanoabogado.com (1 each — already saturated).
- **Scale run:** corrected 15-domain set → **~53–55 NEW live-verified targets vs ~197 baseline** — yield held consistent at 2× scale.
- **Full expansion approved on 4 highest-ROI domains** (curebyketo.com, fusebot.ai, weputt.com, paretobuddy.com): WAF re-verification + contact paths (27 leads; invalid leads flagged: a gambling-spam domain, a dead site), then 4 email packs (~19 fireable leads).

### Step 5 — First real sends + freeze (Sep 3–4)
- **3 first-touch emails sent** (owner-approved, addresses verified against exec-contact research): Zócalo Health (latinomedico.com), Taskade (oneguy.org), Founder Institute (oneguy.org). **Zero replies so far.**
- **Owner ordered a full send-freeze (2026-09-04):** no emails, DMs, form submissions, or follow-ups of any kind without explicit per-send instruction. Pre-written D3/D7/D14 cadences paused. Everything since is ready-copy.

### Step 6 — Ready-copy buildout under freeze (Sep 4–6)
- **30 LinkedIn connection notes** (3 batches: 2 general + 1 LaVoiture-specific), each ≤300 chars, machine-verified, no pricing/links/invented facts.
- **LaVoiture.ai (first client campaign):** top-10 buyer list + FR/EN notes; a re-verification wave caught **5 CEO changes** (Stellantis, Renault, Verkor, ACC, Einride) — corrections folded into the repo with sources; 10 additional **Montreal/Quebec round-2 contacts + 10 French-first messages** (with honest confidence flags on 2 weaker-sourced contacts).
- **Repo hygiene:** stale-exec row fixes (PagerDuty, Stripchat), HOLD banners on all packs, and — per new owner rule — **all generated lead lists/messages now live in both the shared folder and the repo** (PRs #53–54).

### Cumulative output (one line each)
146 researched domains · 146 briefs · 147 micro-message sets · 145 email packs · verified contact sheets · 2 methodologies · ~100 net-new verified buyers · 30 LinkedIn notes ready · ~19-lead email expansion held · 3 real sends (0 replies) · 1 sale (LeanMeds.com) · 127/127 kanban tasks completed · 54 PRs merged.

## 4. How the System Works

### Team topology
| Agent | Role |
|---|---|
| **agent-lead** (operator) | Plans, delegates, monitors; reviews every task; verifies claims; merges all PRs; sole interface for sends/finance decisions; talks to the owner |
| **agent-domain-researcher** | Valuation, comparable sales, buyer identification, exec prospecting, lead lists — web research with source URLs |
| **agent-outreach-architect** | Campaign design, persona messaging, sequences (D3/D7/D14 cadences), response-handling playbooks |
| **agent-web-developer** | Sites/pages from briefs (available for campaign landing pages; currently underused) |

### The work loop
1. **Owner directive or lead plan** → task created on a kanban board (backlog → in-progress → review → done) with full context in the assignment message.
2. **Assigned member executes** against the brief — research, copywriting, or build — writing artifacts to `/home/team/shared/`.
3. **Lead review** (the quality gate): deliverable verified against the never-invent rule (source URLs checked, counts re-computed, char limits machine-verified, duplicates excluded, confidence flags required). Weak submissions are rejected with feedback.
4. **Repo commit:** member produces a local branch → lead reviews the diff → squash-merge via PR. **Members cannot push to main.**
5. **Ready-copy state:** approved messages/lists sit in the shared folder + repo, clearly banner-ed, awaiting the owner.
6. **Sends are human-only right now:** the owner executes LinkedIn DMs, site forms, or approves email from the business inbox. The lead never sends autonomously.

### Data & tooling
- Shared SQLite board (`team-db`) for tasks; shared folder for artifacts; GitHub repo as source of truth for docs/research.
- Business email inbox (AgentMail/SES) — used once, now frozen; bounces/complaints are platform-tracked and reputation is treated as a shared asset.
- Research tooling: web search, real-browser verification for WAF-protected sites, Google Alerts for timing signals.

### Quality rules (non-negotiable, enforced at review)
1. **Never-invent** — every factual claim carries a real source URL; only literally published contacts are fireable.
2. **Current-title verification** — exec churn is real (5 CEO changes caught in one wave); stale names may appear only inside explicit "never fire on these" warnings.
3. **No pricing in first touch** — price conversations happen after a reply.
4. **Honest confidence labeling** — weakly-sourced contacts get M-confidence flags + [VERIFY-BEFORE-USE] tags, never laundered.
5. **Honesty in copy** — no invented relationships, no false urgency, easy opt-out; platform reputation (bounce/complaint tracking) protects the whole team.

## 5. Current Challenges and Issues

1. **Send-freeze = zero funnel data.** The methodology is proven at research level (yield ~3.6 new buyers/domain held at 2× scale) but **unproven at the response level**: 3 lifetime sends, 0 replies, no reply-rate baseline. Every strategic decision (which hooks, which channels, which domains) is currently an educated guess.
2. **Manual-send bottleneck.** Most high-value leads have no fireable email — routing is LinkedIn-DM or site forms, executed by hand by the owner. Cold-email infrastructure exists but is reputationally fragile and freeze-bound; scraping/guessing addresses is prohibited.
3. **Contact-verification decay.** Exec data goes stale fast (the PagerDuty/Tejada row and 5 French-auto CEO changes were both caught *after* initial merge). Verification is one-pass at creation; there is no scheduled re-verification, and 2 Montreal contacts still carry M-confidence flags.
4. **Unproven close.** One sale exists (LeanMeds.com, via marketplace, outside the outreach pipeline). No negotiated deal has yet run through the agentic pipeline end-to-end; pricing floors and negotiation playbooks exist on paper only.
5. **Machine constraints.** The work computer is ~4GB RAM with no swap; leaked shells cause recurring OOM events that kill sessions. Manageable (cleanup procedure exists) but it's the main operational friction.
6. **Copy volume vs. signal.** 30 LinkedIn notes + ~19 email leads + 10 Montreal messages are ready, but under the freeze none have produced signal. There's a risk of over-investing in more ready copy while the top of the funnel is untested.
7. **Two-methodology overhead.** Running homegrown DMPS + the owner-supplied skill doubles research effort per domain; the merge rules are clear but deduping and confidence-tracking take real review time.

## 6. Recommendations — Selling Domains More Effectively

**Priority-ordered; the first three unblock everything else.**

1. **Lift the freeze in small measured waves.** 5–10 sends per wave (start with the highest-DMPS, best-sourced contacts), fixed copy, tracked per-contact. Without a reply-rate baseline nothing else can be optimized. The 3-sends-so-far sample is too small to learn anything from.
2. **Stand up minimal send/outcome tracking before wave 1.** A single table (contact, domain, channel, copy variant, sent date, follow-ups, reply, outcome) — even a spreadsheet — turns every future wave into data. Today there is no system of record for outreach state.
3. **Build the response-handling playbook now, so replies aren't improvised.** Reply templates (interested / not interested / "how much" / wrong person), the D3/D7/D14 cadence rules, and a negotiation band per domain (asking price vs. walk-away floor). The moment the freeze lifts, response latency becomes a closing factor.
4. **Lead with timing signals, not generic fit.** The best hooks in the current pipeline are events: Communauto's succession window, Groupe Touchette's new co-CEO structure, Taiga's relaunch, funding rounds from the alerts feed. Rank outreach waves by *recency of trigger*, not only by DMPS score.
5. **A/B the three-line framework against a slightly longer personal note** (4–6 lines, one concrete observation about the buyer's business). 150–300 chars may be too short to earn a reply from a busy CEO; test both on similar contacts and measure.
6. **Use the web-developer for per-campaign landing pages.** A clean one-pager per domain-for-sale ("what it is, why it fits this industry, contact form, no price") gives every DM/form message a credible destination and captures inbound interest — currently a cold message has nowhere to send people except a reply.
7. **Add a passive backstop:** list the top domains on Sedo/Afternic/Atom concurrently with proactive outreach. It's complementary, not contradictory — inbound marketplace interest validates pricing and occasionally closes while outbound nurtures.
8. **Prepare the close infrastructure.** Escrow.com flow, transfer steps per registrar, and a standard offer letter. A deal that stalls for two weeks on logistics can die; the sale process should be as engineered as the outreach.
9. **Quarterly (or per-wave) exec re-verification** for any contact about to be fired, and auto-flag leads older than ~60 days. The CEO-change catches prove staleness is the norm, not the exception.
10. **Bundle and ladder the portfolio.** The .online/.ai pairs (puticlub, putero) are already priced as bundles; extend the idea — sell thematic sets (e.g., the Spanish adult cluster to one buyer) where one negotiation moves several assets.

## 7. How the Collaborating System Can Plug In

Suggested phased integration (matches the owner's "collaborator, possibly shared repo later" intent):

- **Phase 0 — read-only (day 1):** clone `cerebraino/TurnKeySold`, read `REPO_INDEX.md`, the business plan (Rev 13), `docs/outreach/` and one domain folder (`DOMAINS/lavoiture.ai/`) end-to-end. That's the whole system in miniature.
- **Phase 1 — one bounded workstream, no sends:** best candidates, in order: (a) **response-handling playbook** (§6.3), (b) **send/outcome tracking schema** (§6.2), (c) **per-domain landing pages** (§6.6). Deliverables land as PRs or shared-folder files, reviewed by the lead, same quality gates.
- **Phase 2 — shared repo:** converge on conventions (branch naming `docs/…`/`research/…`, PR review by lead, HOLD banners on anything sendable, members never push main directly).
- **Standing rules for any collaborator:** honor the send-freeze absolutely; never-invent with source URLs; no pricing in first-touch copy; label confidence honestly; don't re-approach the already-handled contacts (3 emailed, 30 LinkedIn-note recipients) without new owner instruction.

---

## Appendix A — Key paths
- Repo: `github.com/cerebraino/TurnKeySold` (main `a7b7e72`) — `REPO_INDEX.md` is the map.
- Domain folders: `DOMAINS/<domain>/01-research/` (leads, contact sheets) + `02-outreach/` (briefs, micro-messages, email packs).
- Batch files: `DOMAINS/lavoiture.ai/01-research/LAVOITURE-{TOP10_2026-09-04, MTL-10_2026-09-05}.md`, `02-outreach/LAVOITURE-MTL-10-MESSAGES_2026-09-05.md`, `docs/outreach/{LINKEDIN-CONNECT-10*, FIREABLE-OUTREACH_2026-08-30}.md`.
- Held packs: `DOMAINS/…/02-outreach/email-pack_*.md` (HOLD-bannered) + `/home/team/shared/outreach-pack_*.md`.
- Methodologies: `docs/domain-outbound-lead-researcher.md`, `COMPANY/research-framework.md`, `docs/methodology/three-line-outreach-framework.md`.
- Governance: `docs/architecture/DECISION_ARCHITECTURE.md`, `/home/team/shared/WORKFLOW.md`.

## Appendix B — Glossary
- **DMPS** — Domain-Market-Persona-Score: our 0–100 buyer-fit rubric per lead.
- **Fireable** — a contact literally published with a real source URL (the only kind that may ever be sent).
- **Three-line framework** — hook (their real work) → what the domain is → light ask; 150–300 chars, no links/pricing.
- **Ready copy / HOLD** — approved content awaiting the owner's per-send instruction; never sent autonomously.
- **New-lead yield** — buyers surfaced by methodology #2 that were absent from prior sheets (pilot avg ~3.6/domain).

*End of briefing. Questions or corrections route through the owner to agent-lead.*
