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