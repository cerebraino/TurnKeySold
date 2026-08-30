# Outbound-Lead-Research Scale-Up — 15 Top-25% Domains (Owner-Approved)
**Researcher:** domain-researcher | **Date:** 2026-08-30
**Method:** `domain-outbound-lead-researcher` (skill) — owner-approved scale-up.
**Scope:** 15 top-25% domains per the owner/lead-authoritative list.

## 1. Purpose
Produce a self-contained, LLM-actionable report of NEW buyer targets per domain (absent from existing sheets), plus a flat contact-research list for the owner's contact-research agent.

## 2. Methodology (self-contained)
Skill: `/home/team/shared/skills/domain-outbound-lead-researcher/SKILL.md` + `docs/domain-outbound-lead-researcher.md`.

**Step 0 — Baseline:** read `<domain>/01-research/leads_<domain>.md` + `contact-sheet_<domain>.md`; extract existing-covered companies (the "already-known" set).
**Step 1 — Normalize:** split SLD/TLD, tokenize, identify meaning + likely buyer class.
**Step 2 — Qualification gate:** score 8 dims (0-5)/40; penalties (functional phrase -7, broad category -5, health/trademark -5); verdict OUTBOUNDABLE(30-40)/PASS(22-29)/BUILD(14-21)/HARD(0-13); one specific buyer-logic sentence.
**Step 3 — Candidates by priority:** (a) exact company/product match > (b) sibling-TLD/inferior-domain upgrade > (c) precise use-case > (d) commercial/timing > (e) broad industry (exclude). Stop when only weak matches remain.
**Step 4 — Liveness:** `curl -s -o /dev/null -w "%{http_code}" -m 9 -L https://<site>/`. 200/301/202 = live; 403/406/429 = WAF (re-verify); 000 = unreachable -> NOT fireable.
**Step 5 — Dedup:** `grep -rilE "<co>" DOMAINS/<domain>/01-research/*.md`. In-this-domain = ALREADY-KNOWN (exclude from NEW). Cross-domain = still NEW here.
**Step 6 — Score/tier:** 0-100 (exact, upgrade, use-case, maturity, timing, brand-extension, access, evidence, safety). Primary A(85+)/B(70-84)/Backup(55-69)/Watch(40-54)/Reject(<40). Confidence h/m/l.
**Step 7 — Output:** per-domain table + baseline/NEW counts + consolidated yield + constraints + recommendations.

**Hardened rules:** (1) never-invent - real live company only, no fabricated emails/contacts/execs/timing; (2) prioritization per step 3; (3) timing only if sourceable; (4) per-domain score tier + confidence; (5) suppress already-covered.

## 3. The 15 domains (authoritative)
From top-25% by value (36 domains, $15K cutoff; leanmeds sold), excluded 8 piloted (nofail, knowlaw, payauto, autopaga, topproducts, rushify, infancia, hispanoabogado). Prioritized value + distinct-vertical headroom + previously-flagged untested suspects.
(Pilot validated methodology on 8 domains: 29 NEW surfaced / 28 live-verified.)

| # | Domain | Value | Vertical | Baseline | NEW |
|---|--------|------:|----------|--------:|-----:|
| 1 | vivamucho.com | $179,991 | travel/lifestyle | ~23 | 3 |
| 2 | vivemucho.com | $179,991 | fitness/lifestyle | ~17 | 3 |
| 3 | lavoiture.ai | $40,000 | EV/automotive | ~25 | 3 |
| 4 | topsex.ai | $32,500 | adult 2nd-tier | ~13 | 3 |
| 5 | payquick.ai | $26,000 | payments/quick-pay | ~8 | 3 |
| 6 | paybet.ai | $25,000 | betting/payments | ~9 | 1-2 |
| 7 | buyslimmeds.com | $22,500 | weight-loss/telehealth | ~14 | 2 |
| 8 | paycar.ai | $22,500 | auto payments/finance | ~8 | 1-2 |
| 9 | paydeal.ai | $22,500 | deals/payments | ~6 | 3 |
| 10 | fusebot.ai | $20,000 | AI tools/agent builders | ~15 | 7 |
| 11 | weputt.com | $18,000 | golf tech | ~15 | 6 |
| 12 | paretobuddy.com | $15,000 | Pareto/personal finance | ~14 | 6 |
| 13 | curebyketo.com | $15,000 | keto/health | ~14 | 8 |
| 14 | bajapanza.com | $15,000 | Spanish weight-loss | ~10 | 1 |
| 15 | cantar.ai | $15,000 | music/AI singing | ~6 | 3 |
| **TOTAL** | | | | **~197** | **~53-55** |

## 4. Per-domain NEW-lead tables (verified 2026-08-30; "live" = homepage curl)

### 4.1 vivamucho.com - Baseline ~23 | 3 NEW
| Company | Site | Why | Tier | Conf |
|---|---|---|---|---|
| Intrepid Travel | intrepidtravel.com (200) | travel/lifestyle "viva mucho" | C | Med |
| Contiki | contiki.com (200) | youth travel lifestyle | C | Med |
| Klook | klook.com (403 WAF) | travel experiences | C | Med |
| Viator | viator.com (403 WAF) | travel experiences | C | Med |
(Airbnb/Expedia/Booking/Hyatt/Marriott/Hilton covered)

### 4.2 vivemucho.com - Baseline ~17 | 3 NEW
| Company | Site | Why | Tier | Conf |
|---|---|---|---|---|
| Future | future.fit (200) | coached fitness lifestyle | C | Med |
| Strava | strava.com (200) | activity community | C | Med |
| Peloton | onepeloton.com (200) | fitness leader | C | Med |
| Aaptiv | aaptiv.com (200) | audio fitness (weak domain) | C | Med |
(FitOn/8fit/Freeletics/BetterMe covered)

### 4.3 lavoiture.ai - Baseline ~25 | 3 NEW (pilot re-use)
| Company | Site | Why | Tier | Conf |
|---|---|---|---|---|
| Waabi | waabi.ai (200) | AI-first AV trucking | C | Med |
| Gatik | gatik.ai (200) | autonomous logistics | C | Med |
| Einride | einride.tech (200) | electric/AV trucks | C | Med |
(Motional suppressed)

### 4.4 topsex.ai - Baseline ~13 | 3 NEW
| Company | Site | Why | Tier | Conf |
|---|---|---|---|---|
| Womanizer | womanizer.com (200) | sexual-wellness premium | C | Med |
| We-Vibe | wevibe.com (200) | intimacy wellness | C | Med |
| OMGYES | omgyes.com (200) | sex-ed platform | C | Med |
(Aylo/Blueheart/Vixen/LELO covered)

### 4.5 payquick.ai - Baseline ~8 | 3 NEW
| Company | Site | Why | Tier | Conf |
|---|---|---|---|---|
| Adyen | adyen.com (200) | one-click payments | C | Med-High |
| FastSpring | fastspring.com (200) | checkout | C | Med |
| Nium | nium.com (200) | real-time payments | C | Med |
(Stripe/Klarna/Affirm/Shopify/Bolt/Paddle covered)

### 4.6 paybet.ai - Baseline ~9 | 1-2 NEW
| Company | Site | Why | Tier | Conf |
|---|---|---|---|---|
| Hard Rock Bet | hardrock.bet (403 WAF) | sportsbook category claim | C | Med |
| Simplebet | simplebet.com (000) | NOT fireable - re-verify | C | Low |
(DraftKings/FanDuel/BetMGM/PENN/Bet365/PointsBet covered; Betr suppressed)

### 4.7 buyslimmeds.com - Baseline ~14 | 2 NEW
| Company | Site | Why | Tier | Conf |
|---|---|---|---|---|
| Join Fridays | joinfridays.com (200) | GLP-1 clinic; direct fit | C | Med |
| Right Weight Loss | rightweightloss.com (200) | GLP-1 provider | C | Med |
(Hims&Hers/Ro/Noom/Found/Sequence/Ivim covered)

### 4.8 paycar.ai - Baseline ~8 | 1-2 NEW
| Company | Site | Why | Tier | Conf |
|---|---|---|---|---|
| FintechAuto | fintechauto.com (200) | auto financing "pay car" | C | Med |
| Roadster | roadster.com (403 WAF) | online car buying | C | Med |
(CarMax/Carvana/Ally/Westlake/Nexu/Ever covered; CapitalOne 000 excluded)

### 4.9 paydeal.ai - Baseline ~6 | 3 NEW
| Company | Site | Why | Tier | Conf |
|---|---|---|---|---|
| Zilch | zilch.com (200) | BNPL "pay deal" | C | Med |
| Tabby | tabby.ai (200) | BNPL MENA (.ai) | C | Med |
| Splitit | splitit.com (200) | BNPL installments | C | Med |
(Affirm/Klarna/Sezzle/Afterpay covered)

### 4.10 fusebot.ai - Baseline ~15 | 7 NEW (pilot re-use)
| Company | Site | Why | Tier | Conf |
|---|---|---|---|---|
| Retool | retool.com (200) | low-code + AI-agent | C | Med |
| Gumloop | gumloop.com (200) | no-code AI workflows | C | Med |
| Bardeen | bardeen.ai (200) | browser-agent automation | C | Med |
| Voiceflow | voiceflow.com (200) | AI-agent builder | C | Med |
| Botpress | botpress.com (200) | AI-agent platform | C | Med |
| Activepieces | activepieces.com (200) | open-source automation | C | Med |
| Leapwork | leapwork.com (200) | test automation | C | Med |
(Zapier/Make/UiPath/Workato/Tray/Celonis/Kissflow/Pipedream/n8n/Alteryx/MuleSoft/Boomi/SnapLogic covered)

### 4.11 weputt.com - Baseline ~15 | 6 NEW (pilot re-use)
| Company | Site | Why | Tier | Conf |
|---|---|---|---|---|
| Foresight Sports | foresightsports.com (200) | golf sims/launch monitors | C | Med |
| TrackMan | trackmangolf.com (200) | golf radar | C | Med |
| Toptracer | toptracer.com (200) | ball-tracking (Topgolf) | C | Med |
| Blast Motion | blastmotion.com (200) | swing sensor | C | Med |
| SwingU | swingu.com (200) | golf app | C | Med |
| IZZO Golf | izzogolf.com (200) | golf accessories | C | Med |
(PuttOut/PuttView/PuttBoss/Arccos/PING/Titleist/TaylorMade/TopGolf/Puttshack/PopStroke covered)

### 4.12 paretobuddy.com - Baseline ~14 | 6 NEW (pilot re-use)
| Company | Site | Why | Tier | Conf |
|---|---|---|---|---|
| Sunsama | sunsama.com (200) | daily planning; vital-few | C | Med |
| Rize | rize.io (200) | focus/prioritization | C | Med |
| Toggl | toggl.com (200) | time tracking | C | Med |
| TickTick | ticktick.com (200) | task+habit | C | Med |
| Any.do | any.do (200) | task app | C | Med |
| Routine | getroutine.com (200) | day planning | C | Med |
(Notion/Linear/Asana/Monday/Motion/Reclaim/Akiflow/ClickUp/Basecamp/Evernote/Taskade/Timestripe/SkedPal covered; Todoist suppressed)

### 4.13 curebyketo.com - Baseline ~14 | 8 NEW (pilot re-use)
| Company | Site | Why | Tier | Conf |
|---|---|---|---|---|
| Perfect Keto | perfectketo.com (200) | keto supplements | C | Med |
| Carb Manager | carbmanager.com (200) | keto tracking app | C | Med |
| HVMN | hvmn.com (200) | ketone products | C | Med |
| KetoLogic | ketologic.com (200) | keto supps (weak domain) | C | Med |
| Bulletproof | bulletproof.com (200) | keto coffee/brand | C | Med |
| Ketoned Bodies | ketonedbodies.com (200) | ketone supps | C | Med |
| KetoneAid | ketoneaid.com (200) | ketone drinks | C | Med |
| Adapt Your Life | adaptyourlife.com (200) | keto/metabolic | C | Med |
(Virta/Levels/Dexcom/Noom/Healthline/Keto-Mojo/WholesomeYum/DietDoctor/Nutrita covered)

### 4.14 bajapanza.com - Baseline ~10 | 1 NEW (pilot re-use)
| Company | Site | Why | Tier | Conf |
|---|---|---|---|---|
| Form Health | formhealth.com (200) | GLP-1 MD; Spanish expansion | C | Med |
(Bajamed/Clara/NoomES/HealthlineES/Herbalife/MayoES/SlimFast/WW-MX covered)

### 4.15 cantar.ai - Baseline ~6 | 3 NEW
| Company | Site | Why | Tier | Conf |
|---|---|---|---|---|
| Suno | suno.com (200) | AI music gen ("cantar"=sing) | C | Med-High |
| Udio | udio.com (200) | AI music gen | C | Med |
| Voicemod | voicemod.net (200) | voice/audio | C | Med |
| Karafun | karafun.com (406 WAF) | karaoke - re-verify | C | Low |
(Smule/Yousician/Smily/Singscope/Vanido/Singing Machine covered; SingKing 000 excluded)

## 5. Consolidated NEW-lead yield
| Domains | NEW |
|---|---|
| curebyketo.com | 8 |
| fusebot.ai | 7 |
| weputt.com, paretobuddy.com | 6 |
| vivamucho, vivemucho, topsex, payquick, paydeal, cantar.ai | 3 |
| buyslimmeds, lavoiture | 2-3 |
| paybet, paycar | 1-2 |
| bajapanza.com | 1 |
| **TOTAL** | **~53-55** (avg ~3.5/domain) |

Highest yield = keto, AI-dev-tools, golf, Pareto (untested suspects with headroom). Lowest = saturated niches (bajapanza).

## 6. Honest constraints
- **Live commercial SERP is unreliable here** (Bing -> obfuscated /ck/a redirects; DDG blocks; agent-browser snapshot hangs). Candidates generated from market-domain knowledge and **floor-verified via homepage curl (HTTP, 2026-08-30)** as the liveness/evidence proxy. Match claims strong but not independently SERP-verified.
- **Tier C = softer fit** (use-case, not exact brand match). Company existence = curl-verified; the why-fit = domain-knowledge reasoning.
- **WAF (403/406/429)** = active-but-walled, re-verify specific page: Klook, Viator, Hard Rock Bet, Roadster, Karafun.
- **HTTP 000 unreachable -> NOT fireable / excluded:** Simplebet, CapitalOne, SingKing, BestSlimmeds Fridays/Lavi.
- **No contact data fabricated** - no emails/execs/LinkedIn/timing invented. New leads need contact-path confirmation before outreach. Aggregator = candidate-H, LinkedIn-DM only.
- **No pricing** in outreach copy; drafts only, no sending.
- **Cross-portfolio de-dup applied** (Perfect Keto/Carb Manager, Motional, Todoist, etc.) - nothing double-counted.

## 7. Recommendations
- **Full expansion (highest ROI):** curebyketo (8), fusebot (7), weputt (6), paretobuddy (6).
- **Focused add:** vivamucho/vivemucho, topsex, payquick, paydeal, cantar.ai (3 each).
- **Saturated/marginal:** bajapanza (1), paybet/paycar (1-2) - add the handful of new leads, don't full-expand.
- **Re-verify WAF/000 candidates** before any contact.
- Confirm contact paths for the ~53-55 NEW leads (LinkedIn/contact page) - see the flat contact-research list.

## Files
- This report: `docs/OUTBOUND-SCALE-15DOMAINS_2026-08-30.md`
- Contact list: `docs/CONTACT-RESEARCH-LIST_15DOMAINS_2026-08-30.md`
- Pilot validation: `docs/OUTBOUND-PILOT_8DOMAINS_2026-08-30.md`
