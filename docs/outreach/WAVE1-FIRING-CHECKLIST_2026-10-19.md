# Wave-1 Firing Checklist — PayAuto ×7 + PayQuick ×6 (13 first-touch messages)
**Date:** 2026-10-19 · **Compiled by:** lead (architect's loop hit platform errors after the compliance pass; checklist completed by lead from the packs' route data per established lead-completion pattern) · **Status:** ⏸️ **NOTHING FIRES until the owner's explicit per-send instruction (freeze directive 2026-09-04).**
**Packs:** `DOMAINS/payauto.ai/02-outreach/PAYAUTO-WAVE1-FIRST-TOUCH_2026-09-21.md` (A1–A7) · `DOMAINS/payquick.ai/02-outreach/PAYQUICK-WAVE1-FIRST-TOUCH_2026-09-21.md` (B1–B6) — compliance pass merged as PR #84 (main `53a0fd9`).

## 0. Gate
The SEND FREEZE is absolute. Every send requires the owner's explicit per-send instruction for THAT target. A general "go ahead" is NOT sufficient. Log each instruction (date, target, channel) in §4's log before sending.

## 1. One-time pre-flight (before the first send only)
- [ ] Owner confirms **sender identity** — packs assume "Juan L. Aguirre — TurnKeySold Domains" — and the **from-address** (pending owner confirmation).
- [ ] Owner confirms sending infrastructure (platform inbox vs. tooling stack per `docs/OUTREACH-TOOLING-PLAYBOOK_2026-09-20.md`).
- [ ] Confirm zero bounces so far on the team's sending reputation (3 lifetime sends, 0 replies as of 2026-09-03; any bounce = STOP and re-evaluate).

## 2. Per-message checklist (repeat for EVERY send)
1. [ ] Owner's per-send instruction for this exact target — logged in §4.
2. [ ] **Fireable-status recheck** against §3 below (any status downgrade since the pack date = STOP, re-verify).
3. [ ] **Route recheck** — the route's URL/page still live and the form accessible (Tensec's site is bot-walled; Fragment is parked — B6 is DO-NOT-SEND until re-verified).
4. [ ] **Copy checks:** no pricing tokens · no links · no "I own" framing · body <100 words · explicit no-pressure close present · greeting matches verification status (VERIFIED = personalized; NOT-VERIFIED = company-level).
5. [ ] Send.
6. [ ] Append the log line in §4 (target, date, route, message ID).

## 3. Target status table (as of compliance pass, PR #84; A3 row updated 2026-10-20 after PR #87 — Luce VERIFIED)
| ID | Target | Contact status | Route | Flags |
|---|---|---|---|---|
| A1 | Natural — Kahlil Lalji (CEO) | ✅ VERIFIED | LinkedIn (Lalji) / natural.com contact form | no published email — never infer one |
| A2 | Payman AI — Tyllen Bicakcic (Co-Founder & CEO) | ✅ VERIFIED | hello@paymanai.com (published general/press route) / LinkedIn | parallel target Teymour Farman-Farmaian (multi-thread allowed — same body, swap greeting) |
| A3 | Basis Theory — Colin Luce (Co-Founder & CEO) | ✅ VERIFIED (PRN, fetched 2026-10-19) | LinkedIn (Luce) / basistheory.com contact route | greeting personalized to Luce |
| A4 | Catena Labs — Sean Neville (Co-Founder & CEO) | ✅ VERIFIED | LinkedIn (Neville) / catena.com contact | no public email |
| A5 | Crossmint — Rodri Fernandez Touza (Co-Founder) | ✅ VERIFIED (secondary Rawitz ⚠️ NOT verified) | LinkedIn (Touza) / crossmint.com contact | Rawitz only after verification |
| A6 | Paid — Manny Medina (Co-Founder & CEO) | ✅ VERIFIED | LinkedIn (Medina) / paid.ai contact | no public email |
| A7 | Skyfire — Amir Sarhangi (CEO & Founder) | ✅ VERIFIED | LinkedIn (Sarhangi) / skyfire.xyz contact | funding CORRECTED to $8.5M seed — copy already aligned |
| B1 | Causa Prima — Maex Ament (Co-Founder & CEO) | ✅ VERIFIED | site form + LinkedIn (Ament) | Gebbing/Stanislaus verified parallel co-founders (multi-thread allowed) |
| B2 | GrailPay — Will Messina (Co-Founder & CEO) | ✅ VERIFIED | site form / LinkedIn (Messina) | **william@grailpay.com NOT-FIREABLE** (removed from all routes); Jones/Bykov NOT-VERIFIED — do not name |
| B3 | SolvaPay — company-level | ⚠️ founders NOT verified | **contact@solvapay.com FIREABLE** (site footer — preferred) / site form | LinkedIn only after founder verification |
| B4 | Tensec — company-level | ⚠️ founders NOT verified | site form (bot-walled — verify accessibility before send) / LinkedIn company page | no published email |
| B5 | PayQuicker — corporate route | corporate (no named exec) | corporate contact form / brand or corp-dev channel | defensive-acquisition angle; strategic long cycle |
| B6 | Fragment — company-level | ⚠️ NOT verified | **DO NOT SEND until re-verified** — site parked-for-sale | route undetermined until company status confirmed |

## 4. Per-send log (append one line per owner instruction + send)
`DATE | TARGET | MESSAGE-ID | ROUTE | OWNER-INSTRUCTION (verbatim/date) | RESULT (sent / deferred / blocked + why)`

## 5. Standing caveats
- Multi-threading is ALLOWED (owner rule 2026-09-21): same-company contacts are parallel targets — same body, swapped greeting, each with its own per-send instruction.
- No pricing in any copy; internal anchors live in the briefs/master CSV only.
- Never-invent: every claim traceable; only literally-published contacts fireable (index §9.7 flag vocabulary).
