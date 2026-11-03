# agentbucks.si — Buyer Research (.si wave, task `siwave-5domain-20261025`)

**Date:** 2026-10-25 (board task) · **Evidence fetched:** 2026-11-03 UTC · **Researcher:** domain-researcher
**Scope:** buyer research **only** — no outreach copy, no valuation ladder, no price recommendation. Options-only.
**Register facts:** Namecheap · Active · expires **Oct 18 2027** · auto-renew **ON** · renewal price TBD (registrar-side, out of scope).
**Freeze status:** SEND FREEZE untouched — research only, nothing fires.

---

## §0 Method & discipline

Same wave discipline as `DOMAINS/cardbot.si/01-research/CARDBOT_SI-RESEARCH-2026-10-25.md` §0. Never-invent (no email asserted), no WAF evasion (403/000 recorded), price-provenance on every figure (`docs/assets/SI-WAVE-COMP-REGISTER_2026-10-25.csv`).

**Term analysis:** "agent bucks" = **the unit of account for AI agents** — agent payments, agent credits, agent incentives/rewards. It is a *coinage*, not a dictionary term, which cuts both ways: no incumbent to fight, but also no established search demand. Sibling-TLD check was therefore the primary test (§2), and it came back **decisive**.

---

## §1 `.si` market context (shared)

> ".ai has a new baby brother, Slovenian ccTLD **.si**, that is also making waves as an acronym for 'super intelligence'… Atom's **$50,000 sale of OpenRouter.si** and Spaceship's sale of **Staffing.si** at the same price."
> — DNJournal, <https://www.dnjournal.com/domainsales.htm>, fetched 2026-11-03 · **VERIFIED**

Relevant to *this* domain specifically: **`OpenRouter.si` — $50,000 (Atom.com)** is the top `.si` comp in the chart and it is an **AI-infrastructure** name, not a Slovenia-local name. That is the closest thing to proof that `.si` is being bought as an AI acronym by AI-native buyers — exactly the buyer class `agentbucks.si` needs.

Also in the same chart: **`X402.si` + `QA.si` sold for $7,839** (x402 = agent-payments protocol). Two agent-economy `.si` sales in one fortnight.

Compound `.si` comps (our structural class — `agentbucks` is a compound): CarInsurance.si $5,001 · HyperFocus.si $3,599 · guidelines.si $3,360 · Cubby.si $2,295 · Schema.si $2,000.

Registry: ARNES (Ljubljana); port-43 WHOIS refused, policy pages 404 on 2026-11-03 — **recorded, not circumvented**; **eligibility NOT VERIFIED**.

---

## §2 Sibling-TLD landscape (WHOIS-verified 2026-11-03) — the decisive finding

| Domain | Status | Evidence | Reading |
|---|---|---|---|
| **agentbucks.ai** | **Registered 2026-05-26** (Cloudflare, Inc.) · expires 2028-05-26 · registrant country **US**, name redacted — and it **serves a live, login-gated application**: page copy *"Welcome Back! Log in or create account to get back to your dashboard!"*, built on Next.js + Clerk, meta description *"AI workspace for projects, brands…"* | `whois.nic.ai` + HTTP 200 | **Someone is operating a product on `agentbucks.ai` right now, registered in May 2026.** That is a current, active, AI-native operator for this exact coinage — and they do **not** hold the `.si`. |
| **agentbucks.com** | Registered **2012-02-08** (Mesh Digital Limited) · expires 2027-02-08 · status `ok` · **no HTTP response** (curl 000) | `whois.verisign-grs.com` + HTTP check | A long-held `.com` that serves nothing. Holder unknown (privacy). |
| **agentbucks.io** | **UNREGISTERED** ("Domain not found") | `whois.nic.io` | A second registration gap beside our `.si`. |
| agentbucks.si | Ours (parked, 162.255.119.74) | register + `dig` | — |

**Sibling-TLD insight (the point of this domain):** the term is **taken on `.ai` by a live product** and **free on `.io`**, with a dormant `.com`. For a buyer, the realistic brand-protection set is `agentbucks.ai` (held) + `agentbucks.si` (ours) + `agentbucks.io` (free). **We are the only party holding a ccTLD leg of a brand that is already operating.** The operator's identity is *not* public on their own login page — no name, no email, no company is asserted here.

---

## §3 Buyer map (12 targets, ranked)

### Tier A — the sibling holder (highest priority, exact-name match)

| # | Party | Fit | Route | Caution |
|---|---|---|---|---|
| A1 | **Operator of `agentbucks.ai`** (US registrant; product live since ≤2026-05-26) | **Exact name, already operating, AI-native.** A live product with no ccTLD cover is precisely the profile that buys the second leg. | Not published on their public page → must be sourced (site footer / LinkedIn / registrar-side) before any approach | **Identity NOT SOURCED.** Registrant is privacy-redacted. Do not guess a company name, do not invent an address. |

### Tier B — agent-payments / agent-economy infrastructure (the "bucks" half of the coinage)

All verified live 2026-11-03 (HTTP 200):

| # | Company | What they build (verbatim) | Why `agentbucks.si` | Route |
|---|---|---|---|---|
| B1 | **Payman AI** | "Agentic AI That Does the Banking. Under Your Control." | Agents that hold and move money need a unit-of-account brand; "bucks" is the consumer word for it. | corp/site form |
| B2 | **Skyfire** | "The Agent Trust Stack" | Agent identity + payment rails; a credits/currency product line fits. | Amir Sarhangi — **VERIFIED (skyfire.xyz)** |
| B3 | **Nevermined** | "Payments Infrastructure for AI Agents" | Agent metering/payments — "bucks" is literally the metering unit. | site/LinkedIn |
| B4 | **Catena Labs** | "How AI Agents Use Money" | The phrase is their homepage thesis. | site/LinkedIn |
| B5 | **Natural** | "Powering agentic payments" (**"Our $30M Series A July 20"** — VERIFIED, 2026-11-03) | Funded, launching, agent-payments native. | site/LinkedIn |
| B6 | **Crossmint** | "Stablecoin Platform & APIs for Enterprises" | Enterprise agent wallets → agent balance brand. | site/LinkedIn |
| B7 | **Causa Prima** | "Agent-to-agent network for finance teams" (**"We raised $20 million funding"** — VERIFIED 2026-11-03; conflicts with repo $30M) | Agent-to-agent settlement. | Maex Ament — **VERIFIED (causaprima.com/about)** |

### Tier C — EU / `.si`-regional AI & payments

| # | Company | Status | Fit |
|---|---|---|---|
| C1 | **NAKA (formerly Eligma)** — <https://eligma.com> serves "NAKA" | Rebrand observed 2026-11-03 | Slovenia's best-known AI/payments-adjacent brand in a rebrand cycle; weak on the coinage, but the `.si`-native party most able to *use* an AI-flavoured `.si` |
| C2 | **CargoX** — <https://cargox.io> | 200 | Weak |
| C3 | **Bitstamp** — <https://bitstamp.net> | 200 | Weak (SI-founded exchange) |
| C4 | **NiceHash** | 000 — unresponsive | Recorded, not contacted |
| C5 | **Mangopay** — <https://mangopay.com> | 200; homepage "€68B transactions processed" (VERIFIED) | EU multi-party flows; weak on the coinage |

**`.si`-native verdict: THIN for the term, but the `.si` market itself is demonstrably AI-native** (OpenRouter.si $50K). The value here is the acronym/positioning, not Slovenian local demand.

---

## §4 Cross-fit with the payments-family master (67 rows)

| Master-CSV row | Angle for agentbucks.si | Verdict |
|---|---|---|
| Payman, Skyfire, Nevermined-adjacent (Crossmint, Catena), Natural, Causa Prima, Monid, ReFiBuy | Agent-economy / agent-money layer — the exact "bucks" audience | **carry forward** (Tier B) |
| Lithic, Highnote | Card issuing for agents — a "bucks" balance sits on a card | **not carried here** — `cardbot.si` owns that angle |
| Klarna, Affirm, Afterpay | Consumer BNPL — different job | **not carried** |
| Stripe, Visa, Mastercard | Megacap rails | **not carried** (defensive only; noted in `cardbot.si`) |
| ES/PT real-estate, betting, LatAm, fitness rows | none | **not carried** |

Net: **7 of 67** rows are `.si`-relevant for this term. The decisive lead (Tier A) is **outside** the family entirely — it came from WHOIS, not from the master CSV.

---

## §5 Honest fit flag

**Fit: MODERATE — the most interesting *story* of the five, on the thinnest *evidence base*.**

- **Pro:** a live product operates on `agentbucks.ai` with no ccTLD leg (a textbook second-leg buyer profile); the `.si` market is publicly branded as the "super intelligence" ccTLD, which makes `.si` unusually legible for an AI coinage; `.io` is also free, so a buyer assembling the set needs us for the `.si` leg specifically; two agent-economy `.si` comps (`OpenRouter.si` $50K, `X402.si` $7,839) exist.
- **Con:** the term has **no dictionary or search traction** ("agent bucks" is a coinage); the Tier-A operator is **unidentified** — we cannot approach a privacy-redacted registrant, and no compliant route exists until someone sources them; compounds settle at **$2,000–$5,000**; and the `.ai` holder may be a small side project, not a funded buyer.
- **Do not overstate:** the `.ai` being live is *evidence of use*, not evidence of ability or willingness to pay.

**Options for the owner (no ladder recommended):** (1) hold for the agent-economy `.si` wave and target Tier B (they have naming cycles); (2) treat as a speculative keep — auto-renew ON, Oct 2027 expiry, no decision needed; (3) source the `agentbucks.ai` operator before any positioning decision, because that single fact changes the whole picture.

---

## §6 Contact & fireable-status ledger

| Party | Named contact | Status | Fireable email |
|---|---|---|---|
| operator of `agentbucks.ai` | *(none — registrant redacted)* | NOT SOURCED | **None** |
| Skyfire | Amir Sarhangi | VERIFIED (skyfire.xyz) | **None** |
| Causa Prima | Maex Ament | VERIFIED (causaprima.com/about) | **None** |
| Payman, Nevermined, Catena, Natural, Crossmint, NAKA, CargoX, Bitstamp, Mangopay | *(none)* | NOT SOURCED | **None** |

**Zero invented contacts. Zero emails asserted.** The one company that matters most here (the `.ai` operator) is deliberately left blank rather than guessed.

---

## §7 Open items

1. Research only — nothing fires.
2. **Sourcing task (blocking the best lead):** identify the operator of `agentbucks.ai`. WHOIS is privacy-redacted; the only compliant routes are their own published channels. Until then, Tier A is a placeholder, not a lead.
3. Causa Prima figure conflict (§6 of `cardbot.si` doc) applies here too.
4. Owner decision: is this domain part of the agent-commerce trio, or a standalone AI-acronym play? Its buyer set overlaps the trio's Tier A but its *thesis* is different (AI acronym, not payments).
5. `.si` eligibility unverified (ARNES 404 / WHOIS refused).

---

## §8 Sources (literal URLs, fetched 2026-11-03 UTC)

- DNJournal (`.si` "super intelligence" editorial; `OpenRouter.si` $50,000; `X402.si`/`QA.si` $7,839): <https://www.dnjournal.com/domainsales.htm>
- WHOIS: `whois.nic.ai` (agentbucks.ai — Cloudflare, created 2026-05-26, US registrant, redacted) · `whois.verisign-grs.com` (agentbucks.com — Mesh Digital, 2012) · `whois.nic.io` (agentbucks.io — not found)
- Live pages: <https://agentbucks.ai> (200, login-gated Next.js app) · `agentbucks.com` (000) · <https://paymanai.com> · <https://skyfire.xyz> · <https://nevermined.io> · <https://catenalabs.com> · <https://natural.co> · <https://crossmint.io> · <https://causaprima.com> · <https://eligma.com> · <https://cargox.io> · <https://bitstamp.net> · <https://mangopay.com> · `nicehash.com` (000)
- Comp register: `docs/assets/SI-WAVE-COMP-REGISTER_2026-10-25.csv` · Leads: `DOMAINS/agentbucks.si/01-research/leads_agentbucks.si.csv`
