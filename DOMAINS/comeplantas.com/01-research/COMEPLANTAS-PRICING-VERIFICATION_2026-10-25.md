# ComePlantas.com — Pricing & Comps Verification (2026-10-25)

**Scope:** verification pass on `COMEPLANTAS-PRICING-EXTERNAL-RESEARCH_2026-10-25.md` (owner-supplied; full-field ingested verbatim + price-bands CSV). **Every figure below is a verdict, never an estimate.** No ask/BIN/floor is set or endorsed here — the owner rules after verified comps.

## 1. Aftermarket stats (DomainDetails) — ❌ NOT-VERIFIED (blocked)
Source claims: median ~$2,500 · average ~$16,233 · 55% $1K–$3K / 25% $3K–$10K / 15% $10K–$100K (DomainDetails valuation guide, 2025).
**Attempted 2026-10-25:** `curl` on domaindetails.com market-report + homepage → **HTTP 403 bot-wall** (5.5KB challenge page). No literal stat located → per never-invent, **carried as EXTERNAL-UNVERIFIED, do-not-cite**. Retry via agent-browser queued.

## 2. "$1,500–$3,000 band for a short two-word .com" — ◐ UNVERIFIED (carried)
Claim attributes generic value of ComePlantas.com (11 chars, no hyphen) to a $1,500–$3,000 band. No independent source fetched this session (same bot-wall applies to market sources). Band is the source's reasoning, recorded as source-proposal only.

## 3. NameBio comps (vegan / plantbased / comer, last 2 years, $1,000+) — ❌ BLOCKED (retried 2026-10-25, task 78f094f9)
**Attempted 2026-10-25 (PR #97 wave):** `https://namebio.com/?s=vegan` (+ plantbased, comer) via curl → **HTTP 403 bot-wall, 0 rows retrieved.**
**Retry 2026-10-25 (task 78f094f9) via agent-browser (play that beat EUIPO's wall):** NameBio is behind a **hard Cloudflare WAF ban, not a challenge** — agent-browser rendered the block page (`Attention Required! | Cloudflare` → "Sorry, you have been blocked", IP-level, no interactive checkbox) for both `https://namebio.com/?s=vegan` and the bare homepage `https://namebio.com/`, including after a 45s pause and a full browser restart. **No bypass attempted (evading a WAF block is not appropriate) — retry avenues from this network are exhausted.**
**Verdict: no comps asserted (never-invent).** The `vegan / plantbased / comer · 2y · $1,000+` NameBio query remains **queued for alternate access — flagged as an OWNER-side item**: NameBio requires a different egress IP (e.g. a residential session) or a paid NameBio API key; the agent's network is WAF-banned. §4 source proposal stands unaudited until comps land.

## 4. Source's setup (recorded as the SOURCE's proposal only — no endorsement)
BIN **$25,000** · private floor **~$7,500** · direct-outreach anchor **$30,000** (settle $10K–$20K for NotCo/Heura-tier; broker route for CPG/brand-house leads). Same source: "don't take the first flipper offer", "list by early December so the January Veganuary spike hits your lander". **Owner rules the ladder after the queued comps.**

## 5. Timing note (recorded)
**"List by early December so the January Veganuary spike hits the lander"** — feeds the Afternic/Sedo November setup queue (MuyGuay exit-plan pattern). Not an action taken; noted for the owner's listing decision.

## 6. Cross-reference
Buyer-type labels map to the buyer-landscape file's tiers (source header). The 6 bands also cross-walk the 5-row `COMEPLANTAS-BUYER-TYPES_2026-10-20.csv` (EXTERNAL-UNVERIFIED). EUIPO gate still CLEAR (PR #95); OEPM owner-side.

**Rules honored:** never-invent (blocked ≠ estimated; nothing cited without a fetched source) · no pricing endorsement · SEND FREEZE untouched.
