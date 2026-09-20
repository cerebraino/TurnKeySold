# TurnKeySold — Outreach Tooling Research

**Date:** 2026-09-07 · **Author:** domain-researcher (for owner + lead decision)
**Scope:** tooling across A–H categories for low-volume, high-personalization outreach with strict pragmatism (initial spend < $100 total; scale ONLY on results).
**Sourcing rule applied:** every price below was fetched from the vendor's own pricing page on **2026-09-07** (curl/agent-browser). Anything I could not verify on the live page today is marked **UNVERIFIED** and left to a human double-check before purchase. No signups, no purchases were made.

---

## 0. Context that should drive every choice

- We send **low volume** (single-digit to low-double-digit sends/week), **highly personalized**, to **verified decision-makers** — never bulk blasting.
- Most sends are **owner-manual** (LinkedIn DM / site form) from ready copy. The team's email reputation is fragile: bounces/complaints pause ALL sending.
- The single cheapest reputation safeguard is **not** sending to unverified addresses + using a **separate mailbox** for any future higher-volume sends. That costs ~$7/mo (Google Workspace), not $100s.
- Sequencing platforms (Instantly/Smartlead et al.) solve *volume + automation + warmup* — we do not yet have the volume to justify them. They are Phase 2 when reply-rate ≥5% across ≥30 sends proves the message works.

---

## A. Email sequencing / outreach platforms

**Baseline: manual sends from our existing business inbox = $0/mo.** This is the bar every tool must clear.

| Tool | Entry tier (verified 2026-09-07) | Free tier | Limits @ entry | Warmup req. | Setup complexity | Source URL |
|---|---|---|---|---|---|---|
| **Instantly.ai** | Growth **$47/mo** (5,000 emails/mo, 1,500 uploaded contacts, unlimited email accounts); Starter bundle **$85/mo** (annual-billed; $94 monthly) | No (referral/bundles only) | See left; Scale $194/mo (100k emails), Lightspeed $358/mo | Built-in SISR warmup | Medium — needs 1+ sending inboxes | https://instantly.ai/pricing |
| **Smartlead.ai** | Base **$39/mo** (2,000 contacts, 6,000 emails/mo, 2,000 verified-emails included); Pro **$59/mo** | Free plan exists (limited; UNVERIFIED limits) | Left | Built-in warmup | Medium | https://www.smartlead.ai/pricing |
| **Lemlist** | Email plan **From $55/user/mo** (monthly billing; annual cheaper — UNVERIFIED); Multichannel From $87/user/mo | Free plan exists ("Sign up for free") — UNVERIFIED limits | 14-day free trial; credits for enrichment extra | Built-in warmup | Medium | https://www.lemlist.com/pricing |
| **Woodpecker.co** | Usage-based slider by "contacted prospects"; page shows **$7.00 per 100 contacted prospects** tooltip; add-ons: LinkedIn accounts $29/mo, extra warmups $5/mo, email addresses $6/mo (Google/MS) or $4/mo (Maildoso et al.) | Warmups/emails/domains "FREE" listed; entry plan price UNVERIFIED (slider) | Scales with prospects | Built-in warmups (4 free; more $5/mo) | Medium | https://woodpecker.co/pricing/ |
| **Reply.io** | Page 403'd on 2026-09-07 → **UNVERIFIED** (historically ~$49/mo entry) | n/a | n/a | n/a | Medium | https://reply.io/pricing |
| **Saleshandy** | Starter **$34/mo** billed annually ($408/yr; if paid monthly more — UNVERIFIED); Pro $76/mo annual; Scale $149/mo annual | No (7-day free trial) | Email verification included + credits; mailbox add-ons (e.g. Microsoft $2.99–$3/mailbox/mo shown) | Built-in warmup | Low–Med | https://www.saleshandy.com/pricing |
| **QuickMail** | **$49/mo** (unlimited email senders, 2 workspaces, +$49/extra workspace, 100k uploaded contacts, 500k emails/mo); $99/mo, $299/mo | No | Left | Built-in auto-warmup ("Free Auto...") | Low–Med | https://quickmail.com/pricing |
| **GMass** | Standard **$29/mo** (monthly; **$20/mo** billed annually = $249/yr); Premium $39/$29 ($349/yr); Professional $59/$49 ($599/yr) | Free plan exists (free Google Sheets CRM + free email-address verification on page; email cap UNVERIFIED) | Uses your Gmail/Workspace itself — good fit for low volume | None (rides Gmail rep) | **Low** — fits our current style (manual sends from Gmail w/ tracking & mail-merge) | https://www.gmass.co/pricing |
| **YAMM** | Paid tiers UNVERIFIED (pricing page 404'd) | Free plan ("Get started for free") — UNVERIFIED limits (historically 50 emails/day) | Mail-merge from Google Sheets in Gmail | None | **Low** | https://www.yamm.com/ |
| **Brevo** | Starter **$9/mo** (5k emails/mo), Standard **$18/mo**, Professional $499/mo (USD monthly per page JSON; annual terms cheaper/mo) | **Free $0/mo (300 emails/day)** | Transactional/marketing email — **NOT a cold-outreach sequencer**; usable later for domain-for-sale form notifications or a waitlist confirm | n/a | Low | https://www.brevo.com/pricing |

**Read on A:** For *today's* volume, GMass ($0 free tier or $20–29/mo) or manual Gmail + free YAMM is the pragmatic pick. Instantly/Smartlead/QuickMail only make sense when we have ≥30 sends/mo worth automating + a warmup need. **Annual vs monthly trap:** Saleshandy/GMass/Anymail all price annual ~25–33% below monthly; Instantly's "Starter $85/mo" is the annual-billed bundle of a $94/mo plan — never buy monthly at these tools unless testing.

---

## B. Contact enrichment / email-finding (closes our "no fireable emails" gap)

| Tool | Free tier (verified) | Paid entry | Unit economics | Accuracy reputation | Source URL |
|---|---|---|---|---|---|
| **Apollo.io** | **Free Starter plan (free forever)** — page FAQ confirms "Starter plan which is free forever"; trial = 50 credits + 5 mobile credits | Paid plans UNVERIFIED on page (JS; historically ~$49/user/mo) | Unlimited plans: 10,000 credits/account/mo (per FAQ); overflow $0.025/credit | Good for companies; exec email coverage decent | https://www.apollo.io/pricing |
| **Hunter.io** | **Free $0 — 50 credits/mo** (verified on page) | Starter **$49/mo monthly / $34/mo billed yearly** ($408/yr) — 2,000 credits/mo; Growth $149/$104 | ~$0.017–0.025/verified credit at Starter | Strong for domain-based patterns (firstname@company) | https://hunter.io/pricing |
| **Snov.io** | Free trial; **Starter $39/mo** (page shows "$39.00/mo, Save $117/yr" → ~$29/mo annual); Pro S $99/mo | LinkedIn automation add-on $69/mo/slot (separate) | Credits-based (1,000s); UNVERIFIED exact | Mixed; fine for volume, verify before send | https://snov.io/pricing |
| **Anymail Finder** | free tier exists (UNVERIFIED limit; historically 3 credits/day) | **$29/mo = 400 credits ($0.073/credit)**; $49/mo = 1k ($0.049); $89/mo = 2k ($0.045); "yearly to save 33%" | See left | Good | https://anymailfinder.com/pricing |
| **Prospeo** | UNVERIFIED (pricing page rendered no prices today) | UNVERIFIED (historically ~$39/mo) | n/a | Good | https://prospeo.io/pricing/ |
| **ContactOut** | UNVERIFIED (page shows only Sales/Recruiter bundles) | Page shows **$299** tier ("Unlimited sales users") — **UNVERIFIED** lower tiers | n/a | Good but pricier | https://contactout.com/pricing/ |
| **Kaspr** | **Free €0/$0 per user/mo** (verified on page) | Starter **$49/mo per user** (page: €45/€59 · $49/$65 — annual/monthly dual pricing); Business $79/$99 | Credit usage based | Decent European coverage (LinkedIn-sourced) | https://www.kaspr.io/pricing/ |

**Read on B:** **Hunter Free (50 credits/mo) + Apollo Free (free forever)** gives us ~2 tools for $0 to close the "no fireable emails" gap one address at a time — exactly our volume. Pay nothing until we hit ~50 email finds/mo. Never-buy: Snov LinkedIn add-on, ContactOut bundles, enterprise Apollo.

---

## C. Email verification (protect sender rep)

| Tool | Free tier | Paid entry (verified 2026-09-07) | Cost per verification | Notes | Source URL |
|---|---|---|---|---|---|
| **MillionVerifier** | Free trial (page: "Free Trial") | **$39 pack = ~10k credits @ $0.0039/credit**; $59 → $0.00236; $89 → $0.00178; $149; $299; **$449 = 1M verifications ($0.00044)** up to $2,599 ($0.00025) | 0.04¢–0.39¢/email (best prices anywhere in this set) | "Credits never expire, bulk discounts stack" | https://www.millionverifier.com/ (browser-checked) |
| **ZeroBounce** | Freemium $0/mo (page shows) | **Pay-as-you-go from $39**; ZeroBounce ONE subscription $99 | Pack sizes UNVERIFIED (historically ~0.5–0.8¢/email) | Strong, widely used | https://www.zerobounce.net/pricing/ |
| **DeBounce** | 100 free credits (UNVERIFIED — page shows $0 tiers) | "Pay-As-You-Go" credit packs — exact pack prices UNVERIFIED (page JS-half-rendered) | Historically ~0.02–0.2¢/email (cheap) | Cheap, decent | https://debounce.io/pricing/ |
| **NeverBounce** | none confirmed | 403 today → **UNVERIFIED** | historically ~0.4¢/email | n/a | https://neverbounce.com/pricing/ |

**Read on C:** **MillionVerifier is the pick.** $39 gets ~10k verifications at 0.39¢ each — we'd verify every address we ever plan to send to for a year. ZeroBounce if we ever need highest-accuracy + integration. Never buy monthly subscriptions for verification at our volume — buy one credit pack and stop.

---

## D. LinkedIn: manual-first vs automation

**Baseline: manual-first = $0.** You are the bottleneck-killer: our leads already carry LinkedIn URLs; sending a connect request + DM manually from the owner's account takes ~1–2 min per lead and carries **zero account risk**.

Automation tools and their risk on the owner's profile:

| Tool | Entry price (verified 2026-09-07) | ToS / account-restriction risk |
|---|---|---|
| **Waalaxy** | Free trial; paid tiers UNVERIFIED (pricing page didn't render; historically ~€40/mo) | **HIGH** — browser-automation; LinkedIn actively restricts automated activity (temporary + permanent bans documented) |
| **Expandi** | **$99/mo** monthly plan (page states monthly plan for $99) | **HIGH** — cloud-based automation, fewer detections but still violates LinkedIn ToS; account ban risk remains |
| **LinkedHelper** | from **$15/license/mo** (page: "base price per license $15", ~$8 local / $16 cloud, term/volume discounts) | **HIGH** — same automated-activity class |
| **La Growth Machine** | **$110/mo** Pro (page: "lgm pro is just $110/mo") | **HIGH** |
| **Karafun of LinkedIn tools** (any "auto-invite/auto-follow" bot) | n/a | **HIGH** — do not touch |

**Recommendation:** **Manual-first, permanently at our volume.** LinkedIn automation violates the platform's User Agreement; a restriction on the owner's account would kill our #1 channel (the DM/form strategy in the ready packs depends on the *owner's* LinkedIn identity). At ~10–20 sends/week, automation saves maybe 1–2 hrs/mo for $100+/mo + existential account risk. **DO NOT BUY.** (If volume ever reaches 100+/wk, revisit via a *separate* brand-account, never the owner's.)

---

## E. Tracking / CRM

| Tool | Free tier (verified) | Paid | Fit for us |
|---|---|---|---|
| **Google Sheets (baseline)** | $0 | n/a | **Keep as the system of record.** One row per lead: domain, campaign, source URL, status (queued→sent→replied→negotiating→closed), next action date. Zero cost, zero lock-in. |
| **Airtable** | Free plan exists (1,000 records/base — UNVERIFIED cap) | Team $20/user/mo; Business $45/user/mo (page) | Nice structured UI + automations; only when Sheets gets unwieldy (>~500 rows) |
| **Notion** | **Free $0** | Plus $10/seat/mo (annual), Business $20/seat/mo (annual); Sites custom domain $8/mo (annual) | Good free alternative w/ linked databases; no email-native tracking |
| **HubSpot Free CRM** | Free CRM ($0; page JS-walled today but free tier is longstanding — treat as UNVERIFIED-in-detail) | Starter etc. UNVERIFIED today | Overkill now; useful later if a buyer pipeline + forms needed |
| **Streak (Gmail-native)** | "Free to try" free plan exists | Pro **$49/user/mo** ($59 monthly); Pro+ $69 ($89 monthly); Enterprise $129 ($159 monthly) | If we want email-native pipeline views (deal stages inside Gmail) for negotiated deals; $0 free tier worth a look for Phase 1 |

**Read on E:** Sheets covers Phase 0 and Phase 1. Add **Streak free** only when we have live deals to track in-inbox. No paid CRM until a domain actually closes.

---

## F. Landing / forms (per-domain for-sale pages for top-10 PRIORITY domains)

| Tool | Entry price (verified 2026-09-07) | Free tier | Fit |
|---|---|---|---|
| **Carrd** | **Pro $19/yr per site** (homepage: "Go Pro from just $19"; annual per-site — historic $9→$19 change; per-site UNVERIFIED nuance) | Free sites on *.carrd.co subdomains | **Best fit**: one-page for-sale site per domain ($19/yr each, custom domain, no branding, form + buy button). Top-10 priority = ~$190/yr if all 10, or start with 2–3. |
| **Tally** | Pro **$24/mo** (annual; page: months off Pro $24/mo), Business $74/mo | Free plans exist (no price shown — UNVERIFIED caps) | Great free form+builder for "Make an offer" / "Request access" forms inside a Carrd or site |
| **Typeform** | UNVERIFIED today (JS-walled); historically free tier + paid ~$25–40/mo | Free tier exists (UNVERIFIED response cap) | Prettier but pricier; no advantage at our scale |

**Read on F:** **Carrd Pro $19/yr + Tally free** = the full "for-sale page with offer form" stack for ~$1.60/mo per domain. Skip Typeform. Buy Carrd for the top 2–3 domains first (curebyketo, fusebot, weputt, paretobuddy are the expansion-ready four — see plan Rev 13), scale to 10 only when inquiries justify it.

---

## G. Marketplace backstop economics

| Marketplace | Listing cost | Commission / fee | Notes (verified 2026-09-07 where noted) |
|---|---|---|---|
| **Sedo** | Free to list (page structure; exact terms UNVERIFIED today) | Commission on sale — % UNVERIFIED today (historically ~9.5–15% tiered; minimum fee ~$50–75) | Established secondary market, payment plan offers (adds complexity) |
| **Afternic** | **Free to list** (homepage; terms UNVERIFIED) | Commission **UNVERIFIED** today (GoDaddy-owned; historically 15% standard, lower tiers for premium/network listings) | **dan.com now redirects to Afternic (observed 2026-09-07)** — Dan's standalone commission model is being folded into GoDaddy; re-check before listing |
| **Atom** | Free to list (marketplace side) | UNVERIFIED (page we pulled is their brand-contest service $299–$1,499, not marketplace commission) | Focus on brandables; smaller volume than Sedo/Afternic |
| **Dan.com** | Free to list (historically) | **Being sunset/merged into Afternic** (redirect observed today) — do not plan around Dan standalone | Historically 9–15% + payment processing; superseded |

**Read on G:** Use marketplaces as a **passive backstop** behind our active outreach — list the top priority domains free on Sedo + Afternic (both free-to-list), let Landers/parking capture organic demand, keep our agentic outreach as the primary channel. Verify the exact commission at listing time (both sites are JS-walled today — flagged UNVERIFIED). Commission drives a **minimum viable asking price**: at 15% commission + our 20% success fee, a $15K domain nets seller $10.2K — still fine at our price points, but don't list cheap.

---

## H. Close infrastructure — Escrow.com

**Verified 2026-09-07** from https://www.escrow.com/fee-calculator (Standard tier):

| Transaction amount | Standard fee | Minimum |
|---|---|---|
| $0 – $5,000 | 2.6% | $50.00 |
| $5,001 – $50,000 | 2.4% | $130.00 |
| $50,001 – $200,000 | 1.9% | $1,200.00 |
| $200,001 – $500,000 | 1.5% | $3,800.00 |
| $500,001 – $3,000,000 | 1.0% | $12,000.00 |
| $3M – $5M | 0.95% | $30,000.00 |
| $5M – $10M | 0.9% | $47,500.00 |

Plus: payment-processing fee on top of Standard/Concierge (+~3% card, per page snippet; wire options), and **+$25 for international buyers** (intermediary bank fee, added when buyer selects a foreign bank). Concierge ≈ 2× Standard (5.2%/4.8%…). Domain-holding service has a separate fee (FAQ-linked).

**Is it the right default?** For **our sizes ($3K–$45K)**: a $15K direct sale costs **$360 (2.4%)** — that's the *buyer- or split-* level; many marketplace sales bundle escrow into the commission instead. **Yes, Escrow.com is the right independent default** for owner-negotiated direct sales (no chargebacks against sellers, protects both sides, pay-per-transaction no monthly). For marketplace-listed sales, escrow comes included — don't double-pay. Tip: at $3K–$5K deals the 2.6%/$50-min is fine; for sub-$3K (puticlub.online bundles) it's borderline — prefer bundling those into the main domain or marketplace sale.

---

## I. Separate mailbox (Google Workspace 1 seat on turnkeysold.com)

**Verified 2026-09-07** from https://workspace.google.com/pricing.html:
- **Business Starter: $7/user/mo** (annual commitment; per-user/month pricing shown on page; monthly-billing price higher — UNVERIFIED exact number)
- Business Standard $14/user/mo (annual), Business Plus $22/user/mo (annual) — not needed.

**Worth it now or later?** **Later — specifically Phase 1 (first interested reply).** Today (send-freeze; ~3 sent emails) our current business inbox carries negligible reputation load. The moment we start sending from a *sequencing* platform or volume >~20 sends/mo, **$7/mo for an isolated turnkeysold.com sender mailbox becomes the single cheapest reputation insurance** (a paused inbox = dead team). It also makes replies land in a branded, monitored inbox. **Buy at Phase 1 trigger, not before** (avoids paying for an idle seat through the freeze). Note: warmup tools (Instantly/Smartlead built-ins) need *multiple* mailboxes to be effective — a single Workspace seat is the minimum viable sender.

---

## 2. RECOMMENDED PHASED STACK (explicit spend triggers)

### Phase 0 — NOW ($0–15/mo) — "No results yet, no money"
| Tool | Cost | Why |
|---|---|---|
| Manual sends from business inbox (+ owner LinkedIn DM / site forms) | $0 | Baseline — send-freeze compliant |
| Google Sheets CRM (one tab: `OUTREACH-TRACKER`) | $0 | System of record |
| **Hunter.io Free** (50 credits/mo) | $0 | Close the "no fireable email" gap one verified address at a time |
| **Apollo.io Free Starter** | $0 | Backup enrichment + company data |
| **MillionVerifier $39 pack** (≈10k verifications) | **$39 one-time** | Verify every address before any send — this is the fragile reputation's cheapest insurance |
| **Carrd Pro** × 2 (2 top priority domains, e.g. curebyketo.com + fusebot.ai) | $19 + $19 = **$38/yr** | For-sale landing + offer form (Tally free embedded) |
| Tally free | $0 | Offer forms / intake |
| **Phase 0 total: ≈ $77 one-time (≈ $1.6/mo amortized)** ✅ within $100 |

### Phase 1 — TRIGGER: first interested reply (~$50/mo cap)
Add, in order of value:
1. **Google Workspace 1 seat (turnkeysold.com) — $7/mo** — isolate sender reputation, branded sender.
2. **GMass Standard $20/mo (annual)** — mail-merge + tracking + replies-in-thread from Gmail; natural evolution of manual sends without moving to a cold platform. (Free tier first if the daily cap suffices.)
3. **Hunter Starter $34/mo (annual)** if enrichment need >50 finds/mo.
4. **Streak free** in-Gmail deal tracking if a negotiation actually opens.
(≈ $27–61/mo depending on which trigger lands first — stay under cap; don't stack all four at once.)

### Phase 2 — TRIGGER: proven reply-rate ≥5% across ≥30 sends (~$100/mo cap)
- **Smartlead Base $39/mo** (or **Instantly Growth $47/mo**) — real sequencing + warmup + multi-message cadences for the D3/D7/D14 follow-ups that today are paused/manual.
- Add 1–2 **buy-included warmup mailboxes** if needed (~$6–21/mo each depending on provider).
- **HubSpot Free CRM** or **Streak paid** ($49/user) only if a live pipeline demands it.
- Keep Apollo/Hunter free tiers; upgrade one only if credit-capped.

### "DO NOT BUY YET" list (good tools, wrong stage)
- ❌ **LinkedIn automation (Waalaxy / Expandi / LinkedHelper / La Growth Machine)** — ToS/account-restriction risk vs. our tiny volume; the owner's LinkedIn identity is our channel.
- ❌ **Premium Apollo / ContactOut bundles / Snov LinkedIn add-on** — enrichment at our volume is free-tier-able.
- ❌ **NeverBounce / ZeroBounce subscriptions** — MillionVerifier credit pack beats them on price for our volume.
- ❌ **Lemlist Multichannel / Reply.io / QuickMail / Woodpecker** — feature-rich sequencers we can't yet use; revisit at Phase 2 with only *one* pick.
- ❌ **Typeform paid** — Tally free does it.
- ❌ **Any warmup-as-a-service standalone** (Mailreach etc.) before we have a hot sender domain.

---

## 3. THE "$100 INITIAL ALLOCATION" — buy today, and why

> **"Spend $77 now: MillionVerifier $39 one-time (~10k verifications to protect the team's fragile sender reputation — the single cheapest insurance that the send-pause never triggers), Carrd Pro × 2 at $19/yr each for for-sale pages on the two expansion-ready domains (curebyketo.com, fusebot.ai) with Tally's free offer-forms embedded, and $0 for Hunter Free + Apollo Free to start closing every 'no fireable email' gap with verified, published addresses. Hold the remaining ~$23 of the $100 budget in reserve for the Phase 1 first purchase — the $7/mo Google Workspace seat on turnkeysold.com that isolates our sending reputation the moment the first interested reply makes real sends imminent. Do not buy a sequencer, LinkedIn automation, or any paid CRM until the reply-rate trigger is proven — every one of those is a volume bet on a message we haven't yet validated, and each costs more per month than this entire initial stack costs per year."**

---

## Verification log (all checked 2026-09-07)
- **Verified live (page text/JSON):** Instantly, Smartlead, Lemlist, Woodpecker (slider + add-ons), Saleshandy, QuickMail, GMass, Brevo, Apollo (FAQ), Hunter, Snov, Anymail, Kaspr, MillionVerifier (browser), ZeroBounce, DeBounce (partial), Expandi, LinkedHelper, La Growth Machine, Airtable, Notion, Streak, Carrd (homepage), Tally, Atom, Escrow.com fee-calculator, Google Workspace pricing, dan.com→Afternic redirect.
- **Blocked/JS-walled today (flagged UNVERIFIED):** Reply.io (403), NeverBounce (403), Prospeo, ContactOut (partial), Typeform, HubSpot, Sedo commission exacts, Afternic commission exacts, Waalaxy € prices, YAMM paid tiers.
- **Known annual-vs-monthly traps flagged:** Saleshandy (~25% cheaper annual), GMass (~31%), Anymail (~33%, "yearly to save 33%"), Hunter ($34 vs $49), Snov (~25%), Instantly bundles (annual-billed), Notion ($10 vs $12, custom-domain Sites $8 annual / $10 monthly), Tally ($24 vs presumably ~$29), Carrd ($19/yr vs $0 subdomain free).