# Agentic Payments — US-Funded Startups (Owner-Supplied External Research)

**Date received:** 2026-10-25 · **Provenance:** owner-supplied, researched with an external LLM (pasted verbatim below) · **Status of figures: EXTERNAL-UNVERIFIED** per §9.7 until this team verifies each claim with a literal published source URL. Source-of-truth = this file (full-field rule).

**CRITICAL RECONCILIATION FLAGS for this team (lead, 2026-10-25):**
- **Rye — ACQUISITION CLAIM:** the source states Rye (a16z-backed universal checkout API, $14M raised per our verified Tier-2 pass PR #87) "was acquired by Jolly in September 2026 — the first real consolidation signal in agentic checkout." If true, Rye's buyer/valuation data in our records is stale and any Rye outreach targeting is invalid. **Verify FIRST — highest priority in this integration.**
- **Figure deltas vs our verified records:** Payman "~$13.8M over 3 rounds" vs our verified $13M (PR #87 reconciliation said $13M company-primary); Skyfire "$9.5M" vs our verified $8.5M seed + DCVC line (keep $8.5M per PR #87 evidence); Basis Theory "$50M+ total" vs our verified $33M Series B (Costanoa-led, Oct 2025 — the $50M+ total may include earlier rounds; verify); Natural "$40M total — $9.8M seed + $30M Series A (Forerunner, Jul 2026)" — our Tier-1 pass had Natural as a top target, verify the Series A; Catena Labs "~$48M — $18M seed (a16z crypto, May 2025) + $30M Series A (May 2026)" vs our Tier-1 record; Crossmint "$23.6M Ribbit (Mar 2025) + Circle Ventures (Sep 2025)" — matches our Tier-1 closely.
- **New companies NOT in our ~31-company buyer system:** Monid (SF, "checkout counter for AI agents," claimed $7.7M seed Oct 2026), Highnote (SF, card issuing + Visa agentic-commerce work May 2026, claimed $173M total/$90M Series B/~$750M valuation — genuinely new and the largest), Lithic (NY, programmable virtual cards, claimed $100M+ incl. $43M Series B). These become onboarding candidates for the payments master CSV.
- Watchlist re-confirmations: Skyfire, Payman AI (pivoting to "agentic banking" per source), Nekuda (our records: KILL-flagged — site dead per Wayback evidence PR #90-era verification; the source still lists it as a Visa Intelligent Commerce launch partner — reconcile: is nekuda.com live again?).

---

## External research transcript (VERBATIM — source authority)

**Question asked:** find agentic or ai payment startups which are well funded and based in the USA

**The short answer**

US agentic-payment pure plays are still a small, thinly funded cohort — most rounds are seed-to-Series A, and only a handful have crossed $20M. The real capital concentration is one layer down, in card issuing and tokenization infrastructure that agents actually transact through. Below is what's confirmed by funding announcements as of October 2026.

### Core agentic-payment startups (US, $20M+)

| Company | HQ | What it does | Funding |
|---|---|---|---|
| Natural | San Francisco | Orchestration layer that lets AI agents hold funds, pay vendors, collect money, and transact with other agents — explicitly positioned against Stripe. Launched Oct 2025, product live Jul 2026. | $40M total — $9.8M seed (Oct 2025) + $30M Series A led by Forerunner (Jul 2026) TechCrunch |
| Catena Labs | Boston | "AI-native financial institution": banking, treasury and governance rails for agents over cards, ACH and wires. Founded by Circle co-founder Sean Neville; filed for an OCC national trust bank charter. | ~$48M — $18M seed led by a16z crypto (May 2025) + $30M Series A co-led by a16z crypto and Acrew (May 2026) a16z |
| Basis Theory | San Francisco | Processor-agnostic, PCI-compliant tokenization vault — the credential layer agent checkout runs on. Leads the 20+ member Agentic Commerce Consortium (Lithic, Skyfire, Crossmint, Rye). Customers include Pinterest, Melio, MoneyGram. | $50M+ total — $33M Series B led by Costanoa (Oct 2025) Press release |
| Crossmint | San Francisco | Gives agents a wallet, virtual card and stablecoin balance via one API — card + stablecoin orchestration in a single stack. Circle Ventures strategic investor. | $23.6M+ — $23.6M led by Ribbit Capital (Mar 2025), plus Circle Ventures investment (Sep 2025) Crossmint |

### Adjacent, but where the volume actually is

These aren't agentic-payment pure plays, but they're the funded infrastructure agents run on — and both are shipping agent-specific products.

| Company | HQ | Relevance | Funding |
|---|---|---|---|
| Highnote | San Francisco | Card issuing + program management; launched agentic-commerce work with Visa for AI-initiated payments (May 2026). | $173M total; $90M Series B (Jan 2025) + $25M extension; ~$750M valuation |
| Lithic | New York | Programmable virtual cards with per-agent spend controls; already seeing agents spend on Lithic-issued cards. | $100M+ raised (incl. $43M Series B) |

### Watchlist: strategically backed, not yet "well funded"

- Skyfire — San Francisco — KYAPay agent identity + payment network; $9.5M (a16z CSX, Coinbase Ventures, Neuberger Berman). Running production volume but the smallest war chest of the identity players.
- Payman AI — US — agent wallets with programmable spend rules, now pivoting to "agentic banking" sold to banks/credit unions; ~$13.8M over 3 rounds, Visa-backed, selected for ICBA ThinkTECH 2026.
- Nekuda — US — agent wallet SDK + "Agentic Mandates"; Visa Intelligent Commerce launch partner; $5M seed (Madrona, Amex Ventures, Visa Ventures).
- Monid — San Francisco — "checkout counter for AI agents"; $7.7M seed (Oct 2026).

One exit to note: Rye, the a16z-backed universal checkout API ($14M raised), was acquired by Jolly in September 2026 — the first real consolidation signal in agentic checkout.

### How to read this market

Three things separate the winners from the noise:

1. Regulatory moat beats API moat. Catena's bank charter filing is the most defensible move in the cohort — payments infrastructure without a charter is a feature Stripe can bundle. Natural is betting the opposite: that speed and architecture beat incumbency.
2. The card networks already own distribution. Visa Intelligent Commerce, Mastercard Agent Pay and Visa TAP are absorbing the trust/identity layer. Startups that survive there (Skyfire, Nekuda, Basis Theory) are the ones the networks chose as launch partners, not the ones competing with them.
3. Funding is thin relative to the thesis. Dealroom counts 112 startups building payments for AI agents, yet most disclosed rounds are under $10M — this is a category where a $30M Series A still makes you top-three funded.

**Caveat (source's own):** "well funded" here means disclosed equity rounds ≥$20M with US headquarters; several of these companies are remote-first, and private valuations beyond Highnote's aren't public.
