# cardbot.si — Buyer Research (.si wave, task `siwave-5domain-20261025`)

**Date:** 2026-10-25 (board task) · **Evidence fetched:** 2026-11-03 UTC (session clock) · **Researcher:** domain-researcher
**Scope:** buyer research **only** — no outreach copy, no valuation ladder, no price recommendation. Options-only; the owner sets any ladder.
**Register facts (docs/assets/DOMAIN-MASTER-REGISTER.csv, main 08e1af1):** Namecheap · Active · expires **Oct 18 2027** · auto-renew **ON** · renewal price TBD (registrar-side, explicitly out of scope for this task).
**Freeze status:** SEND FREEZE untouched — nothing in this document is copy and nothing fires.

---

## §0 Method & discipline

DMPS baseline (buyer role → money → timing) + `domain-outbound-lead-researcher` ordering (**exact-match > sibling-TLD > use-case > timing**) + cross-fit against the existing payments-family system (`payments_family_buyers_master.csv`, 67 rows, main 08e1af1).

- **Never-invent:** every named contact below is either (a) carried from the repo's verified/attributed records with its original status string, or (b) absent. No emails, no inferred addresses, no `firstname@` guesses.
- **No WAF/anti-bot evasion:** every 403/406/000 is recorded as an outcome, not worked around.
- **Price-provenance:** every figure carries a literal URL + fetched-on date in `docs/assets/SI-WAVE-COMP-REGISTER_2026-10-25.csv`. Anything unprovenanced is labelled **EXTERNAL-UNVERIFIED**.
- **No pricing asserted for our domain.** Comp data is market context, not a valuation.

---

## §1 `.si` market context (shared across all five `.si` domains)

The `.si` wave is not a Slovenia-local play. It is an **AI-acronym play**, and that is now on the public record:

> ".ai has a new baby brother, Slovenian ccTLD **.si**, that is also making waves as an acronym for 'super intelligence'. Two of those hit the Big Board this week with Atom's **$50,000 sale of OpenRouter.si** and Spaceship's sale of **Staffing.si** at the same price…"
> — DNJournal, latest bi-weekly Domain Sales Report, <https://www.dnjournal.com/domainsales.htm>, fetched 2026-11-03 · **VERIFIED** (verbatim)

The same chart carries **35+ distinct `.si` sales** (full register in `docs/assets/SI-WAVE-COMP-REGISTER_2026-10-25.csv`). Shape of the market:

| Band | Examples (published prices) |
|---|---|
| Ceiling | OpenRouter.si $50,000 · Staffing.si $50,000 · Gifts.si €28,000 = $31,360 |
| Premium single words | Hollywood.si $30,000 · Pure.si $26,825 · Fractal.si / Game.si / Stocks.si $25,000 · Dubai.si / Plasma.si $20,000 · Caspian.si $19,795 |
| Mid | Truth.si $8,676 · **X402.si + QA.si $7,839 (pair)** · Genes.si $7,500 · Surplus.si $7,495 |
| **Compound-word floor (our structural class)** | **CarInsurance.si $5,001** · HyperFocus.si $3,599 · guidelines.si $3,360 · Cubby.si $2,295 · Schema.si $2,000 |

Two structural reads that matter for `cardbot.si`:

1. **`X402.si` is the single most relevant comp in the wave.** x402 is the agent-payments protocol name; a buyer paid a real price for a *protocol-term* `.si` in the same fortnight the agent-commerce thesis is being priced. `cardbot.si` is a first-order agent-commerce term.
2. **Compound names settle at the $2,000–$5,000 band, not the $25,000+ band.** `CarInsurance.si $5,001` is the only compound near the top of that band. Honest read: `cardbot.si` is a *compound*, so the premium-single-word band is not its comparable class.

**Registry notes:** `.si` is the Slovenian ccTLD; the registry operator is ARNES (Ljubljana — <https://www.arnes.si/>). Its port-43 WHOIS refused connections from our network on 2026-11-03 (`ConnectionRefusedError`), and ARNES policy pages returned HTTP 404 — **recorded, not circumvented**. Registrations are handled through accredited registrars (e.g. the national registrar listing at <https://www.registry.si/>, which states "Before registering a .si domain name, please consider reviewing General Terms and Conditions"). **Eligibility/residency rules: NOT VERIFIED** — do not assert them to a buyer or in copy.

---

## §2 Sibling-TLD landscape (WHOIS-verified, 2026-11-03)

| Domain | Status | Evidence |
|---|---|---|
| **cardbot.com** | **Registered since 1998-09-28** (Tucows), expires 2027-09-27 — but it **serves a "Domain Available / Premium domain available" lander**. The `.com` is itself on the market, not an operating brand. | `whois.verisign-grs.com`; HTTP 200 lander |
| **cardbot.ai** | **UNREGISTERED** ("Domain not found") | `whois.nic.ai` |
| cardbot.si | Ours (parked at Namecheap — resolves to 192.64.119.79) | register + `dig` |

**Sibling-TLD insight:** `cardbot` is a *clean registration field* — the `.com` is a for-sale lander and the `.ai` is free. That cuts both ways and must be stated honestly to the owner: a buyer who wants the exact brand can assemble `.com + .ai` without us, so **`cardbot.si` sells on the `.si`-specific thesis (EU/Slovenia presence + "si"/"super intelligence" branding), not on scarcity.** The counterweight is that the `.com` being listed means someone is actively pricing the name — a market signal, not a competitor to our `.si`.

---

## §3 Buyer map (12 targets, ranked)

Ordering follows the skill's priority chain. `.si` fit is stated per row; nothing here is a claim that the buyer wants the domain.

### Tier A — agentic-payments pure-plays (exact use-case: an agent that holds/uses a card)

| # | Company | What they build (verified page) | Why `cardbot.si` | Route |
|---|---|---|---|---|
| A1 | **Payman AI** | "Agentic AI That Does the Banking. Under Your Control." — <https://paymanai.com> (200) | The literal product class: an agent that moves money on a card rail. `cardbot` is a product-name candidate, and `.si` gives an EU-facing twin. | corp/site form; named contacts per `payments_family_buyers_master.csv` (Payman multi-contact per owner directive) |
| A2 | **Skyfire** | "The Agent Trust Stack" — <https://skyfire.xyz> (200) | Agent identity + payment authorisation; a card-issuing-agent product line fits. | Amir Sarhangi — **VERIFIED (skyfire.xyz)** per master CSV |
| A3 | **Nevermined** | "Payments Infrastructure for AI Agents" — <https://nevermined.io> (200) | Agent metering/payments; `.si` = EU + "super intelligence" framing. | site/LinkedIn |
| A4 | **Catena Labs** | "How AI Agents Use Money" — <https://catenalabs.com> (200) | Agent-native financial rails; card issuance is an adjacent line. | site/LinkedIn |
| A5 | **Natural** | "Powering agentic payments" — <https://natural.co> (200) — homepage states **"Our $30M Series A July 20"** (**VERIFIED**, fetched 2026-11-03) | Funded, hiring, product-launch cadence → timing. | site/LinkedIn |
| A6 | **Crossmint** | "Stablecoin Platform & APIs for Enterprises" — <https://crossmint.io> (200) | Agent wallet/card surface for enterprises. | site/LinkedIn |
| A7 | **Causa Prima** | "Agent-to-agent network for finance teams" — <https://causaprima.com> (200) | B2B agent payments → corporate card agents. **Note:** homepage now states **"We raised $20 million funding"** (VERIFIED, 2026-11-03), which **conflicts with the $30M figure reconciled in `PAYQUICK-VERIFICATION-RESULTS_2026-09-21.md`** — flagged for the lead (see §6). | Maex Ament — **VERIFIED (causaprima.com/about)** per master CSV |

### Tier B — card-issuing infrastructure (sibling-TLD / product-line fit)

| # | Company | What they build | Why `cardbot.si` | Route |
|---|---|---|---|---|
| B1 | **Lithic** | Card-issuing APIs — <https://lithic.com> (payments-family record; $43M B + $60M C led by Stripes Sep-2026 per PR #98 — **EXTERNAL-UNVERIFIED in this doc**, verified in the PR #98 ledger) | Issuing infra selling to agent platforms; a `.si` product microsite is a plausible defensive buy. | corp-dev |
| B2 | **Highnote** | Card issuing + acquiring — $90M Series B, >$750M valuation per PR #98 ledger (**EXTERNAL-UNVERIFIED here**) | Same, US-centric → `.si` only as an EU marker. | corp-dev |
| B3 | **Enfuce** | Finnish card-issuing/payments (200) — <https://enfuce.com> | **EU-native issuer**; a `.si` (EU ccTLD) card-product brand is a cheaper option than a gTLD for a regional line. | site/LinkedIn |
| B4 | **Wallester** | "Business accounts, cards and White-Label issuing" (200) — <https://wallester.com> | White-label issuing = they *sell* card products under others' brands; `cardbot` is a ready-made product name. | site/LinkedIn |
| B5 | **Swan** | "embed banking features" (200) — <https://swan.io> | French EMI/embedded banking; card issuing included → EU `.si` twin. | site/LinkedIn |

### Tier C — EU payments platforms (use-case + timing; `.si` as an EU sub-brand)

| # | Company | What they build | Why `cardbot.si` | Route |
|---|---|---|---|---|
| C1 | **Adyen** | "Fintech platform for enterprises" (200) — <https://adyen.com> | Has an agentic-commerce/commerce-media narrative; `.si` works as an EU-facing AI sub-brand. Megacap → slow procurement. | corp-dev |
| C2 | **Mangopay** | "Multi-party payment flows" (200); homepage states **"€68B transactions processed"** (**VERIFIED**, 2026-11-03) | EU marketplace payouts + cards; `.si` as an EU brand extension. | corp-dev |

### Tier D — `.si`-native / Slovenia-regional (thin, honestly)

| # | Company | Status | Note |
|---|---|---|---|
| D1 | **NAKA (formerly Eligma)** | <https://eligma.com> now serves a page titled **"NAKA"** (200, fetched 2026-11-03) | Slovenia's best-known payments/crypto brand, now rebranded — a rebranding company is the classic domain-buying moment. **Name change observed, not otherwise verified.** |
| D2 | **CargoX** | "Building digital trust, one document at a time" (200) — <https://cargox.io> | Ljubljana; document/payment rails. Weak `cardbot` fit. |
| D3 | **Bitstamp** | 200 — <https://bitstamp.net> | Slovenia-founded exchange (ownership now external); weak fit, listed for completeness. |
| D4 | **NiceHash** | **No HTTP response** (000, 2026-11-03) | Recorded as unresponsive — not contacted, not assumed dead. |

**`.si`-native verdict:** the Slovenia-regional layer is **thin for this specific term**. No Slovenian company was found building card-issuing-for-agents. The `.si` value here is *the AI-acronym thesis plus EU presence*, not local demand.

---

## §4 Cross-fit with the payments-family master (67 rows)

Which of the existing 67 rows have a `.si` / regional-EU expansion angle for `cardbot`:

| Master-CSV row | Angle for cardbot.si | Verdict |
|---|---|---|
| Skyfire, Causa Prima, Paid, ReFiBuy, Monid | Agent-payments layer — product-name fit | **carry forward** (Skyfire/Causa Prima into Tier A) |
| Lithic, Highnote | Card-issuing infra | **carry forward** (Tier B) |
| Stripe (VERIFIED: Patrick Collison) | Issuing + agentic commerce at scale | **low priority** — megacap procurement; noted only |
| Visa (VERIFIED: Ryan McInerney), Mastercard (VERIFIED: Michael Miebach) | Agentic card mandates | **low priority** — defensive-only; no realistic `.si` product need |
| Klarna, Affirm, Afterpay/Block | BNPL, not card-agent | **not carried** |
| Pomelo (LatAm issuing) | Card issuing but LatAm-only | **not carried** — no `.si` angle |
| ES/PT real-estate + mortgage rows (Zillow, Rocket, Habito-pool etc.) | none | **not carried** |

Net: **7 of 67** rows convert into `.si`-relevant cardbot candidates; the other 60 are excluded on use-case grounds rather than left as noise.

---

## §5 Honest fit flag

**Fit: MODERATE — not thin, not strong.**

- **Pro:** exact product-class term in the hottest adjacent category; a direct, recent, verifiable agent-protocol `.si` comp (`X402.si`, $7,839 pair); clean sibling field (`.com` = for-sale lander, `.ai` = unregistered) so there is no incumbent brand to fight; `.si` is publicly branded as the "super intelligence" ccTLD, which is free positioning for an AI product name.
- **Con:** it is a **compound**, and compound `.si` comps cluster at **$2,000–$5,000** (CarInsurance.si $5,001 as the top of that class). No Slovenian card-issuing buyer exists. The `.ai` being unregistered is a genuine substitution risk.
- **Buyer-quality caveat:** the Tier-A companies are startups with active product-naming needs (good) but small domain budgets (bad). Tier-B/C are large enough to buy but have no demonstrated need (slow).

**Options for the owner (no ladder recommended):** (1) hold for the agent-commerce `.si` wave and target Tier A on product-naming cycles; (2) sell as a bundle rider alongside the payments family; (3) treat as a cheap keep (auto-renew ON, 2027 expiry — no action needed before Oct 2027).

---

## §6 Contact & fireable-status ledger

| Company | Named contact carried | Status (verbatim from source) | Fireable email? |
|---|---|---|---|
| Skyfire | Amir Sarhangi | VERIFIED (skyfire.xyz) — master CSV | **None published in our files** |
| Causa Prima | Maex Ament | VERIFIED (causaprima.com/about) — master CSV | **None published in our files** |
| Stripe | Patrick Collison | VERIFIED — master CSV | **None published in our files** |
| Visa | Ryan McInerney | VERIFIED (public) — master CSV | **None published in our files** |
| Mastercard | Michael Miebach | VERIFIED (public) — master CSV | **None published in our files** |
| Payman AI, Nevermined, Catena, Natural, Crossmint, Lithic, Highnote, Enfuce, Wallester, Swan, Adyen, Mangopay, NAKA, CargoX, Bitstamp | *(none)* | NOT SOURCED — execs to source before any outreach | **None** |

**Zero invented contacts. Zero emails asserted. Multi-contact rule:** where the master CSV already holds parallel contacts (Payman per owner directive), those rows stay parallel — do not collapse them into one.

**Two data-quality flags for the lead:**
1. **Causa Prima funding:** homepage (2026-11-03) says **"$20 million"**; the repo's PayQuick verification reconciled **$30M**. One of the two records should be corrected — recommend the homepage figure with its fetched-on date, pending a second source.
2. **`.si` registry eligibility** is unverified (ARNES pages 404, WHOIS refused). If outreach later leans on "EU presence", that claim must be re-checked first.

---

## §7 Open items (owner/lead)

1. Nothing to fire — this is research only; freeze untouched.
2. Decide the `.si` wave's story: **AI-acronym thesis** (`.si` = super intelligence) vs **Slovenia/EU presence** vs **bundle rider**. The comp evidence supports the first; the buyer map supports the second weakly.
3. If the wave goes ahead: exec sourcing is required for 15 of 20 companies (all but Skyfire/Causa Prima/Stripe/Visa/Mastercard) — that is a separate, never-invent-compliant research task.
4. Causa Prima figure conflict (§6).

---

## §8 Sources (literal URLs, fetched 2026-11-03 UTC)

- DNJournal bi-weekly Domain Sales Report (`.si` "super intelligence" editorial + full comp chart): <https://www.dnjournal.com/domainsales.htm>
- Sibling WHOIS: `whois.verisign-grs.com` (cardbot.com), `whois.nic.ai` (cardbot.ai), `whois.nic.io` (agentbucks.io)
- Buyer pages: <https://paymanai.com> · <https://skyfire.xyz> · <https://nevermined.io> · <https://catenalabs.com> · <https://natural.co> · <https://crossmint.io> · <https://causaprima.com> · <https://enfuce.com> · <https://wallester.com> · <https://swan.io> · <https://adyen.com> · <https://mangopay.com> · <https://eligma.com> · <https://cargox.io> · <https://bitstamp.net>
- Registry: <https://www.arnes.si/> · <https://www.registry.si/>
- Blocked/unresponsive (recorded, not circumvented): `nicehash.com` (000), `thredd.com` (403 Cloudflare), `worldline.com` (406), ARNES WHOIS port 43 (connection refused), ARNES policy pages (404)
- Comp register (all prices + fetched-on dates): `docs/assets/SI-WAVE-COMP-REGISTER_2026-10-25.csv`
- Leads CSV for this domain: `DOMAINS/cardbot.si/01-research/leads_cardbot.si.csv`
