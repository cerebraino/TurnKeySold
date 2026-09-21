# TurnKeySold — Outreach Tooling Playbook

**Date:** 2026-09-20 · **Source:** `OUTREACH-TOOLING-RESEARCH_2026-09-07.md` (all prices/flags carried over unchanged; nothing re-researched) · **Owner of record:** TurnKeySold (Juan L. Aguirre)

---

## 0. How to use this document

**For the owner:** Read §1–§3 (context, purpose, hard constraints) once, then §4 (stack at a glance) and §8 ($100 allocation) to decide what to buy. §6 tells you exactly what *you* do vs. what the agents do at each phase. §7 shows how the CTO.new platform operates in tandem with these tools. When the send-freeze lifts, §10's verify-before-send discipline + tracking schema are the operating rules.

**For a collaborator LLM agent:** Treat this document as the complete, self-contained brief — do not assume any prior context. It tells you *why* each tool was chosen, *at what price*, *what to verify before using*, and *which workstreams belong to Phase 1*. If a price here is marked **UNVERIFIED**, never restate it as fact — tell the owner to confirm at the linked pricing page before purchase. The verification log (§11) lists every source URL and check date.

---

## 1. CONTEXT — who we are, what we're selling

- **TurnKeySold Domains** is the first vertical of TurnKeySold, an agentic sales company. We sell a **146-domain portfolio** of premium domains (asking **$3K–$45K** per domain; commission model = **20% success fee on each sale**, no upfront fees).
- We sell to **end-user buyers** — companies, startups, or individuals who would genuinely benefit from the exact name (e.g. curebyketo.com → keto-health companies; fusebot.ai → AI-automation startups). Buyers are identified through structured research (DMPS-scored lead lists + outbound-lead methodology) and contacted with **highly personalized copy**.
- The team is agentic: a research agent finds + verifies buyers, an outreach architect writes the ready-copy messages, a web developer builds landing pages, the lead coordinates. **The owner is the only human sender.**
- **Send-freeze (owner directive, 2026-09-04):** no emails of any kind until the owner gives explicit per-send instruction. **3 lifetime sends to date, 0 replies.** All outreach copy for ~19 leads across 4 packs exists and is READY-ONLY (HOLD-bannered) — it fires only when the owner unfreezes, per-send.
- This playbook is about the **tooling** that supports that pipeline — find + verify buyers, deliver outreach, track outcomes, close — not about the copy itself.

## 2. PURPOSE — what the stack is for

1. **Find** qualified buyers and their contact paths (enrichment).
2. **Verify** every address before any send (protect sender reputation).
3. **Deliver** low-volume, high-personalization outreach — **not bulk cold-blasting** (we send single-digit to low-double-digit sends/week, manually or lightly automated).
4. **Track** every lead, send, reply, and deal (CRM/Sheets).
5. **Collect inbound** (per-domain for-sale landing pages + offer forms).
6. **Close** via secure escrow (marketplace backstop for passive demand).

## 3. CONSTRAINTS (hard rules — never broken)

| # | Constraint |
|---|---|
| C1 | **Initial spend < $100 USD total.** Spend increases ONLY on results triggers (§6). |
| C2 | **Never-invent.** Only fireable contacts = literally published + real source URL. No guessed addresses, no permutations. |
| C3 | **Sender reputation is fragile.** Bounces/complaints pause ALL outbound email for the whole team, and neither owner nor agents can lift it. Verify before every send; stop at the first bounce. |
| C4 | **No LinkedIn automation on the owner's account.** ToS risk; the owner's LinkedIn identity is a primary channel. |
| C5 | **No pricing in first-touch copy.** |
| C6 | **Freeze until owner per-send instruction.** Ready copy is HOLD-bannered; nothing fires autonomously. |

---

## 4. THE STACK AT A GLANCE

| Category | Pick | Price (verified 2026-09-07 unless flagged) | Phase | Info URL | Signup URL |
|---|---|---|---|---|---|
| Sending (baseline) | Manual sends — business inbox + owner LinkedIn DM / site forms | $0 | 0 | — | — |
| CRM / tracking | Google Sheets (tab: `OUTREACH-TRACKER`) | $0 | 0 | — | — |
| Enrichment | **Hunter.io Free** (50 credits/mo) | $0 | 0 | https://hunter.io/pricing | https://app.hunter.io/register |
| Enrichment (backup) | **Apollo.io Free Starter** (free forever) | $0 | 0 | https://www.apollo.io/pricing | https://app.apollo.io/ |
| Verification | **MillionVerifier** credit pack | **$39 one-time** (≈10k credits @ $0.0039/credit) | 0 | https://www.millionverifier.com/ | https://app.millionverifier.com/ |
| Landing pages | **Carrd Pro** ×2 (curebyketo.com, fusebot.ai) | **$19/yr per site** | 0 | https://carrd.co (homepage: "Go Pro from just $19") | https://carrd.co (account created on-site) |
| Offer forms | **Tally** free | $0 | 0 | https://tally.so/pricing | https://tally.so/signup |
| Sending mailbox | Google Workspace Business Starter (1 seat, turnkeysold.com) | **$7/mo** (annual commitment) | 1 | https://workspace.google.com/pricing.html | https://workspace.google.com/signup/ |
| Mail-merge/tracking | **GMass** Standard | $29/mo monthly; **$20/mo billed annually** ($249/yr) | 1 | https://www.gmass.co/pricing | https://www.gmass.co (Google-OAuth from extension) |
| Deal tracking (optional) | **Streak** free (Gmail-native) | $0 free tier | 1 | https://www.streak.com/pricing | https://www.streak.com (via Chrome-extension install) |
| Sequencing | **Smartlead Base** (alt: Instantly Growth) | **$39/mo** (alt $47/mo) | 2 | https://www.smartlead.ai/pricing · https://instantly.ai/pricing | https://app.smartlead.ai/register · https://app.instantly.ai/ |
| Marketplace backstop | **Sedo + Afternic** (free-to-list) | $0 to list; commission % on sale (**UNVERIFIED** today) | 0 (list once) | https://sedo.com · https://www.afternic.com | sedo.com · afternic.com (register from site root) |
| Closing | **Escrow.com** | Per-transaction only (2.6%/min $50 ≤$5K; see §5) | 0 (when needed) | https://www.escrow.com/fee-calculator | https://my.escrow.com/register |

---

## 5. TOOL DETAILS

> Format per tool: **what it does / why picked / price (VERIFIED 2026-09-07 or UNVERIFIED flag) / setup (1–3 lines)**. Alternatives considered are listed with the reason they were rejected. Signup URLs below are site roots (account creation starts there).

### 5.1 Manual sends (business inbox + owner LinkedIn DM / site forms) — $0 · Phase 0
- **What:** The owner sends the ready-copy outreach manually: first-touch, D3/D7/D14 follow-ups, replies.
- **Why picked:** Baseline — the bar every tool must beat. Complies with the freeze; zero reputation risk beyond what we already carry; our volume (≤ ~20 sends/wk) makes it viable indefinitely.
- **Price:** $0. **Setup:** none.
- **Alternatives:** every sequencer in §5.11 — all cost $39+/mo and add warmup complexity we don't need at this volume.

### 5.2 Google Sheets (OUTREACH-TRACKER) — $0 · Phase 0
- **What:** System-of-record CRM. One row per lead; schema in §10.3.
- **Why picked:** Zero cost, zero lock-in, collaborator-LLM readable, already the team's working pattern.
- **Setup:** Create one sheet with the §10.3 columns. Agents write rows; owner updates send/reply status.

### 5.3 Hunter.io Free — $0 · Phase 0
- **What:** Finds/verifies email addresses by company domain (firstname@company patterns).
- **Why picked:** **50 free credits/mo verified on page** — exactly our volume; strong for the "no fireable email" gap.
- **Price:** Free **$0 — 50 credits/mo** (VERIFIED 2026-09-07). Paid: Starter **$49/mo monthly / $34/mo billed yearly** ($408/yr, 2,000 credits/mo) — **not now**.
- **Signup:** https://app.hunter.io/register (VERIFIED live 2026-09-21).
- **Setup:** Sign up free → search a company or paste a name → spend 1 credit per find; save results to the tracker.
- **Alternatives:** Snov $39/mo (mixed accuracy), Anymail $29/mo (fine but paid), Prospeo/ContactOut (**UNVERIFIED** pricing) — free tier wins at our volume.

### 5.4 Apollo.io Free Starter — $0 · Phase 0
- **What:** Enrichment database (companies, execs, emails) + free sends.
- **Why picked:** **Free Starter plan "free forever"** (VERIFIED via page FAQ). Backup to Hunter when credits run out.
- **Price:** Free. Trial = 50 credits + 5 mobile credits (page FAQ). Paid plans **UNVERIFIED** (JS page; historically ~$49/user/mo) — **not now**.
- **Signup:** https://app.apollo.io/ (sign-up flow on the app root; VERIFIED live 2026-09-21).
- **Setup:** Sign up → search accounts/people → use free credits; export rows (export credits apply) into tracker.
- **Alternatives:** none needed at $0; premium Apollo/ContactOut bundles rejected (C1/C3).

### 5.5 MillionVerifier — $39 one-time · Phase 0
- **What:** Bulk email verification (syntax + MX + catch-all checks).
- **Why picked:** The fragile-reputation insurance. Verify **every** address before **any** send (C3). Cheapest per-verification price in the researched set; credits never expire.
- **Price:** **$39 pack = ~10k credits @ $0.0039/credit**; $59 → $0.00236; $89 → $0.00178; $449 = 1M @ $0.00044; up to $2,599 @ $0.00025 (VERIFIED 2026-09-07, browser-checked). Free trial exists.
- **Signup:** https://app.millionverifier.com/ (VERIFIED live 2026-09-21).
- **Setup:** Buy $39 pack → paste list (or API) → mark results in tracker; delete/fix anything not `valid`.
- **Alternatives:** ZeroBounce (PAYG from $39, packs UNVERIFIED; 0.5–0.8¢/email historically — more expensive), DeBounce (cheap but page half-rendered → **UNVERIFIED** packs), NeverBounce (**UNVERIFIED**, 403 today). MillionVerifier wins on verified price.

### 5.6 Carrd Pro ×2 — $19/yr each · Phase 0
- **What:** One-page for-sale microsites on custom domains (buy-now + offer form), e.g. curebyketo.com and fusebot.ai landers.
- **Why picked:** Cheapest branded for-sale page per domain. **"Go Pro from just $19"** on homepage (VERIFIED 2026-09-07; per-site nuance UNVERIFIED — confirm at purchase).
- **Price:** **$19/yr per site** (free tier = *.carrd.co subdomain). **Signup:** https://carrd.co (account created on-site; Pro upgrade from the site). **Setup:** Create page → Pro upgrade → connect domain → embed Tally form.
- **Alternatives:** Typeform paid (**UNVERIFIED**, JS-walled) — pricier, no advantage; full site build (web-developer) — overkill until a domain generates traffic.

### 5.7 Tally (free) — $0 · Phase 0
- **What:** Forms: "Make an offer", "Request access", intake.
- **Why picked:** Free forms that embed cleanly in Carrd (and the team's site if needed).
- **Price:** Free plans exist (caps UNVERIFIED); Pro **$24/mo annual** — **not now** (VERIFIED 2026-09-07).
- **Signup:** https://tally.so/signup (VERIFIED live 2026-09-21).
- **Setup:** Create form → copy embed link into Carrd page → connect submissions to a Sheets row via webhook or manual.

### 5.8 Google Workspace Business Starter (1 seat) — $7/mo · Phase 1 (trigger: first interested reply)
- **What:** Isolated branded sender mailbox on turnkeysold.com.
- **Why picked:** The single cheapest reputation insurance (C3) once real, repeated sends begin. A paused inbox = dead team. Branded reply-to.
- **Price:** **$7/user/mo** with annual commitment (VERIFIED 2026-09-07 at https://workspace.google.com/pricing.html; monthly-billing price higher — UNVERIFIED exact). Standard $14/mo, Plus $22/mo — not needed.
- **Signup:** https://workspace.google.com/signup/ (VERIFIED live 2026-09-21).
- **Setup:** Add user (e.g. juan@turnkeysold.com) → verify domain DNS → start sending from it. Warmup tools (Instantly/Smartlead) need multiple mailboxes to be effective — one seat is the minimum viable sender.
- **Buy now or later?** **Later** — at Phase-1 trigger, not before (freeze makes an idle seat cost).

### 5.9 GMass Standard — $20/mo (annual) · Phase 1 (trigger: first interested reply)
- **What:** Mail-merge + tracking + reply-in-thread inside Gmail/Workspace (uses the mailbox itself — no separate platform).
- **Why picked:** Natural evolution of manual sends without moving to a cold platform; fits our personalization style.
- **Price:** Standard **$29/mo monthly / $20/mo billed annually** ($249/yr); Premium $39/$29; Professional $59/$49 (VERIFIED 2026-09-07). Free plan exists (email cap UNVERIFIED) — try free first.
- **Signup:** https://www.gmass.co (Google-OAuth signup from the extension; no separate registration page).
- **Setup:** Install Chrome extension → compose template with `{{First}}` merge fields → pick tracker rows → send. **Warmup:** none (rides Gmail/Workspace reputation — another reason to verify strictly).
- **Alternatives:** YAMM free (mail-merge only, paid tiers UNVERIFIED) — fine but less tracking; Brevo $9/mo — **not a cold-sequencer** (marketing/transactional email; useful later for form notifications).

### 5.10 Streak free (optional, Phase 1) — $0
- **What:** In-Gmail pipeline/deal stages for negotiated sales.
- **Why picked:** When a reply becomes a negotiation, Streak's free tier tracks stages inside the mailbox we already use.
- **Price:** Free tier exists (VERIFIED "Free to try"); Pro **$49/user/mo** ($59 monthly), Pro+ $69 ($89), Enterprise $129 ($159) — **not now** (VERIFIED 2026-09-07).
- **Signup:** https://www.streak.com (signup via Chrome-extension install in Gmail; no separate page found).
- **Setup:** Install extension → create pipeline (Queued→Sent→Replied→Negotiating→Closed) → drag deals.

### 5.11 Smartlead Base — $39/mo · Phase 2 (trigger: reply-rate ≥5% across ≥30 sends)
- **What:** Cold-email sequencing platform: multi-message cadences (D3/D7/D14), built-in warmup, per-mailbox sending limits.
- **Why picked:** The moment follow-up cadences can't be managed manually anymore. Cheapest verified sequencing entry with warmup included.
- **Price:** Base **$39/mo** (2,000 contacts, 6,000 emails/mo, 2,000 verified-emails included); Pro $59/mo (VERIFIED 2026-09-07). Free plan exists (limits UNVERIFIED).
- **Signup:** https://app.smartlead.ai/register (VERIFIED live 2026-09-21) · Instantly alt: https://app.instantly.ai/ (VERIFIED live).
- **Setup:** Create account → connect the Workspace mailbox (+ warmup rotations) → import tracker rows → enable cadences.
- **Alternatives (choose ONE at Phase 2):** Instantly Growth $47/mo (5k emails/mo, 1,500 uploaded contacts); Lemlist from $55/user/mo; QuickMail $49/mo (unlimited senders, 500k emails/mo); Woodpecker (usage-based, $7/100 prospects tooltip); Saleshandy Starter $34/mo annual; Reply.io **UNVERIFIED** (403). Smartlead is the price/volume sweet spot; Instantly if we prefer its UI/unlimited accounts.

### 5.12 Sedo + Afternic (marketplace backstop) — $0 to list · Phase 0 (list once)
- **What:** Passive secondary-market listings.
- **Why picked:** Free-to-list, capture organic demand, supplement active outreach. **dan.com now redirects to Afternic** (observed 2026-09-07) — plan around Afternic, not Dan.
- **Price:** $0 to list; sale commission **UNVERIFIED** today (Sedo historically ~9.5–15% tiered/min fee; Afternic historically 15% standard) — **confirm the exact % at listing time** (C2/C3 on claims, not cost).
- **Signup:** Account registration from site roots: https://sedo.com · https://www.afternic.com (deep /register URLs bot-blocked 403 on 2026-09-21 — register via the site root UI).
- **Setup:** List top-priority domains → set asking price → let Landers/parking routes catch demand.
- **Note:** Commission drives minimum viable asking price — at 15% commission + our 20% fee, a $15K domain nets the seller ~$10.2K. Don't list cheap.

### 5.13 Escrow.com — per-transaction · Phase 0 (when a deal forms)
- **What:** Escrow closing for direct owner-negotiated sales.
- **Why picked:** Protects both sides (no chargebacks against sellers), pay-per-transaction, no monthly. **The right default** for direct sales; marketplace sales include escrow — don't double-pay.
- **Price (VERIFIED 2026-09-07, fee-calculator, Standard tier):** $0–5K = 2.6% (min $50); $5,001–50K = 2.4% (min $130); $50,001–200K = 1.9% (min $1,200); $200K–500K = 1.5%; $500K–3M = 1.0%; +3M lower. Plus payment-processing (~+3% card) and **+$25 international-buyer bank fee**. Concierge ≈ 2× Standard. A $15K direct sale = **$360 (2.4%)**.
- **Signup:** https://my.escrow.com/register (account portal registration; VERIFIED live 2026-09-21).
- **Setup:** Start transaction at escrow.com → buyer funds → domain transfer → release.

---

## 6. SEQUENCE — phases, triggers, and who does what

### Phase 0 — NOW (≈ $77 one-time; $0–15/mo recurring) — "No results yet, no money"
| # | Action | Who |
|---|---|---|
| 1 | Keep sending $0: manual from business inbox + owner LinkedIn DM / site forms (freeze-compliant) | Owner |
| 2 | Set up `OUTREACH-TRACKER` sheet (§10.3) | Agent (research) |
| 3 | Buy **MillionVerifier $39** pack | Owner |
| 4 | Sign up **Hunter Free + Apollo Free**; start closing email gaps one verified address at a time | Agent (research) |
| 5 | Buy **Carrd Pro ×2** ($38/yr) for curebyketo.com + fusebot.ai; embed Tally offer forms | Owner buys · web-developer builds |
| 6 | Continue buyer research, WAF re-verification, ready-copy maintenance (freeze-respectful) | Agent (research) |

### Phase 1 — TRIGGER: **first interested reply** (recurring ≈ $27–61/mo; stay under ~$50 cap)
| # | Action | Who |
|---|---|---|
| 1 | **Google Workspace 1 seat $7/mo** on turnkeysold.com — isolate sender reputation | Owner |
| 2 | **GMass $20/mo (annual)** for merge/tracking; free tier first if caps suffice | Owner |
| 3 | **Hunter Starter $34/mo (annual)** only if enrichment > 50 finds/mo | Owner |
| 4 | **Streak free** for in-Gmail deal tracking if a negotiation opens | Agent + Owner |
| 5 | Continue verification-first discipline; stop at first bounce | All |

### Phase 2 — TRIGGER: **reply-rate ≥5% across ≥30 sends** (recurring ≈ $100/mo cap)
| # | Action | Who |
|---|---|---|
| 1 | **Smartlead Base $39/mo** (or Instantly Growth $47/mo) — cadences + warmup | Owner buys · outreach-architect configures |
| 2 | Add 1–2 warmup mailboxes inside the platform (~$6–21/mo each) if needed | Owner |
| 3 | **HubSpot Free CRM / Streak paid ($49/user)** only if a live pipeline demands it | Owner |
| 4 | Upgrade Apollo/Hunter only if credit-capped; keep everything else as-is | All |

**Rule:** never stack multiple phase-1 tools at once; add in the order above, only when the previous one is genuinely used.

---

## 7. CTO.NEW AS THE OPERATING LAYER — HOW THE PLATFORM WORKS IN TANDEM WITH THESE TOOLS

> **Framing rule applied here:** only capabilities that are already part of the TurnKeySold platform at plan cost are listed as "available". Anything plan-gated is explicitly flagged as gated — it is **not** asserted as available on the current tier. Tier prices below are the platform list (lead-provided baseline); **confirm exact tier pricing and current gating before upgrading** — treat them as UNVERIFIED here.

### 7.1 What CTO.new already provides at plan cost (verified working today)

| Capability | What it means for TurnKeySold |
|---|---|
| **Agent team + kanban task board** | The workforce: lead + domain-researcher / outreach-architect / web-developer, coordinated through a shared task board (`team-db`) with backlog → in-progress → review → done. This is where the pipeline gets executed and tracked. |
| **Shared work folder + GitHub repo workflow** | Agents prepare deliverables in `/home/team/shared` (research, packs, trackers); the lead reviews and commits/merges to the repo. Repo = the durable memory of what was researched, verified, and decided. |
| **Business email inbox with automatic bounce/complaint reputation tracking** | The platform-managed inbox (AgentMail/SES) is the owner-approval + inbound-monitoring channel. It automatically tracks bounces and spam complaints — crossing the threshold pauses ALL outbound email (this is the fragility in constraint C3). |
| **Website hosting + publishing for the team's live site (port 3000)** | TurnKeySold.com surface is published from the platform; the same publishing path can serve domain-focused pages. DNS/domain tooling for owned domains is available at the held plan — see gating note in §7.3. |
| **Connected Stripe account for real payments/invoicing** | Used to invoice the 20% success fee (two-rail money flow, §7.2). |
| **Scheduled tasks + webhooks** | **Plan-gated** (per §7.3). Not asserted as available today. |
| **MCP extensibility** | External tools exposing MCP servers can be granted natively to member agents (no manual copy-paste between tools and agents). |

### 7.2 Per-tool tandem mapping (tool category × CTO.new touchpoint × data flow)

| Tool category | Pick | CTO.new touchpoint | Data flow |
|---|---|---|---|
| Enrichment / verification | Hunter, Apollo, MillionVerifier | Agents execute the lookups (browser/API via the platform's tool access); CTO.new is the **labor + orchestration layer**, the tools are **data providers** | Lookup result → shared folder → repo CSV → `OUTREACH-TRACKER` |
| Landing pages | Carrd (external) **OR** platform-hosted for-sale page | **Two routes:** (a) Carrd external pages per tool spec; (b) CTO.new hosts a for-sale page **on the actual domain itself** (classic domain-sales practice) via the platform's site publishing + DNS tools | Route (b) requires serving on your own domain — **plan-gated (Plus tier, §7.3)**. Genuine trade-off: Carrd = $19/yr per site, zero platform-tier dependency, quick; platform-hosted = keeps the domain "developed" (better SEO/trust) but tier-gated. Neither is the declared winner. |
| Sending | Workspace / GMass / Smartlead | Sequencer operates the **campaign mailbox**; CTO.new inbox stays the **owner-approval + inbound-monitoring** channel; agents prep all copy | Copy from shared folder → owner per-send approval → sequencer sends from campaign mailbox; replies + bounces land in monitored inbox. **Reputation isolation is the point of the split.** |
| Tracking | team-db / Sheets | **Chosen: Sheets-first (`OUTREACH-TRACKER`), agent-updated** — matches §5.2/§10.3: agents write rows, owner updates send/reply status. CTO.new's `team-db` (SQLite, native to agents) remains the agent-side coordination record (task board, per-deal notes) | Trade-off: Sheets-first is human-familiar and owner-readable with zero sync machinery; team-db-first is more agent-native but would need an export path to Sheets for owner visibility. Keep Sheets as the single owner-facing truth; mirror deal status into team-db only as the lead sees fit. |
| Closing / money | Escrow.com + Stripe | **Two-rail money flow:** (1) Escrow.com handles the domain-transfer payment (buyer → escrow → seller); (2) CTO.new's connected Stripe invoices the 20% success fee | Both rails logged in the tracker (deal status + invoice status) so no commission is missed |
| Automation hooks | Webhooks + scheduled tasks | **Plan-gated (Pro tier, §7.3).** Webhooks can pipe sequencer events (replies/bounces) into the tracker; scheduled tasks can run periodic exec re-verification sweeps + inbox checks | Events → tracker updates; scheduled jobs → re-verification logs |
| MCP path | Any listed tool with an MCP server | Can be granted natively to a member agent (no manual copy-paste) | Same data flow as API/browser above |

### 7.3 Plan-tier pragmatism (factual, tier-gated — not free)

- Platform features are **tier-gated** per the platform's plan list: **email sending/receiving, webhooks, and scheduled tasks at Pro ($20/mo)**; **serving sites on your own domain at Plus ($60/mo)**. Treat these as the list baseline — confirm current prices/gating before upgrading (UNVERIFIED here).
- **Rule: upgrade tiers on the SAME results triggers as the tool stack (§6) — never pre-buy capability.** Pro is only worth it once a Phase-1 trigger (first interested reply) makes webhook-piped tracking valuable; Plus only when an actual domain needs an on-domain for-sale page.
- Heavy agent automation consumes platform usage allowance — **automation depth is itself a budget line**, not free. Deep automation + Pro tier should be treated as a Phase-2-style spend decision.

### 7.4 Division of labor — one-liner

> **External tools = specialized data, sending, and money rails. CTO.new = the workforce, the memory, the records, and the approval chain.**

---

## 8. THE $100 INITIAL ALLOCATION — buy today, and why

> **"Spend $77 now: MillionVerifier $39 one-time (~10k verifications to protect the team's fragile sender reputation — the single cheapest insurance that the send-pause never triggers), Carrd Pro × 2 at $19/yr each for for-sale pages on the two expansion-ready domains (curebyketo.com, fusebot.ai) with Tally's free offer-forms embedded, and $0 for Hunter Free + Apollo Free to start closing every 'no fireable email' gap with verified, published addresses. Hold the remaining ~$23 of the $100 budget in reserve for the Phase 1 first purchase — the $7/mo Google Workspace seat on turnkeysold.com that isolates our sending reputation the moment the first interested reply makes real sends imminent. Do not buy a sequencer, LinkedIn automation, or any paid CRM until the reply-rate trigger is proven — every one of those is a volume bet on a message we haven't yet validated, and each costs more per month than this entire initial stack costs per year."**

---

## 9. DO-NOT-BUY-YET list (good tools, wrong stage)

| Tool | Reason it violates pragmatism now |
|---|---|
| ❌ **LinkedIn automation** (Waalaxy / Expandi $99/mo / LinkedHelper from $15/mo / La Growth Machine $110/mo) | C4: HIGH ToS/account-restriction risk vs. our tiny volume; the owner's LinkedIn identity is a primary channel. Manual-first permanently at this volume. Revisit only at 100+/wk via a separate brand account — never the owner's. |
| ❌ **Premium Apollo / ContactOut bundles ($299+)/ Snov LinkedIn add-on ($69/mo)** | Enrichment at our volume is free-tier-able (Hunter 50/mo + Apollo free). C1. |
| ❌ **NeverBounce / ZeroBounce subscriptions** | MillionVerifier's verified $39 pack beats them on cost per verification at our volume. |
| ❌ **Lemlist Multichannel / Reply.io / QuickMail $49/mo / Woodpecker** | Feature-rich sequencers we can't yet use (volume + freeze). Revisit at Phase 2 with only ONE pick. |
| ❌ **Typeform paid** | Tally free covers forms. |
| ❌ **Any standalone warmup-as-a-service** (e.g. Mailreach) | No hot sender domain yet; Phase-2 platforms include warmup. |
| ❌ **Brevo paid ($9+/mo)** | Not a cold-sequencer; only useful later for form/landing notifications — free 300/day tier suffices if ever needed. |
| ❌ **All paid tiers of tools we chose for their free tier** (Hunter Starter, Apollo paid, GMass Premium+, Streak paid, Tally Pro, Notion Plus/Business, Airtable Team/Business, HubSpot paid) | Same job available at $0 until a trigger proves need. |

---

## 10. OTHER CONSIDERATIONS

### 10.1 Verify-before-every-send discipline (C3)
1. Every address goes through **MillionVerifier** before it appears in any send list; only `valid` results are fireable.
2. Addresses must also be **literally published** on a real source (company site, official press/Y Combinator page, HN profile) — never guessed patterns (first@, flast@).
3. **Stop at the first bounce.** Log it in the tracker with the date; adjust the source list. One bounce is a warning, two is a review.
4. When unsure, send to **fewer, known-good** addresses. Reputation once lost = whole team paused.

### 10.2 Opt-out language in templates
- Every template (first-touch and every follow-up) carries a **plain one-line opt-out**: "Happy to be taken off this list — just reply 'remove'." No manufactured urgency, no "URGENT"/"Action Required"/"Final notice" unless a real deadline exists.
- Honest framing only: never imply a prior conversation, agreement, or work we did not do (first contact ≠ "as we discussed").

### 10.3 Tracking table schema (minimum columns — `OUTREACH-TRACKER`)
```
domain | campaign/pack | lead_name | title | company | company_url | source_url | email
email_verified (MillionVerifier status + date) | linkedin_url | linkedin_status
first_sent_date | followup_1_date(D3) | followup_2_date(D7) | followup_3_date(D14)
reply_received (Y/N + date) | status (queued → sent → replied → negotiating → closed) 
next_action | next_action_date | owner_notes
```
Agents fill research/verify columns; owner fills send/reply columns. One row per lead; no deletions (archive closed).

### 10.4 Marketplace backstop
- List the top-priority domains on **Sedo + Afternic (free-to-list)**; Atom optional (brandable-focused). **Dan.com → Afternic redirect** (observed 2026-09-07): do not plan around Dan standalone.
- Confirm **exact commission % at listing time** (both sites JS-walled → UNVERIFIED today). Factor it + our 20% fee into the minimum asking price. Marketplace sales include escrow — don't double-pay with Escrow.com.

### 10.5 Closing — Escrow.com
- Pay-per-transaction, no monthly. Standard tier: 2.6%/min $50 (≤$5K) down to 0.9% at $5M+. +~3% card processing and +$25 international-buyer fee.
- Sub-$3K bundles (e.g. puticlub.online) are borderline — prefer bundling into the main domain or a marketplace sale.

### 10.6 Quarterly exec re-verification
- Exec roles/emails go stale. Every 3 months, re-check the fireable list against published sources (company sites, official announcements) and re-run MillionVerifier on anything about to be used. Log changes in the tracker.

### 10.7 How a collaborator LLM should use this playbook
- **Your Phase-1 workstream candidates** (do not purchase anything; prepare only):
  1. Build/refresh `OUTREACH-TRACKER` rows for the ~19 ready leads (schema §10.3), with source URLs + verification status.
  2. Draft the **WAF re-verification** pass for the next domain batch (curl checks for mailto:/LinkedIn paths — JS-heavy sites flagged).
  3. Prepare the **offer-form copy + Carrd page content brief** for curebyketo.com and fusebot.ai (no pricing in first-touch copy — C5).
  4. Draft a **bounce-log SOP** (what to do on first/second bounce, C3).
  5. When the owner lifts the freeze, prepare a **per-send checklist** referencing §10.1–§10.2.
- **Do not:** sign up, purchase, or send. All purchases are owner-executed; all sends are owner-authorized per-send.

---

## 11. VERIFICATION LOG (all prices checked 2026-09-07)

**Verified live (page text/JSON):** Instantly, Smartlead, Lemlist, Woodpecker (slider + add-ons), Saleshandy, QuickMail, GMass, Brevo, Apollo (FAQ), Hunter, Snov, Anymail, Kaspr, MillionVerifier (browser), ZeroBounce, DeBounce (partial), Expandi, LinkedHelper, La Growth Machine, Airtable, Notion, Streak, Carrd (homepage), Tally, Atom, Escrow.com fee-calculator, Google Workspace pricing, dan.com→Afternic redirect.

**Blocked/JS-walled today (flagged UNVERIFIED — never restate as fact):** Reply.io (403), NeverBounce (403), Prospeo, ContactOut (partial), Typeform, HubSpot, Sedo commission exacts, Afternic commission exacts, Waalaxy € prices, YAMM paid tiers, Carrd per-site nuance.

**Annual-vs-monthly traps flagged (prefer annual where listed):** Saleshandy (~25% cheaper annual), GMass (~31%), Anymail (~33%, "yearly to save 33%"), Hunter ($34 vs $49), Snov (~25%), Instantly bundles (annual-billed), Notion ($10 vs $12, custom-domain Sites $8 annual / $10 monthly), Tally ($24 vs presumably ~$29), Carrd ($19/yr vs $0 subdomain free), Google Workspace (annual commitment for $7/user).

**Change note:** This playbook carries the research doc's prices/flags forward unchanged (2026-09-07 baseline). Prices should be re-confirmed at the linked pages before any purchase, especially anything marked UNVERIFIED.
**Signup-URL additions (checked live 2026-09-21):** app.hunter.io/register (200), app.apollo.io/ (200), app.millionverifier.com/ (200), carrd.co (register on-site), tally.so/signup (200), workspace.google.com/signup/ (200), gmass.co (OAuth via extension), streak.com (via extension), app.smartlead.ai/register (200), app.instantly.ai/ (200), sedo.com · afternic.com (root UI; deep /register URLs bot-blocked 403), my.escrow.com/register (200). No prices or flags changed in this pass.
**§7 platform note:** CTO.new tier pricing/gating (Pro $20/mo, Plus $60/mo) is the lead-provided platform-list baseline — flagged UNVERIFIED here; confirm exact gating before any upgrade.