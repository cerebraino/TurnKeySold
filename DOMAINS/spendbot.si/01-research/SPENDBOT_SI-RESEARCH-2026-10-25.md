# spendbot.si — Buyer Research (.si wave, task `siwave-5domain-20261025`)

**Date:** 2026-10-25 (board task) · **Evidence fetched:** 2026-11-03 UTC · **Researcher:** domain-researcher
**Scope:** buyer research **only** — no outreach copy, no valuation ladder, no price recommendation. Options-only.
**Register facts:** Namecheap · Active · expires **Oct 18 2027** · auto-renew **ON** · renewal price TBD (registrar-side, out of scope).
**Freeze status:** SEND FREEZE untouched — research only, nothing fires.

---

## §0 Method & discipline

Same wave discipline as `DOMAINS/cardbot.si/01-research/CARDBOT_SI-RESEARCH-2026-10-25.md` §0: never-invent (no email is asserted anywhere in this file), no WAF evasion (403s/000s recorded), price-provenance on every figure (URL + fetched-on date, consolidated in `docs/assets/SI-WAVE-COMP-REGISTER_2026-10-25.csv`).

**This domain has the strongest sibling-TLD evidence in the whole wave**, and it is the reason it ranks first among the trio: the `.ai` is held by a **European procurement company** and the `.com` is a **live consumer product run by a named company**.

---

## §1 `.si` market context (shared)

Verbatim, the market thesis for the wave:

> ".ai has a new baby brother, Slovenian ccTLD **.si**, that is also making waves as an acronym for 'super intelligence'… Atom's **$50,000 sale of OpenRouter.si** and Spaceship's sale of **Staffing.si** at the same price."
> — DNJournal, <https://www.dnjournal.com/domainsales.htm>, fetched 2026-11-03 · **VERIFIED**

Compound-name `.si` comps (our structural class): **CarInsurance.si $5,001** · HyperFocus.si $3,599 · guidelines.si $3,360 · Cubby.si $2,295 · Schema.si $2,000. Full register: `docs/assets/SI-WAVE-COMP-REGISTER_2026-10-25.csv`.

Registry: ARNES (Ljubljana) operates `.si`; port-43 WHOIS refused our connection and ARNES policy pages 404'd on 2026-11-03 — **recorded, not circumvented**. **Eligibility rules NOT VERIFIED — do not assert.**

---

## §2 Sibling-TLD landscape (WHOIS-verified 2026-11-03) — the core finding

| Domain | Holder / status | Evidence | What it means |
|---|---|---|---|
| **spendbot.ai** | **OptiBuy Sp. z o.o.**, ul. Jana Kazimierza 3, Warszawa 01-248, **Poland** — registrar Marcaria International LLC · created 2022-10-18 · expires 2028-10-18 · status `autoRenewPeriod` | `whois.nic.ai` (registrant org is **published**, person redacted) | **A European procurement company chose `spendbot.ai` as its brand and has held it since 2022.** That is the single best piece of sibling-TLD evidence in this wave: an EU buyer already paid for this exact word. Their corporate site `optibuy.pl` returned **HTTP 403** to us (documented, not circumvented) — route must go through their own published channels, and **no contact name/email is asserted here**. |
| **spendbot.com** | **Spendbot, Inc.** — registrar GoDaddy · created 2009-07-02 · expires 2027-07-02 · footer: *"Copyright © 2026 - Spendbot, Inc. All Rights Reserved."* | `whois.verisign-grs.com` + live page | A **live consumer personal-finance product** ("Spendbot – the world's Best Personal Financial Management System", sign-in gated, testimonial page). An operating company with a product brand that already matches the word — the classic "they own one TLD, we hold another" situation. |
| spendbot.si | Ours (parked, 162.255.119.199) | register + `dig` | — |

**Sibling-TLD insight (explicit):** `spendbot` is *not* an orphan word. Two operating parties hold the other two major TLDs. `spendbot.ai`'s holder is **EU-based**, which makes `.si` (EU ccTLD, adjacent market, same continent) the most plausible complement they could buy. Both are *use-case* matches; neither is a confirmed buyer.

---

## §3 Buyer map (14 targets, ranked)

### Tier A — sibling-TLD holders (highest priority; exact-name match)

| # | Party | Fit | Route | Caution |
|---|---|---|---|---|
| A1 | **OptiBuy Sp. z o.o.** (Warsaw) — holds `spendbot.ai` | **Exact name, EU-based, procurement category** = spend control. If they are building an AI spend product under `spendbot`, `.si` is a natural second-market twin. | Corporate site `optibuy.pl` (**403 to us** — route via their own published contact/LinkedIn) | Registrant org published in WHOIS; **no person, no email asserted**. Their site is bot-walled to us; that is a routing problem for the owner, not something to circumvent. |
| A2 | **Spendbot, Inc.** (holds `spendbot.com`) | Exact name, live consumer PFM product; `spendbot.si` protects the EU/ccTLD flank of their brand. | Site/`Get Live Help` channel published on their own page | Company name verified from their own footer. No person/email asserted. |

### Tier B — EU spend-management platforms (exact use-case: spend control for teams, now agentic)

All pages fetched 2026-11-03, HTTP 200:

| # | Company | What they build (page title, verbatim) | Why `spendbot.si` | Route |
|---|---|---|---|---|
| B1 | **Payhawk** | "AI-Powered Platform for Spend Management & Finance Orchestration" (Sofia, BG) | The category *is* the domain. An AI spend agent sub-brand fits; `.si` = EU ccTLD marker. | corp-dev/site form |
| B2 | **Pleo** | "Smarter spending for your business" (Copenhagen, DK) | Card + spend control for SMBs; agent-spend is their live product frontier. | corp-dev |
| B3 | **Spendesk** | "Spend Smarter, Work Better" (Paris, FR) | Name adjacency (`Spend*`) + EU-native; a `.si` variant is cheap defensive cover. | corp-dev |
| B4 | **Moss** | "Finance AI, shaped by you" (Berlin, DE) | AI-first positioning *and* spend category — the closest thematic match in the EU set. | corp-dev |
| B5 | **Soldo** | "Simplify Spend Management" (London/Rome) | Spend control + cards; EU presence. | corp-dev |
| B6 | **Qonto** | "Manage all your finances from your Qonto business account" (Paris, FR) | Business spend + cards; EU-native. | corp-dev |
| B7 | **Perk** (serves `yokoy.ai`) | "The intelligent platform for travel and spend" | **Note:** the domain `yokoy.ai` now serves a product titled **Perk** — an observed rebrand. Verify identity before any outreach. | site/LinkedIn |

### Tier C — agent-spend / agentic-payments layer (timing: these are the buyers who will name things next quarter)

| # | Company | What they build | Why | Route |
|---|---|---|---|---|
| C1 | **Payman AI** — <https://paymanai.com> | "Agentic AI That Does the Banking. Under Your Control." | Agents that spend → an agent-spend control brand is their next product. | corp/site form |
| C2 | **Natural** — <https://natural.co> | "Powering agentic payments" (homepage: **"Our $30M Series A July 20"** — **VERIFIED**, 2026-11-03) | Funded + launching; spend limits/guardrails are the natural product. | site/LinkedIn |
| C3 | **Causa Prima** — <https://causaprima.com> | "Agent-to-agent network for finance teams" (homepage: **"We raised $20 million funding"** — VERIFIED, 2026-11-03; conflicts with the repo's $30M — see §6) | Finance-team agents = spend control. | Maex Ament — VERIFIED (causaprima.com/about) per master CSV |
| C4 | **Catena Labs** — <https://catenalabs.com> | "How AI Agents Use Money" | Agent money movement + policy. | site/LinkedIn |
| C5 | **Nevermined** — <https://nevermined.io> | "Payments Infrastructure for AI Agents" | Agent metering/spend budgets. | site/LinkedIn |

### Tier D — `.si`-native / Slovenia-regional (thin)

| Party | Status | Fit |
|---|---|---|
| **NAKA (formerly Eligma)** — <https://eligma.com> serves a page titled "NAKA" | Rebrand observed 2026-11-03 | Weak on the term; relevant only as a `.si`-native rebranding party |
| **CargoX** (Ljubljana) — <https://cargox.io> | 200 | Weak |
| **NiceHash** | No HTTP response (000) | Unresponsive — recorded, not contacted |

**`.si`-native verdict: THIN.** No Slovenian spend-management/agent-spend company was found. The `.si` case here rests on the **EU ccTLD complement** to two existing `spendbot` holders, not on local demand.

---

## §4 Cross-fit with the payments-family master (67 rows)

| Master-CSV row | Angle for spendbot.si | Verdict |
|---|---|---|
| Causa Prima, Natural, Payman, Skyfire, Crossmint, Monid, ReFiBuy | Agent payments → spend control is the adjacent product | **carry forward** (Causa Prima/Natural to Tier C) |
| Paid (AP/AR automation, VERIFIED — Manny Medina) | AP automation ≈ spend control | **carry forward as P2** (not tiered here; B2B AP, not card-spend) |
| Klarna, Affirm, Afterpay | BNPL consumer credit | **not carried** — different job |
| Lithic, Highnote, Pomelo | Issuing infra | **not carried** — cardbot.si owns that angle; keep the two `.si` domains from competing for the same contact |
| ES/PT real-estate + mortgage rows | none | **not carried** |

Net: **8 of 67** rows are `.si`-relevant for spendbot; the rest are excluded on use-case grounds.

---

## §5 Honest fit flag

**Fit: STRONG for the wave — the best of the five.**

- **Pro:** two operating parties already hold `spendbot` on other TLDs, and one of them (`spendbot.ai`, OptiBuy) is **EU-based in the exact category**. The EU spend-management buyer set is deep, live and verifiable (7 companies, all 200). The term is category-literal ("bot that spends"), which is precisely what every agent-payments company is building.
- **Con:** it is still a **compound** → comp band $2,000–$5,000 (`CarInsurance.si $5,001` is the top of that class), not the $25K+ single-word band. The strongest named prospect's website is **bot-walled to us** (403) — routing, not circumvention, is the only compliant path. And `spendbot.ai`'s holder may simply be a procurement consultancy that never commercialises the name.
- **Asymmetry to note:** the `.ai` is under `autoRenewPeriod` (2028 expiry) — no imminent drop, so no expiry-based urgency angle exists. Do not manufacture one.

**Options for the owner (no ladder recommended):** (1) hold and pitch Tier A on the EU-complement logic; (2) bundle with `cardbot.si` as a "spend + card" agent-commerce pair; (3) sell into the EU spend-management set (Tier B) as a product-naming asset.

---

## §6 Contact & fireable-status ledger

| Party | Named contact carried | Status (verbatim) | Fireable email |
|---|---|---|---|
| OptiBuy Sp. z o.o. | **Organisation only** (WHOIS registrant org, published) | VERIFIED as registrant org — `whois.nic.ai`, 2026-11-03 | **None — optibuy.pl 403 to us** |
| Spendbot, Inc. | Company only (own footer) | VERIFIED (company) | **None published in our files** |
| Causa Prima | Maex Ament | VERIFIED (causaprima.com/about) — master CSV | **None** |
| Paid | Manny Medina | VERIFIED (PayAuto pass PR #73) — master CSV | **None** |
| All 11 other companies | *(none)* | NOT SOURCED — exec sourcing required before any outreach | **None** |

**Zero invented contacts. Zero emails asserted.**

**Flags for the lead:**
1. **Causa Prima funding conflict** — homepage "$20 million" (2026-11-03) vs repo record "$30M". Needs one correction decision; it affects both `cardbot.si` and `spendbot.si` docs and the master CSV.
2. **`yokoy.ai` now serves "Perk"** — an observed rebrand; any future row must use the current brand, not the old one.
3. **`optibuy.pl` is 403-walled to our network.** Any contact attempt must use the owner's own channels; we did not and will not bypass.
4. `.si` eligibility unverified (ARNES pages 404, WHOIS refused).

---

## §7 Open items

1. Research only — nothing fires; freeze untouched.
2. Exec sourcing needed for 12 of 14 companies.
3. Owner decision: is `spendbot.si` a **standalone EU pitch** or a **pair with `cardbot.si`**? The buyer sets overlap (Payman/Natural/Causa Prima/Catena/Nevermined appear in both) — running them as one conversation is more honest than two.
4. Causa Prima / yokoy.ai flags above.

---

## §8 Sources (literal URLs, fetched 2026-11-03 UTC)

- DNJournal (`.si` editorial + comp chart): <https://www.dnjournal.com/domainsales.htm>
- Sibling WHOIS: `whois.nic.ai` (spendbot.ai → OptiBuy Sp. z o.o.), `whois.verisign-grs.com` (spendbot.com)
- EU spend platforms: <https://payhawk.com> · <https://pleo.io> · <https://spendesk.com> · <https://getmoss.com> · <https://soldo.com> · <https://qonto.com> · <https://yokoy.ai> (serves "Perk")
- Agent-spend layer: <https://paymanai.com> · <https://natural.co> · <https://causaprima.com> · <https://catenalabs.com> · <https://nevermined.io>
- `.si`-native: <https://eligma.com> · <https://cargox.io> · `nicehash.com` (000)
- Blocked, recorded, not circumvented: `optibuy.pl` (403), ARNES WHOIS port 43 (refused), ARNES policy pages (404)
- Comp register: `docs/assets/SI-WAVE-COMP-REGISTER_2026-10-25.csv` · Leads: `DOMAINS/spendbot.si/01-research/leads_spendbot.si.csv`
