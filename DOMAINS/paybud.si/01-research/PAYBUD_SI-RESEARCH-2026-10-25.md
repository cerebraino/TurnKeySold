# paybud.si — Buyer Research (.si wave, task `siwave-5domain-20261025`)

**Date:** 2026-10-25 (board task) · **Evidence fetched:** 2026-11-03 UTC · **Researcher:** domain-researcher
**Scope:** buyer research **only** — no outreach copy, no valuation ladder, no price recommendation. Options-only.
**Register facts:** Namecheap · Active · expires **Oct 18 2027** · auto-renew **ON** · renewal price TBD (registrar-side, out of scope). Flagged `payments-family` in the master register.
**Freeze status:** SEND FREEZE untouched — research only, nothing fires.

---

## §0 Method & discipline

Same wave discipline as `DOMAINS/cardbot.si/01-research/CARDBOT_SI-RESEARCH-2026-10-25.md` §0. Never-invent (no email asserted anywhere), no WAF evasion (403/000 recorded), price-provenance on every figure (`docs/assets/SI-WAVE-COMP-REGISTER_2026-10-25.csv`).

**Special constraint for this domain:** `paybud.ai` is **ours** and already carries a full buyer system (`DOMAINS/paybud.ai/01-research/PAYBUD-CROSSFIT_2026-09-21.md`, 5-of-19 cross-fit after Nekuda was killed). `paybud.si` must therefore be researched as a **companion asset**, not as a competing pitch to the same contacts. Any outreach would have to be a single conversation covering both TLDs — two pitches to one buyer is exactly the kind of pressure this team does not run.

---

## §1 `.si` market context (shared)

> ".ai has a new baby brother, Slovenian ccTLD **.si**, that is also making waves as an acronym for 'super intelligence'… Atom's **$50,000 sale of OpenRouter.si** and Spaceship's sale of **Staffing.si** at the same price."
> — DNJournal, <https://www.dnjournal.com/domainsales.htm>, fetched 2026-11-03 · **VERIFIED**

Compound `.si` comps (our structural class): **CarInsurance.si $5,001** · HyperFocus.si $3,599 · guidelines.si $3,360 · Cubby.si $2,295 · Schema.si $2,000. Registry: ARNES (Ljubljana); port-43 WHOIS refused, policy pages 404 — **recorded, not circumvented**; **eligibility NOT VERIFIED**.

A second `.si` signal worth recording for this domain specifically: **`X402.si` sold together with `QA.si` for $7,839** in the same chart (fetched 2026-11-03). x402 is the agent-payments protocol name — evidence that *payments-protocol* `.si` names are trading.

---

## §2 Sibling-TLD landscape (WHOIS-verified 2026-11-03)

| Domain | Status | Evidence |
|---|---|---|
| **paybud.ai** | **Ours** (payments family; expires Dec 15 2027; auto-renew ON) | `docs/assets/DOMAIN-MASTER-REGISTER.csv` |
| **paybud.com** | Registered **2011-01-02** at GoDaddy, expires 2027-01-02 — **no HTTP response** (curl 000). Registered, not serving; holder unknown (privacy). | `whois.verisign-grs.com` + HTTP check |
| paybud.si | Ours (parked, 162.255.119.219) | register + `dig` |

**Sibling-TLD insight:** unlike `spendbot`, `paybud` has **no identified incumbent** — the `.com` is held anonymously and serves nothing, and we hold the `.ai`. That means `paybud.si` is a **pair-completion** asset: `.ai + .si` gives a buyer both the AI-market and the EU-ccTLD variant of one brand. It also means there is no third-party "sibling holder" lead to work, which lowers the standalone buyer count.

---

## §3 Buyer map (11 targets, ranked)

Ranking reflects that this is a **companion** asset: the buyer set is inherited from the payments family, filtered to parties for whom a European/ccTLD variant is meaningful.

### Tier A — payments-family rows with a genuine EU/regional angle

| # | Company | What they build | Why `paybud.si` | Contact status (verbatim from master CSV) | Route |
|---|---|---|---|---|---|
| A1 | **Klarna** (Stockholm, SE) | BNPL / consumer credit; EU-native | EU-native consumer-payments brand — a `.si` (EU ccTLD) variant is a plausible regional product marker; also the strongest "budget/pay" brand fit in the family | **(CEO)** — PENDING (lead via corp-dev) | corp-dev |
| A2 | **Stripe** (EU HQ Dublin) | Payments infra + agentic commerce | Pair with `paybud.ai` for an EU-facing brand; megacap → defensive only | **Patrick Collison — VERIFIED** | brand/corp-dev |
| A3 | **Causa Prima** (DACH/EU) | Agent-to-agent payments for finance teams | EU agent-payments pure-play; `.si` fits a EU sub-brand | **Maex Ament — VERIFIED (causaprima.com/about)** | site form/LinkedIn |
| A4 | **Skyfire** | Agent trust/payments stack | Agent payments; `.si` = EU marker | **Amir Sarhangi — VERIFIED (skyfire.xyz)** | site/LinkedIn |
| A5 | **Natural** | Agentic payments (homepage: **"Our $30M Series A July 20"** — VERIFIED, 2026-11-03) | Funded + launching; pair-completion play | NOT SOURCED | site/LinkedIn |

### Tier B — payments-family rows carried forward without a strong EU angle

| # | Company | Why it stays | Contact status |
|---|---|---|---|
| B1 | **ReFiBuy** | AI shopping agents — "pay" in an agentic checkout context | Scot Wingo — per family matrix (to re-source) |
| B2 | **Paid** | AP/AR automation | Manny Medina — VERIFIED (PayAuto pass PR #73) |
| B3 | **Monid** | Agent-payments pure-play (rank 65, added PR #98) | *(none)* — NOT SOURCED |
| B4 | **Affirm** | BNPL; US-centric → `.si` weak | Max Levchin — per leads file (to re-source) |
| B5 | **Afterpay (Block)** | BNPL; EU presence via Clearpay | Nick Molnar — per leads file (to re-source) |

### Tier C — `.si`-native / Slovenia-regional

| Party | Status | Fit |
|---|---|---|
| **NAKA (formerly Eligma)** — <https://eligma.com> serves "NAKA" | Rebrand observed 2026-11-03 | Payments-adjacent, `.si`-native; weak on "paybud" specifically |
| **CargoX** — <https://cargox.io> | 200 | Weak |
| **NiceHash** | 000 (unresponsive) | Unresponsive — recorded |

**`.si`-native verdict: THIN, and thinner than the other two trio domains.** No Slovenian company builds consumer/agent "pay-budget" products.

### Explicitly NOT carried (and why)

| Row | Reason |
|---|---|
| DraftKings, FanDuel, BetMGM, Bet365, Flutter | `paybet.ai` owns that contact set; `paybud` has no betting fit |
| CarMax, Carvana, ChargePoint, WEX/Fleetcor | `paycar.ai` / `paycarai.com` own that set |
| Zillow, Rocket, JPMorgan, Better.com, loanDepot, Wells Fargo, Properati, Vivanuncios, Habi, La Haus, Lamudi, Mercado Libre Inmuebles, Realtor.com, suacasapaga pool | ES/PT real-estate set — no `.si` angle |
| Clip, Kushki, dLocal, Nubank, Mercado Pago, Pomelo | LatAm-only — no `.si` angle |
| Strava, Sweatcoin, StepBet, Fitbit, Lympo, Pacer, MapMyFitness, Nike Run Club, Runtastic, Achievement | `jogpay.com` owns that set |
| Lithic, Highnote | `cardbot.si` owns the issuing angle (avoid two `.si` pitches at one buyer) |
| Visa, Mastercard | Defensive megacaps; noted in `cardbot.si` only |
| Nekuda | **KILL stands** (site dead 2026-10-25, PR #98) — do not re-add |

Net: **10 of 67** rows are `.si`-relevant; 5 are Tier A. The rest are excluded on use-case grounds, not dropped silently.

---

## §4 Honest fit flag

**Fit: MODERATE-WEAK as a standalone; STRONG only as a pair with `paybud.ai`.**

- **Pro:** clean pair-completion logic (`.ai` ours, `.com` anonymous/parked, no incumbent to fight); the payments family already carries a verified contact layer; EU-native payments buyers (Klarna, Causa Prima, Skyfire) are real and live; a `.si` payments-protocol comp exists (`X402.si`, $7,839 pair).
- **Con:** "paybud" is a **compound** → comp band $2,000–$5,000. There is **no sibling holder to approach** (unlike `spendbot.si`) and **no Slovenian buyer** at all. Alone, this is the weakest of the agent-commerce trio.
- **Precedent to respect:** the `paybet.ai` (thin) and `jogpay.com` (low-value) flags in the family. `paybud.si` sits closer to `paybet` than to `spendbot.si`.

**Options for the owner (no ladder recommended):** (1) keep as the EU leg of a `paybud.ai + paybud.si` pair; (2) bundle into the wider payments-family sale; (3) treat as a cheap keep (auto-renew ON, Oct 2027 expiry — no decision needed now).

---

## §5 Contact & fireable-status ledger

| Company | Named contact | Status (verbatim) | Fireable email |
|---|---|---|---|
| Stripe | Patrick Collison | VERIFIED | **None published in our files** |
| Causa Prima | Maex Ament | VERIFIED (causaprima.com/about) | **None** |
| Skyfire | Amir Sarhangi | VERIFIED (skyfire.xyz) | **None** |
| Paid | Manny Medina | VERIFIED (PayAuto pass PR #73) | **None** |
| Klarna | (CEO) | PENDING (lead via corp-dev) | **None** |
| ReFiBuy / Affirm / Afterpay | named execs | "per leads file / per family matrix (to re-source)" — **not re-verified in this pass** | **None** |
| Natural, Monid, NAKA, CargoX | *(none)* | NOT SOURCED | **None** |

**Zero invented contacts. Zero emails asserted.** Note the **multi-contact rule**: where the family already carries parallel contacts (e.g. Payman elsewhere), they stay parallel.

**Flags for the lead:** (1) the Causa Prima "$20M (homepage, 2026-11-03) vs $30M (repo)" conflict affects this domain too; (2) three rows here are marked "to re-source" in the master CSV and remain unverified — do not promote them to VERIFIED without a fresh pass.

---

## §6 Open items

1. Research only — nothing fires.
2. Owner decision: sell `paybud.si` **only ever as a pair** with `paybud.ai`? That is the only framing the evidence supports.
3. Exec sourcing needed for 6 of 11 rows.
4. `.si` eligibility unverified (ARNES 404 / WHOIS refused).

---

## §7 Sources (literal URLs, fetched 2026-11-03 UTC)

- DNJournal (`.si` editorial + comps incl. `X402.si`/`QA.si` $7,839): <https://www.dnjournal.com/domainsales.htm>
- WHOIS: `whois.verisign-grs.com` (paybud.com, 2011, GoDaddy); register row for `paybud.ai` in `docs/assets/DOMAIN-MASTER-REGISTER.csv`
- Live pages checked: <https://causaprima.com> · <https://skyfire.xyz> · <https://natural.co> · <https://eligma.com> · <https://cargox.io> · `nicehash.com` (000) · `paybud.com` (000)
- Not fetched this pass (carried from family records only): Klarna, Stripe, ReFiBuy, Affirm, Afterpay, Paid, Monid, Visa/Mastercard
- Comp register: `docs/assets/SI-WAVE-COMP-REGISTER_2026-10-25.csv` · Leads: `DOMAINS/paybud.si/01-research/leads_paybud.si.csv` · Sibling research: `DOMAINS/paybud.ai/01-research/PAYBUD-CROSSFIT_2026-09-21.md`
