# PayAuto.ai — External Acquisition-Target Research (Integration Note)
**Source:** external collaborator LLM (owner-initiated dialog, content received 2026-09-21)
**Provenance status:** ⚠️ EXTERNAL — data produced by another LLM system; NOT yet verified by our team. The collaborator claims contacts/funding were verified from live search in its own session, but we hold only the summary + 5 named contacts it emitted. All rows below carry that provenance until our verification pass completes.
**Date anomaly flagged:** the collaborator self-dates its funding verification "October 2026" — later than today (2026-09-21). Treat dates as approximate; verify against primary sources.

## What this file is
`payauto_ai_acquisition_targets.csv` (same directory) — reconstructed by agent-lead from the collaborator's delivered research summary. 19 companies × 13 columns, matching the collaborator's stated CSV spec (Priority, Tier, Funding, HQ, Website, Contact name/title/LinkedIn, Company LinkedIn, Description, Strategic fit, Notes). Contact fields are filled ONLY where the collaborator's dialog explicitly named a contact (5 named + 1 partial). Where the collaborator claimed "every contact verified" but did not emit the name in the handoff, the field says `TO SOURCE` — we do not invent.

## What is NEW vs our Aug-12 research (leads_payauto.ai.md)
1. **The 2026 Series-A startup wave (8 pure-play agentic-payments companies)** — absent from our list: Natural ($30M Series A), Basis Theory ($33M B), Catena Labs ($30M A, Circle co-founder), Crossmint ($23.6M), Paid ($21.6M seed, Manny Medina), Skyfire ($9.5M), Nekuda ($5M, Visa/Amex-backed). Our list had the macro layer + earlier startups only.
2. **Named, title-verified contacts with LinkedIn** for the top of the wave (Natural CEO Kahlil Lalji, Basis Theory CEO Colin Luce, Catena CEO Sean Neville, Paid CEO Manny Medina) — our rows had none for these.
3. **Funding figures + investor names** per company (our research had none for these orgs).
4. **Market-timing triggers:** agentic commerce $135B (2025) → $1.7T (2030, Rye); Visa "millions of agent purchases by holiday 2026"; 630 agentic M&A deals; AI-fintech deal share 5%→9%. Useful for outreach timing; third-party stats, not buyer evidence.
5. **Urgency ranking + negotiation logic** (name-collision = defensive-buy leverage: Natural, Payman).

## What we ALREADY had (no new information)
- Tier-3 macro buyers: Stripe (our DMPS 96), Visa (94), Mastercard (93), PayPal (88), + Ramp/Brex/Coinbase adjacency. The collaborator's Tier 3 overlaps our Tier-1 rows.
- Payman AI was already our DMPS 92 row.

## Payman dual-contact (owner directive 2026-09-21: multi-contact = opportunity, not conflict)
- **Payman AI has two recorded leaders:** our Aug-12 row says **Teymour Farman-Farmaian (Founder/CEO)**; the collaborator's original says **Tyllen Bicakcic (Co-Founder & CEO)**. Per owner directive, this is NOT a conflict to resolve by picking one — it is **multi-threading**: verify each person's current role independently (published sources), then treat BOTH as parallel outreach targets if both check out; correct any stale record to current reality.
- Same principle applies to every Tier-1 company where our records + the original CSV together surface more than one contact.

## Collaborator's own honesty flags (carried into the CSV)
- No email addresses included anywhere (aligned with our never-invent rule) — LinkedIn/site-form routes only.
- Nekuda: Ayal Karmi name/title verified, personal LinkedIn NOT surfaced → manual search, not guessed.
- Payman + HappyRobot HQ city-level = unverified.
- Tier 3 rows list partnership/BD routing instead of named execs (intentional).

## Verification plan (delegated to domain-researcher)
Tier-1 pass: verify the 8 pure-play companies' existence, funding claims, contact names/titles/LinkedIn; resolve the Payman CEO conflict. Result updates flags to our VERIFIED standard; unresolved rows keep EXTERNAL-UNVERIFIED.

## UPDATE (post-integration): original handoff recovered
The collaborator's ORIGINAL CSV was found at repo root (`payauto_ai_acquisition_targets.csv`, committed in PR #62 alongside this reconstruction). It is **authoritative for contact data**: all 19 rows carry the collaborator's verified Contact Name/Title/LinkedIn/Company-Website/Contact-Information fields — including the contacts this reconstruction marked TO SOURCE (Crossmint, Skyfire, Arcade.dev, HappyRobot, Rye, ReFiBuy). It also lists Payman's CEO as **Tyllen Bicakcic (Co-Founder & CEO)** — confirming the handoff position but NOT resolving the conflict with our Aug-12 row (Teymour Farman-Farmaian, Founder/CEO); both may be co-founders — verification still required before any outreach.
**File roles:** root CSV = collaborator's original handoff (reference copy, EXTERNAL provenance); DOMAINS reconstruction = our verification workbench (provenance/conflict annotations; update flags here as verification completes).
