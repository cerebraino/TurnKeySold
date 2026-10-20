# PayAuto.ai — Tier-1 External Research Verification Results

**Date:** 2026-09-21 (task 1ba44884) · **Verifier:** domain-researcher
**Scope:** Tier-1 (8 pure-play agentic-payments companies) — website liveness, funding claims, contact names/titles; resolve Payman CEO conflict.
**Rule applied:** never-invent — every claim below has a published source URL or is explicitly marked NOT verified. Funding claims quoted verbatim where possible.

## Summary table

| # | Company | Site (HTTP) | Funding claim | Verdict | Contact / title | Verdict |
|---|---------|-------------|---------------|---------|-----------------|---------|
| 1 | Natural | natural.com 200 | $30M Series A led by Forerunner; ~$40M total | ✅ $30M VERIFIED; ~$40M = $10M seed + $30M (inferred) | Kahlil Lalji — CEO | ✅ VERIFIED |
| 2 | Payman AI | paymanai.com 200 | $13.8M (Visa; Boost VC; Protofund) | ⚠️ amount CORRECTED → **$13M total** per company | Tyllen Bicakcic — Co-Founder & CEO | ✅ VERIFIED (conflict RESOLVED) |
| 3 | Basis Theory | basistheory.com 200 | $33M Series B (Oct 2025 - Costanoa); ~$50M total | ⚠️ PARTIAL — $33M raise ✅; "Series B"/Costanoa/`~$50M` ❌ not confirmed | Colin Luce — CEO | ❌ NOT verified (no public team page) |
| 4 | Catena Labs | catena.com 200 | $30M Series A (Acrew + a16z); ~$48M total | ⚠️ PARTIAL — $30M Series A ✅ (Fortune via site); Acrew+a16z / ~$48M ❌ not confirmed | Sean Neville — Co-Founder & CEO | ✅ VERIFIED |
| 5 | Crossmint | crossmint.com 200 | $23.6M (Ribbit Capital) | ✅ VERIFIED | Rodrigo Fernández Touza — Co-Founder | ✅ VERIFIED (site team page) |
| 6 | Paid | paid.ai 200 | $21.6M seed (Lightspeed); total $33.3M | ✅ VERIFIED (both figures) | Manny Medina — Co-Founder & CEO | ✅ VERIFIED |
| 7 | Skyfire | skyfire.com 200 (empty shell); **skyfire.xyz** 200 = live site | $9.5M (Coinbase; a16z CSX; Neuberger) | ⚠️ amount CORRECTED → **$8.5M seed** (Neuberger Berman, Inception Capital, Arrington) | Amir Sarhangi — CEO | ✅ VERIFIED |
| 8 | Nekuda | nekuda.com DEAD | $5M (Madrona + Amex + Visa) | ❌ UNVERIFIED — company appears dead | Ayal Karmi — Co-Founder & CEO | ❌ UNVERIFIED |

## Per-company detail (sources)

### 1. Natural — natural.com
- **Site:** 200 OK. About page states: "The company was incorporated on August 12th, 2025… Within 72 hours of sharing the memo, Natural raised a **$10M seed round**" and "**Kahlil Lalji, CEO, Co-founder**" — https://www.natural.com/about
- **$30M Series A:** TechCrunch 2026-07-20 "Natural raises $30M to reinvent payments for AI agents — and take on Stripe": "it now has $30 million in fresh capital"; "**Kirsten Green, founder and managing partner at VC firm Forerunner… led its $30 mil…**" — https://techcrunch.com/2026/07/20/natural-raises-30m-to-reinvent-payments-for-ai-agents-and-take-on-stripe/
- **~$40M total:** NOT directly published; equal to $10M seed (site) + $30M Series A (TC) — inferred arithmetic, flagged as such.
- Forerunner also quoted on natural.com/about ("At Forerunner, we've spent years…").
- ⚠️ collaborator's "2nd payments company of founder" not checked in this pass.

### 2. Payman AI — paymanai.com
- **Site:** 200 OK. Press index states verbatim: "**Funding: $13M raised in total.**" — https://www.paymanai.com/press
- **CEO CONFLICT RESOLVED:** company's own press release (Middlesex Federal agentic-banking partnership) carries **Tyllen Bicakcic — Co-Founder & CEO** — https://www.paymanai.com/press/payman-ai-partners-with-middlesex-federal. Our Aug-12 leads row (Teymour Farman-Farmaian, Founder/CEO) is **stale for the CEO title**; keep Teymour as co-founder / parallel outreach target per owner multi-contact directive (leads + contacts files updated).
- Collaborator claim "$13.8M (Visa; Boost VC; Protofund)": **NOT corroborated** — company primary says $13M total. Use $13M in outreach.
- TC Skyfire article (2024-08-21) independently confirms Payman as an operating customer of Skyfire.

### 3. Basis Theory — basistheory.com
- **Site:** 200 OK (Framer build; `/about`, `/company`, `/team`, `/careers`, `/blog` all 404 — no public team page).
- **$33M raise:** ✅ confirmed by multiple published headlines (Google News aggregations, 2026):
  - PR Newswire: "Basis Theory Raises $33M to Power Agentic Commerce and the Next Era of Merchant Payments"
  - Payments Dive: "Basis Theory raises $33M"
  - Digital Commerce 360: "Basis Theory raises $33 million to build AI-driven payments for commerce"
  - Finovate: "Data Privacy Management Software Provider Basis Theory Secures $33 Million"; Axios round-up: "Basis Theory's $33m"
- **"Series B (Oct 2025 - Costanoa)" and ~$50M total: NOT independently confirmed** in this pass (PR/article bodies are JS/consent-walled from this environment). Keep as collaborator claim; recommend LinkedIn/PR follow-up.
- **Colin Luce (CEO & Co-Founder): NOT verified** — no public team page; LinkedIn bot-walled. Do not fire outreach on Colin Luce until title confirmed (recommend LinkedIn path / company PR body).

### 4. Catena Labs — catena.com
- **Site:** 200 OK. About page: "**Sean Neville (CEO)** and Matt Venables (CTO) founded Catena… co-founding Circle, inventing USDC…" — https://catena.com/about
- **$30M Series A:** ✅ confirmed — fortune.com headline embedded on catena.com/about: "**Exclusive: Circle cofounder raises $30 million for Series A 'AI-native bank' Catena — Fortune**".
- **Acrew + a16z crypto names and ~$48M total: NOT independently confirmed** (Fortune article itself not fetched; paywalled). Keep as collaborator claim.

### 5. Crossmint — crossmint.com
- **Site:** 200 OK. Team page lists **Rodrigo Fernández Touza, Co-Founder** — https://www.crossmint.com/team
- **$23.6M led by Ribbit Capital:** ✅ confirmed by multiple published headlines (via Google News):
  - The Block: "**Ribbit Capital leads $23.6 million funding round** for enterprise blockchain platform Crossmint" (⚠ The Block's own privacy page may restrict direct fetch; headline + source captured via Google News)
  - PR Newswire: "Crossmint Secures $23.6M to Bring Businesses & AI Agents onchain"
  - CoinDesk: "Blockchain Firm Crossmint Used by Adidas, Red Bull Raises $23.6M in Funding"; PYMNTS: "Crossmint Raises $23.6 Million…"
  - Fortune: "Exclusive: Crossmint nets **$24 million**…" (rounding difference — note it)
- Collaborator's "+ Circle Ventures investment" not separately confirmed.

### 6. Paid — paid.ai
- **Site:** 200 OK. About page lists **Manny Medina** (Co-Founder & CEO per TC) — https://paid.ai/about
- **Funding:** ✅ fully confirmed:
  - Company blog: "Paid raises $21 million seed…" — https://paid.ai/blog/company/paid-raises-21-6-million-seed-round
  - TechCrunch 2025-09-28: "Paid, the AI-agent results-based billing startup from Manny Medina, raises huge $21M seed"
  - traded.co: "Paid secures $21.6 million seed round **led by Lightspeed, bringing total funding to $33.3 million**" — https://traded.co/vc/deal/paid-secures-21-6-million-seed-round-led-by-lightspeed-bringing-total-funding-to-33-3-million/
  - Also Goodwin (legal), Yahoo Finance syndication, WizCase, techbuzz (21.6M) — consistent.
  - ⚠️ paid.ai blog also shows a later "**€10M**" raise ("Paid raises €10M to build the business engine for AI Agents") — total may now exceed $33.3M; flag for outreach copy if relevant.

### 7. Skyfire — skyfire.xyz (live) / skyfire.com (shell)
- **Site:** live site is **skyfire.xyz** (200; about page lists **Amir Sarhangi — CEO**) — https://skyfire.xyz/about. skyfire.com returns 200 but is an empty JS shell in this environment (`/about` → bot-wall) — treat skyfire.xyz as canonical for verification. (Collaborator CSV listed skyfire.com.)
- **Funding — DISCREPANCY:** TechCrunch 2024-08-21 "Skyfire lets AI agents spend your money": "announced **$8.5 million in seed funding** raised from **Neuberger Berman, Inception Capital, Arrington Capital**, and other investors" — https://techcrunch.com/2024/08/21/skyfire-lets-ai-agents-spend-your-money/
  - Collaborator's "$9.5M (Coinbase Ventures; a16z CSX; Neuberger Berman)" is **NOT corroborated**; TC names Neuberger Berman (not "Neuberger") and two other funds, no Coinbase/a16z, and amount differs.
  - TechCrunch 2026-07-20 (Natural article) refers to "**DCVC-backed Skyfire Systems**" — indicates a possible later round; recommend follow-up before quoting Skyfire funding.
- Contact verified: Amir Sarhangi = co-founder & CEO (skyfire.xyz/about; TC 2024-08-21 confirms "Skyfire's co-founder and CEO Amir Sarhangi"; Craig DeWitt = co-founder & CPO).

### 8. Nekuda — nekuda.com
- **Site: DEAD.** DNS resolves to 104.247.81.99 but TCP connects fail; `/about` returns 000; Wayback CDX has no snapshot (archive.org CDX service also intermittently offline). Treat as EXTERNAL-UNVERIFIED/KILL.
- **$5M seed (Madrona + Amex Ventures + Visa Ventures) and Ayal Karmi (Co-Founder & CEO): UNVERIFIABLE** — no live site or archive. Recommend dropping from active outreach list unless revival evidence appears.

## Out-of-scope confirmations captured incidentally (Tier-2 contacts from original CSV)
- **Arcade.dev** — site 200; **Alex Salazar Founder & CEO** — https://www.arcade.dev/about. Funding ($72M total) NOT re-verified in this pass.
- **HappyRobot** — site 200; **Pablo Palafox Co-Founder & CEO** (happyrobot.ai blog); **$150M Series C, led by Prysm Capital co-led by Eurazeo, $1.2B post-money, ~$200M total** confirmed on company blog "We've Raised $150 Million in Series C Funding" (2026-09-22; own claim) — https://www.happyrobot.ai/blog/happyrobot-seriesc-fundraising-announcement. 150+ enterprise customers (DHL, Kuehne+Nagel, Naturgy, Repsol, Uber).
- **Rye** — site 200; **Arjun Bhargava Co-Founder & CEO** — https://rye.com/about. Funding `$14M` NOT re-verified.
- **ReFiBuy** — site 200; **Scot Wingo Co-Founder & CEO** — https://refibuy.ai/about. Funding ($13.6M) NOT re-verified.

## Flags / follow-ups for the lead
1. **Skyfire funding discrepancy** ($8.5M vs $9.5M; investor names) — correct all copy to $8.5M / Neuberger Berman + Inception + Arrington unless a newer round is sourced (DCVC mention 2026).
2. **Basis Theory** — $33M confirmed but Colin Luce title + "Series B/Costanoa/~$50M" unconfirmed → verify via LinkedIn before any outreach naming him.
3. **Nekuda** — dead site; recommend removing from active list.
4. **Payman** — use $13M (company primary); keep Teymour as parallel contact, Bicakcic as CEO target.
5. **Catena** — Acrew + a16z names still collaborator-only; fine for internal use, do not state as fact in outreach without sourcing.
6. **Crossmint** — Fortune says $24M vs PR $23.6M; use $23.6M.
7. Wayback CDX was intermittently "Temporarily Offline" during this pass; archived-page confirmation of Nekuda should be retried when archive.org is stable.
8. Machine notes: Bing/Mojeek/Finsmes bot-blocked for long-tail queries; Google News RSS + TechCrunch WP-API + Bing base64 `u=` decode were the reliable routes (see memory/tooling notes).
---

# PayAuto.ai — Tier-2/3 Second Verification Pass

**Date:** 2026-10-19 (task eb45d140) · **Verifier:** domain-researcher
**Scope:** Tier-2 (4 agentic-commerce-infra companies, rows 9–12) + Tier-3 (7 megacap/corporate-route rows 13–19) + three PR #73 follow-ups (Basis Theory Luce title, Skyfire DCVC line, Nekuda Wayback CDX retry).
**Rule applied:** never-invent — every claim below has a published source or is explicitly marked NOT verified / title-only.

## Summary table

| # | Company | Site (HTTP) | Funding claim | Verdict | Contact / title | Verdict |
|---|---------|-------------|---------------|---------|-----------------|---------|
| 9 | Arcade.dev | arcade.dev 200 | $72M total ($60M Series A Jun 2026 — SYN + Morgan Stanley + Wipro) | ⚠️ PARTIAL — $60M Series A + prior $12M round headline-verified; "$72M total" = inferred sum of published rounds; investor names NOT independently confirmed | Alex Salazar — Founder & CEO | ✅ VERIFIED (Tier-1, arcade.dev/about) |
| 10 | HappyRobot | happyrobot.ai 200 | $150M Series C at $1.2B post-money (Aug 2026) | ✅ VERIFIED (company blog + PYMNTS + SiliconANGLE) | Pablo Palafox — Co-Founder & CEO | ✅ VERIFIED |
| 11 | Rye | rye.com 200 | $14M (a16z-led) | ✅ VERIFIED (CoinDesk headline; identity resolved — Justin Kan co-founder on rye.com/about) | Arjun Bhargava — Co-Founder & CEO | ✅ VERIFIED |
| 12 | ReFiBuy | refibuy.ai 200 | $13.6M seed (May 2026) | ✅ VERIFIED (Axios + Hypepotamus + Yahoo headlines) | Scot Wingo — Co-Founder & CEO | ✅ VERIFIED |
| 13 | Ramp | ramp.com 200 | ~$32B valuation; $700M raise (2025); IPO prep | ⚠️ CORRECTED — $32B (Nov 2025) → $44B @ $750M (Jun 2026) → $60B (Oct 2026); "$700M raise" NOT-VERIFIED (headline = revenue); IPO prep NOT-VERIFIED | corporate BD route | n/a |
| 14 | Brex | brex.com 200 | Multi-billion private fintech (qualitative) | ✅ existence verified; no figure to check | corporate BD route | n/a |
| 15 | Visa | visa.com (public co) | Public company | ✅ program verified (Visa Intelligent Commerce — PRN release URL) | Intelligent Commerce partnerships | n/a |
| 16 | Mastercard | mastercard.com (public co) | Public company | ✅ existence + agentic activity verified (PYMNTS URL); "Agent Pay/Start Path" = internal strategy notes only | Agent Pay / Start Path partnerships | n/a |
| 17 | Stripe | stripe.com 200 | ~$90B+ valuation (secondary) | ⚠️ CORRECTED — latest reported **$159B** post-tender (CNBC/Yahoo headlines, title-only) | Agentic Commerce Suite partnerships | n/a |
| 18 | PayPal | paypal.com (public co) | Public company | ✅ existence verified | ACP / agentic partnerships | n/a |
| 19 | Coinbase | coinbase.com 403 (bot-wall) | Public company | ✅ program verified (x402 protocol — PYMNTS URLs ×2) | x402 / Base ecosystem | n/a |

## Tier-2 per-company detail (sources)

### 9. Arcade.dev — arcade.dev
- **Site:** 200 OK (title: "Arcade: The Actions Runtime for Enterprise AI Agents"). **Alex Salazar Founder & CEO** confirmed in Tier-1 pass (arcade.dev/about).
- **$60M Series A — headline-verified**: multiple independent published headlines, 2026 (publisher pages not fetchable from this network; title + source captured via Google News, 2026-10-19):
  - Business Wire: "Arcade Raises $60M to Become the Secure Action Layer Behind Every Production AI Agent"
  - WSJ: "Exclusive | Arcade.dev Raises $60 Million to Secure AI Agents" · The Next Web · citybiz · SiliconANGLE
- **Prior $12M round — headline-verified**: TechCrunch "Arcade raises $12M from Perplexity co-founder's new fund to make AI agents less awful"; Business Wire "Arcade.dev Scores $12M to Solve the Biggest Security Problem with AI Agents".
- **"$72M total"** = $12M + $60M published-sum — inferred arithmetic, flagged as such (keep or drop in outreach copy; do not state as a company figure).
- **SYN Ventures + Morgan Stanley + Wipro investor names: NOT independently confirmed** (collaborator claim; not in any fetched source).

### 10. HappyRobot — happyrobot.ai
- **Site:** 200 OK. Funding **VERIFIED** three ways:
  - Company blog (own claim): "We've Raised $150 Million in Series C Funding" — https://www.happyrobot.ai/blog/happyrobot-seriesc-fundraising-announcement (captured Tier-1 2026-09-21; led by Prysm Capital co-led by Eurazeo, $1.2B post-money, ~$200M total).
  - PYMNTS: "HappyRobot Vaults to $1.2 Billion Valuation as Enterprise Demand for AI Automation Soars" — https://www.pymnts.com/news/investment-tracker/2026/happyrobot-vaults-to-1-2-billion-valuation-as-enterprise-demand-for-ai-automation-soars/
  - SiliconANGLE headline: "HappyRobot raises $150M at $1.2B valuation to bring AI agents to critical enterprise work" (via GN; title-only).
- **Pablo Palafox Co-Founder & CEO** — company blog + Fortune ("Its founder…" via GN). ✅

### 11. Rye — rye.com
- **Site:** 200 OK (title: "Rye: Universal agentic checkout that actually works"). **Arjun Bhargava Co-Founder & CEO** confirmed (rye.com/about, Tier-1) + leadership page verbatim: "Arjun Bhargava Co-Founder, CEO · Justin Kan Co-Founder · Jamie Quint Co-Founder" — https://rye.com/about.
- **$14M a16z-led round — headline-verified**: CoinDesk "A16z Leads $14M Funding Round for New E-Commerce Platform From Twitch Co-Founder" (via GN 2026-10-19; article body not fetchable). **Identity resolved**: Justin Kan (a Twitch co-founder) is listed as Rye Co-Founder on rye.com/about → the $14M round belongs to Rye.

### 12. ReFiBuy — refibuy.ai
- **Site:** 200 OK (title: "ReFiBuy | Agentic Commerce Optimization"). **Scot Wingo Co-founder CEO** confirmed — https://refibuy.ai/about (Tier-1 + leadership page verbatim).
- **$13.6M seed — headline-verified** (pages not fetchable from this network; titles + sources via GN 2026-10-19): Axios "A Raleigh e-commerce startup led by Scot Wingo has raised a $13.6M seed round" · Hypepotamus "ReFiBuy Raises $13.6M for AI Commerce Platform" · The Business Journals · Yahoo Finance.
- Collaborator caveat stands: **weakest fit — opportunistic only**.

## Tier-3 per-company detail (sources)

### 13. Ramp — ramp.com (corporate route)
- **Site:** 200 OK. **Valuation trajectory VERIFIED (three published milestones):**
  - $32B — TechCrunch 2025-11-17 "Ramp hits $32B valuation, just 3 months after hitting $22.5B" — https://techcrunch.com/2025/11/17/ramp-hits-32b-valuation-just-three-months-after-hitting-22-5b/
  - $44B @ $750M raise — TechCrunch 2026-06-04 "Ramp raises $750M at $44B valuation…" — https://techcrunch.com/2026/06/04/ramp-raises-750m-at-44b-valuation-as-investors-hunger-for-fintechs-with-an-ai-story/
  - $60B — TechCrunch 2026-10-15 "Ramp reaches $60B valuation as it pushes deeper into AI" — https://techcrunch.com/2026/10/15/ramp-reaches-60b-valuation-as-it-pushes-deeper-into-ai/ ; PYMNTS "Ramp Valued at $60 Billion Following New Funding Round" — https://www.pymnts.com/news/investment-tracker/fintech-investments/2026/ramp-valued-at-60-billion-following-new-funding-round/
  - ⚠️ Collaborator's "~$32B" = the Nov-2025 milestone, now stale (use $60B).
- **"$700M in under 2 months (2025)" NOT-VERIFIED** — no such raise found; the "$700M" headline located is annualized revenue ("Ramp has more than doubled its annualized revenue to $700M", TC). **"IPO prep reported" NOT-VERIFIED.**

### 14. Brex — brex.com (corporate route)
- **Site:** 200 OK (JS shell — no title in this environment). Funding claim is qualitative ("multi-billion private fintech"); no specific figure to verify. ✅ existence only.

### 15. Visa (corporate route)
- Public company; agentic-commerce program **"Visa Intelligent Commerce" corroborated with URL**: PR Newswire "Crossmint Launches Agentic Cards API Using Visa Intelligent Commerce and Basis Theory" — https://www.prnewswire.com/news-releases/crossmint-launches-agentic-cards-api-using-visa-intelligent-commerce-and-basis-theory-302786624.html (fetched 2026-10-19; body confirms the program + quotes Basis Theory CEO and Crossmint Co-Founder).
- Visa's own agentic-commerce content (title-only via GN): corporate.visa.com "Agentic Commerce: The expanded payments economy"; www.visa.com "5 trends shaping the future of agentic commerce".

### 16. Mastercard (corporate route)
- Public company; agentic-commerce activity **verified with URL**: PYMNTS "Mastercard Bets Shoppers Will Trust AI Agents One Purchase at a Time" — https://www.pymnts.com/news/artificial-intelligence/2026/mastercard-bets-shoppers-will-trust-ai-agents-one-purchase-at-a-time/
- **"Agent Pay / Start Path" names = internal strategy notes** (contact-route intent), NOT externally verified program names — do not state as fact in outreach.

### 17. Stripe — stripe.com (corporate route)
- **Site:** 200 OK. Collaborator's "~$90B+ valuation (secondary)" **SUBSUMED/CORRECTED** — latest reported **$159B** post-tender-offer (title-only via GN 2026-10-19; CNBC/Yahoo pages not fetchable from this network): CNBC "Stripe valued at $159 billion after tender offer for employees, shareholders"; Yahoo Finance "Stripe's valuation soars 74% to $159 billion".
- No exec claim to verify (partnerships route).

### 18. PayPal (corporate route)
- Public company; existence verified (paypal.com). "ACP / agentic partnerships" = internal strategy note. Funding claim N/A.

### 19. Coinbase (corporate route)
- Public company (coinbase.com 403 bot-walled from this environment; existence via public record). **x402 agentic-payments protocol corroborated with URLs** (PYMNTS, fetched-able):
  - "Block Joins x402 Foundation to Drive Agentic Commerce Standards" — https://www.pymnts.com/news/artificial-intelligence/2026/block-joins-x402-foundation-to-drive-agentic-commerce-standards/
  - "Agentic Payments Are Growing, but Most x402 Payments Are Not From AI Agents" — https://www.pymnts.com/news/artificial-intelligence/2026/agentic-payments-are-growing-most-x402-payments-are-not-from-ai-agents/

## PR #73 follow-ups — all three RESOLVED

1. **Basis Theory — Colin Luce title RESOLVED → VERIFIED "Co-Founder and CEO"**: PR Newswire release body (fetched 2026-10-19) quotes verbatim: *"…says Colin Luce, Co-Founder and CEO of Basis Theory."* — https://www.prnewswire.com/news-releases/crossmint-launches-agentic-cards-api-using-visa-intelligent-commerce-and-basis-theory-302786624.html
   - $33M raise remains headline-verified only (Finovate "Data Privacy Management Software Provider Basis Theory Secures $33 Million"; Payments Dive "Basis Theory raises $33M" — via GN; the $33M PRN release body was not recovered from this network).
   - "Series B / Costanoa / ~$50M total" still NOT independently confirmed.
   - **Architect actionable:** the wave-1 PayAuto A3 (Basis Theory) company-level greeting may now be personalized to Colin Luce — Co-Founder & CEO (PRN URL above). No send without the owner's freeze-lift.
2. **Skyfire — DCVC line VERIFIED**: TechCrunch 2026-07-20 (Natural article) verbatim: *"…several other startups, including DCVC-backed Skyfire Systems, are trying to reinvent the payments backbone for AI agents using USD-backed stablecoins."* — https://techcrunch.com/2026/07/20/natural-raises-30m-to-reinvent-payments-for-ai-agents-and-take-on-stripe/
   - Confirms a DCVC round exists; **no new round amount published** in accessible sources → keep **$8.5M seed** as the verified figure (Neuberger Berman, Inception Capital, Arrington per TC 2024-08-21). "DCVC-backed" usable as evidence of post-seed backing, not as an amount.
3. **Nekuda — Wayback CDX retry: no snapshots, KILL CONFIRMED**: archive.org CDX queried 2026-10-19 (http://web.archive.org/cdx/search/cdx?url=nekuda.com&matchType=domain&output=json&limit=12&collapse=urlkey) → empty response (no snapshot records); site still dead. No archived evidence of the company or contact Ayal Karmi. Keep KILL; do not reintroduce without revival evidence.

## Flags / follow-ups for the lead

1. **Wave-1 A3 (Basis Theory) greeting upgrade** — Luce title now verified (PRN URL); per verification-gated greeting rule, the copy may now personalize. Architect decision + owner freeze-lift still required.
2. **ROOT `payauto_ai_acquisition_targets.csv` is a pre-verification snapshot** (e.g., Payman row still "$13.8M total" vs the verified $13M; no flags column). Tier-1 left it untouched too. Recommend: resync from workbench or explicitly deprecate the root copy — otherwise future consumers may quote stale figures.
3. **Pre-existing workbench malformation**: rows 1/3/6/7 contain unescaped double-quotes inside annotation cells (Tier-1-era write) — csv readers mis-split those rows. Not introduced by this pass; recommend a dedicated cleanup commit (quote-escape the four cells) before any machine consumption of Team_Annotations.
4. **Ramp copy hygiene**: any outreach mentioning Ramp's scale should use $60B (Oct 2026) with the TC/PYMNTS URLs; do NOT use "$700M raise" (revenue figure) or "IPO prep" (unverified).
5. **Stripe copy hygiene**: use "$159B post-tender (2026, CNBC)" if scale ever needed; "~$90B+" is stale.
