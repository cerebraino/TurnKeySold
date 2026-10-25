# Agentic Payments — US External Research: Verification & Reconciliation

**Date:** 2026-10-25 · **Task:** a4146026 · **By:** domain-researcher
**Source:** `AGENTIC-PAYMENTS-US-EXTERNAL-RESEARCH_2026-10-25.md` (owner-supplied external-LLM research; verbatim full-field copy at `DOMAINS/payauto.ai/01-research/`, md5-identical).
**Citation convention:** figures marked *(via GN)* = outlet/headline/date retrieved through Google News RSS on 2026-10-25 (PR #95 precedent). Literal URLs cited where already team-verified and carried in the root CSV.

Per §9.7 flag vocabulary: every source figure starts `EXTERNAL-UNVERIFIED`; verdicts below are the team's own verification of each claim.

---

## P1 — RYE × JOLLY acquisition claim: **UNCONFIRMED** (priority check)

The external source states Rye (our Tier-2 **VERIFIED** buyer, PR #87: $14M a16z-led round, Arjun Bhargava Co-Founder & CEO, rye.com/about) "was acquired by Jolly in September 2026."

Checks run 2026-10-25:

| Check | Result |
|---|---|
| Google News RSS `Rye acquired Jolly agentic checkout` | **0 hits** |
| Google News RSS `Rye Jolly acquisition September 2026` | **0 hits** |
| Google News RSS `Rye a16z universal checkout API` | **0 hits** |
| Google News RSS `Jolly Rye` (loose) | 29 hits — all unrelated (Faygo soft-drinks 2026-09-21; Rye Country Day School 2019; local boxing 2016). **Zero tech/agentic-checkout coverage** |
| Bing `"Rye" acquired "Jolly"` | **"There are no results"** (searchNoResult marker) |
| TechCrunch site search (WP API) `rye jolly` | only an unrelated 2008 post |
| Live probes | userye.com HTTP 000 (unreachable from this box — inconclusive), rye.com HTTP 200 |

**Verdict:** no published source corroborates the acquisition. Per the never-invent rule we do **NOT** mark Rye stale, and the PR #87 record **STANDS** (Tier-2 VERIFIED, $14M a16z, contact Arjun Bhargava). No Jolly entry is added (the source gives no Jolly identity/URL/HQ to verify). **Action:** re-check before any Rye direct outreach; treat the acquisition as an EXTERNAL-UNVERIFIED claim.

## P2 — figure reconciliation (external vs our verified records)

| Company | Source claim | Our verified record | Verdict 2026-10-25 |
|---|---|---|---|
| Natural | $40M total = $9.8M seed (Oct-2025) + $30M Series A (Forerunner, Jul-2026) | $30M Series A **VERIFIED** (PR #73 — literal TC URL techcrunch.com/2026/07/20/natural-raises-30m-to-reinvent-payments-for-ai-agents-…; root CSV) | **Series A re-confirmed** — Finextra 2026-07-22 "Natural raises $30 million…", TNW 2026-07-21, PYMNTS 2026-07-20 *(via GN)*. **$9.8M seed NOT separately located → $40M total PARTIAL** |
| Catena Labs | ~$48M = $18M seed (a16z crypto, May-2025) + $30M Series A (May-2026) | $30M Series A VERIFIED (PR #73); funding PARTIAL | **Series A re-confirmed** — Fortune 2026-05-20 "Exclusive: Circle cofounder raises $30 million for Series A 'AI-native bank' Catena Labs" + Yahoo/Bitpush (a16z Crypto participation) + PYMNTS 2026-05-24 *(via GN)*. a16zcrypto.com "Investing in Catena Labs" (2025-05-20) corroborates the seed round only; **$18M amount NOT located → PARTIAL stands** |
| Basis Theory | $50M+ total | $33M Series B VERIFIED (Costanoa, Oct-2025 — PR #87) | "$50M+ total" **UNVERIFIED** (earlier-round composition not located); $33M base unchanged |
| Payman AI | ~$13.8M over 3 rounds | CORRECTED to **$13M company-primary** (PR #87) | Delta is aggregate-multi-round vs single-figure basis; no new evidence → **keep $13M** |
| Skyfire | $9.5M | CORRECTED to **$8.5M seed + DCVC line** (PR #87, literal TC URL) | No new round located → **keep $8.5M** |
| Crossmint | $23.6M Ribbit (Mar-2025) + Circle Ventures (Sep-2025) | $23.6M Ribbit **VERIFIED** (The Block, PR #73) | **Consistent — no change** |
| Nekuda | $5M seed (Madrona, Amex Ventures, Visa Ventures) | UNVERIFIED + KILL (site dead) | **$5M seed VERIFIED** at company level — Pulse 2.0 2025-05-19 "Nekuda: $5 Million Raised…" *(via GN)*; co-investor list not individually re-verified. KILL verdict unchanged (P4) |

## P3 — new onboarding candidates (master CSV ranks 65–67)

1. **Monid** (San Francisco — "checkout counter for AI agents") → row added under **paydeal.ai** (agent-checkout pure-play semantics).
   - **$7.7M seed VERIFIED** — Dealroom 2026-10-07 "Monid raises $7.7M seed to be the checkout counter for AI agents"; Crypto Briefing 2026-10-06 "Monid raises $7.7 million to plug AI agents into pay-per-use tools" *(via GN)*.
   - HQ SF = source claim only (UNVERIFIED). No contacts yet; willingness left blank (no valuation basis).
2. **Highnote** (San Francisco — card issuing + Visa agentic-commerce work, May-2026) → row under **payauto.ai**.
   - **$90M Series B + >$750M valuation VERIFIED** — Forbes 2025-01-21 "Fintech Payments Startup Highnote Raises $90 Million, Valued At More Than $750 Million"; Business Wire; PaymentsJournal *(via GN)*.
   - "$173M total" (incl. $25M extension) **PARTIAL** — extension not separately located. Largest-capitalized of the three new candidates.
3. **Lithic** (New York — programmable virtual cards) → row under **payauto.ai**.
   - **$43M Series B VERIFIED** — Finovate 2021-05-20 "Privacy.com Rebrands to Lithic, Closes $43 Million in Series B Round" *(via GN)*.
   - **NEW data point beyond the source:** **$60M Series C led by Stripes** — Dealroom 2026-09-27 "Stripes leads Lithic's $60 million Series C" *(via GN)* → the source's ">$100M raised" is directionally confirmed and now understated.

## P4 — NEKUDA reconcile (KILL verdict)

- **Company-level: Visa Intelligent Commerce launch partner CONFIRMED** — PYMNTS 2025-12-22 "nekuda Powers Agentic Commerce with Visa Intelligent Commerce" *(via GN)*; Gensmo partnership PYMNTS 2025-11-12 *(via GN)*. The source's Visa-partner listing is true for the company (through Dec-2025).
- **Site-level: still dead 2026-10-25** — HTTP 000 (no route) on apex + www; Wayback CDX shows **zero 2026 captures** (last capture 2025-07-12, HTTP 200).
- **Verdict: KILL STANDS** — no live web presence to route outreach through; Nekuda stays out of targeting (watchlist-only). Nuance added to root CSV + workbench (company witnessed active as Visa partner into Dec-2025; site unreachable since before mid-2025 capture gap).

---

## Files changed (PR #98 · task a4146026)

- `DOMAINS/payauto.ai/01-research/AGENTIC-PAYMENTS-US-EXTERNAL-RESEARCH_2026-10-25.md` (source verbatim, md5-identical)
- `docs/AGENTIC-PAYMENTS-US-VERIFICATION_2026-10-25.md` (this doc)
- `DOMAINS/payauto.ai/01-research/payauto_ai_acquisition_targets.csv` (workbench — Team_Annotations ×8)
- `payauto_ai_acquisition_targets.csv` (root — funding_verification_status notes ×8, Nekuda source_urls)
- `payments_family_buyers_master.csv` (+3 rows, 67 total, ranks 65–67)
- `REPO_INDEX.md` (Quick Reference row + wave log)

SEND FREEZE honored — research + data-only, nothing fires.
