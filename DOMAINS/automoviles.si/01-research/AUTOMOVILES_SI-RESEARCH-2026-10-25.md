# automoviles.si — Buyer Research (.si wave, task `siwave-5domain-20261025`)

**Date:** 2026-10-25 (board task) · **Evidence fetched:** 2026-11-03 UTC · **Researcher:** domain-researcher
**Scope:** buyer research **only** — no outreach copy, no valuation ladder, no price recommendation. Options-only.
**Register facts:** Namecheap · Active · expires **Oct 18 2027** · auto-renew **ON** · renewal price TBD (registrar-side, out of scope).
**Freeze status:** SEND FREEZE untouched — research only, nothing fires.

---

## §0 Method & discipline

Same wave discipline as `DOMAINS/cardbot.si/01-research/CARDBOT_SI-RESEARCH-2026-10-25.md` §0. Never-invent, no WAF evasion (403/000 recorded), price-provenance on every figure (`docs/assets/SI-WAVE-COMP-REGISTER_2026-10-25.csv`).

**The question this document exists to answer:** *is a Spanish-market auto word on a Slovenian ccTLD a real asset, or a thin candidate?* The answer below is documented, not softened.

---

## §1 `.si` market context (shared)

> ".ai has a new baby brother, Slovenian ccTLD **.si**, that is also making waves as an acronym for 'super intelligence'…"
> — DNJournal, <https://www.dnjournal.com/domainsales.htm>, fetched 2026-11-03 · **VERIFIED**

Compound `.si` comps: CarInsurance.si $5,001 (Atom.com) · HyperFocus.si $3,599 · guidelines.si $3,360 · Cubby.si $2,295 · Schema.si $2,000.

**Critical caveat for this domain:** every one of those `.si` sales is an **English or brandable** term sold into the AI/EU narrative. **None of the 35+ `.si` sales in the chart is a Spanish-language word.** That is not proof that a Spanish `.si` cannot sell — it is proof that *no precedent exists*, which is what a buyer will say back to us.

Registry: ARNES (Ljubljana); port-43 WHOIS refused, policy pages 404 on 2026-11-03 — **recorded, not circumvented**; **eligibility NOT VERIFIED**.

---

## §2 Sibling-TLD and comp landscape (verified 2026-11-03)

| Domain | Status | Evidence | Reading |
|---|---|---|---|
| **automoviles.com** | Registered **1996-06-14** (GoDaddy), expires 2027-06-13 — serves a **parked `/lander`** (JS redirect) | `whois.verisign-grs.com` + HTTP 200 lander | The exact-match `.com` is a **parked asset held by an investor**, not an operating brand. A 1996 registration held parked usually means a priced-for-sale or dormant holding. |
| **automoviles.net** | Registered **1997-03-26** (GoDaddy), expires 2028-03-27 — **parked domain lander** | `whois.verisign-grs.com` + HTTP 200 | Same pattern — second investor holding. |
| **automoviles.es** | **Registered and hosted** (resolves to 104.247.81.99) — registrant **NOT RETRIEVABLE**: `whois.nic.es` port-43 query returned empty from our network | `dig` + WHOIS attempt | The market-defining ccTLD is taken by an unknown party. **No bypass attempted.** |
| automoviles.si | Ours (parked, 162.255.119.98) | register + `dig` | — |

**Comp sales — what we could and could not establish:**

| Item | Result |
|---|---|
| `automoviles` sale in the DNJournal chart (current bi-weekly) | **None found** — no `automovil*` entry anywhere on the page (full-text check, 2026-11-03) |
| NameBio comps | **NOT ATTEMPTED** — NameBio is IP-blocked from this network per standing rule; no evasion, **no comp asserted** |
| Nearest verified `.es` comp in the chart | **`joyland.es` $5,600** (DNJournal, fetched 2026-11-03) — an `.es` sale, i.e. the ES market does trade, at the low thousands |
| Spanish-word `.ai` comps | `automoviles.ai` $5K–$20K band appears in our own `DOMAINS/automoviles.ai/01-research/leads_automoviles.ai.md` (2026-07-22) as a **DMPS estimate, EXTERNAL-UNVERIFIED** — not a sale, must not be quoted as one |

**Honest conclusion on comps:** there is **no provenanced comp for `automoviles` on any TLD**, and none for a Spanish word on `.si`. Everything a buyer could be told today would be inference.

---

## §3 Buyer map (11 targets) — who actually buys ES auto-industry domains

The Spanish auto/classifieds and auto-finance layer is real and large; the question is whether any of them would want a **Slovenian ccTLD**. Ranked by fit:

### Tier A — ES auto marketplaces & portals (the natural exact-match buyers)

| # | Company | Status (fetched 2026-11-03) | Why `automoviles.si` | Route |
|---|---|---|---|---|
| A1 | **AutoScout24 España** — <https://autoscout24.es> | 200 ("Coches de segunda mano") | Pan-EU marketplace group (Scout24) already operates across European ccTLDs; `.si` is a European market it could enter — but it would buy `.si` for **Slovenia**, not for Spanish content. | corp-dev |
| A2 | **Motor.es** — <https://motor.es> | 200 | Spanish auto portal; exact word, zero `.si` need. | corp-dev |
| A3 | **Carwow España** — <https://carwow.es> | 200 | UK/EU comparison platform expanding in ES; multi-ccTLD operator. | corp-dev |
| A4 | **Flexicar** — <https://flexicar.es> | 200 ("Más de 170 concesionarios") | Large ES used-car network; brand is `flexicar`, not `automoviles`. | corp-dev |
| A5 | **OcasiónPlus** — <https://ocasionplus.com> | 200 ("120 centros, +20.000 coches") | Same. | corp-dev |
| A6 | **Carplus** — <https://carplus.es> | 200 | Same. | corp-dev |
| A7 | **coches.net** (Adevinta/Milanuncios group) | **403 bot-wall** ("Ups! Parece que algo no va bien…") — **documented, not circumvented** | Largest ES auto vertical; would be the single best Spanish buyer — but unverifiable from our network today. | corp-dev (unverified) |
| A8 | **milanuncios.com** | **403** ("Pardon Our Interruption") — documented | Generalist classifieds with a large motors section. | corp-dev (unverified) |

### Tier B — ES auto finance & leasing (the "who pays for domains" layer)

| # | Company | Status | Fit |
|---|---|---|---|
| B1 | **Santander Consumer España** — <https://santanderconsumer.es> | 200 | Auto finance; exact-word ES domains are brand-comfort assets. `.si` still foreign. |
| B2 | **Ayvens** (ex-LeasePlan/ALD) — <https://ayvens.com> | 200 | Multi-country leasing — the *only* Tier-B party for whom a `.si` has operational meaning (they run EU country sites). |
| B3 | **Arval España** (BNP Paribas) — `arval.es` | **403** (CloudFront) — documented | Same logic, unverified. |
| B4 | **Cetelem España** (BNP) | **No HTTP response** (000) | Auto/consumer credit. |
| B5 | **Aramovil** | **No HTTP response** (000) | Recorded as unresponsive. |

### Tier C — the mismatch test: Slovenian auto buyers?

**None identified.** No Slovenian dealer group, portal or financier was surfaced in this pass that would use a Spanish word. Slovenia's own auto vocabulary is *avtomobil/avtomobili* — the Slovenian word for cars is `avtomobil`, not `automoviles`. **`automoviles.si` is not a Slovenian word and not a Slovenian market play.**

---

## §4 Cross-fit with the payments-family master (67 rows)

| Row | Angle | Verdict |
|---|---|---|
| CarMax, Carvana | US auto retail + auto finance | **not carried** — no ES, no `.si` |
| ChargePoint | EV charging | **not carried** |
| WEX / Fleetcor | Fleet payments | **not carried** |
| Stripe / Visa / Mastercard | none for a car word | **not carried** |

Net: **0 of 67** payments-family rows convert for this domain. This is the only one of the five `.si` domains with a **complete cross-fit failure** — worth recording as a finding in itself.

---

## §5 Honest fit flag — **THIN / LOW-VALUE (paybet-jogpay precedent)**

**Verdict: THIN. Stated plainly, as the brief requires.**

Four independent reasons, each verifiable:

1. **No comp exists.** No `automoviles` sale on any TLD in the public chart; NameBio blocked (not attempted). Nothing provenanced to anchor a conversation.
2. **No language–TLD precedent.** 35+ `.si` sales in the current chart, **zero** Spanish-language words. Every `.si` buyer to date has been buying an English/brandable term into an AI or EU narrative.
3. **Wrong market pairing.** `automoviles` is the Spanish word for cars; `.si` is Slovenia's ccTLD and the Slovenian word is `avtomobil`. A Spanish-language buyer has no reason to want a Slovenian ccTLD, and a Slovenian buyer has no reason to want a Spanish word.
4. **Zero payments-family cross-fit** (§4) — the one system this team has already built gives no leverage here.

**The one non-zero angle:** `automoviles.ai` is already in the portfolio with a buyer map (`DOMAINS/automoviles.ai/01-research/`), and a Spanish-market buyer who wants a multi-TLD set could take `.ai + .si` together. That is a **bundle rider**, not a standalone case — and even then `.si` adds nothing a Spanish buyer needs.

**Options for the owner (no ladder recommended):** (1) hold as a **bundle rider** with `automoviles.ai`; (2) park it as a long-dated keep (auto-renew ON, Oct 2027 — no decision needed); (3) if the owner wants a decision this quarter, treat it as the **first candidate to drop** on renewal economics, alongside the `paybet.ai` (thin) and `jogpay.com` (low-value) precedents.

---

## §6 Contact & fireable-status ledger

| Party | Named contact | Status | Fireable email |
|---|---|---|---|
| AutoScout24 ES, Motor.es, Carwow ES, Flexicar, OcasiónPlus, Carplus, Santander Consumer ES, Ayvens | *(none)* | NOT SOURCED — exec sourcing required before any outreach | **None** |
| coches.net, milanuncios.com, arval.es | *(none)* | NOT VERIFIABLE — bot-walled to our network (403) | **None** |
| Cetelem ES, Aramovil | *(none)* | UNRESPONSIVE (000) | **None** |

**Zero invented contacts. Zero emails asserted.** No Spanish-market contact names were sourced in this pass — that is the honest state, not an omission to paper over.

---

## §7 Open items

1. Research only — nothing fires.
2. **Blocked sources recorded:** `coches.net` (403), `milanuncios.com` (403), `arval.es` (403), `cetelem.es`/`aramovil.com` (000), `whois.nic.es` (empty response), NameBio (IP-blocked, not attempted). Any of these would need owner-side or alternate-egress access.
3. Owner decision: keep as `automoviles.ai` bundle rider, or drop at renewal. This doc recommends **no standalone campaign**.
4. `.si` eligibility unverified (ARNES 404 / WHOIS refused).

---

## §8 Sources (literal URLs, fetched 2026-11-03 UTC)

- DNJournal (`.si` editorial; comps; **no `automovil*` entry**): <https://www.dnjournal.com/domainsales.htm>
- WHOIS: `whois.verisign-grs.com` (automoviles.com — 1996, GoDaddy, parked lander; automoviles.net — 1997, GoDaddy, parked lander); `whois.nic.es` (empty response — recorded)
- DNS: `dig automoviles.es` → 104.247.81.99 (registered/hosted)
- ES buyers checked: <https://autoscout24.es> · <https://motor.es> · <https://carwow.es> · <https://flexicar.es> · <https://ocasionplus.com> · <https://carplus.es> · <https://santanderconsumer.es> · <https://ayvens.com>
- Blocked/unresponsive (documented, not circumvented): `coches.net` (403), `milanuncios.com` (403), `arval.es` (403), `cetelem.es` (000), `aramovil.com` (000), `alphabet.es` (301 loop)
- Comp register: `docs/assets/SI-WAVE-COMP-REGISTER_2026-10-25.csv` · Leads: `DOMAINS/automoviles.si/01-research/leads_automoviles.si.csv` · Sibling asset: `DOMAINS/automoviles.ai/01-research/leads_automoviles.ai.md`
