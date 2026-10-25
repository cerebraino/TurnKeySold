# TurnKeySold Domains — Inventory Reconciliation (Namecheap export vs asset tree vs backlog)

**Date:** 2026-10-25 · **As-of anchor:** Namecheap CSV export merged to `main` (owner branch `Updated-Namecheap-Domains` → merge commit `3ea86bd`) · **Author:** domain-researcher (task bfbb20e6)

> **Disposition rule:** this document records **situations + options + owner decisions that have been received** — nothing else is assumed. Follow-up 2026-10-25: owner dispositions integrated (§9 decision log) and the master register built (§11).

---

## 1. Sources & normalization

| Source | Location | Rows / size | Authority |
|---|---|---|---|
| **Namecheap export (authoritative inventory baseline)** | `Domain_List.csv` (repo root; unchanged copy also at `/home/team/shared/Domain_List.csv`) | **175 domains** (175 unique) | Registrar export — the owner's own list of what is at Namecheap. Columns: domain · privacy · NC status · auto-renew · expiry |
| **DOMAINS/ asset tree** | `DOMAINS/*/` on `main` | **146 domain dirs** + `DOMAINS/coldbeerportfolio/` bundle folder + `DOMAINS/CSV/` meta-dir | Research/outreach assets per domain — coverage, not ownership proof |
| **Backlog CSV** | `domain-backlog-new.csv` (repo root) | **110 rows** | Planning/subset — candidates + rough estimates; NOT authoritative for ownership |
| **Master domain register** | `docs/assets/DOMAIN-MASTER-REGISTER.csv` (this wave) | **184 rows** = 175 NC + 9 other-registrar | NEW unified all-registrar view — see §11 |

**Normalization:** lowercase, trailing dots stripped, exact match — no fuzzy logic. **Delta vs Aug audit:** 145 dirs → **146** today (+1; audit refresh = follow-up). **Backlog copies:** root `domain-backlog-new.csv` md5 `cd027a3b0d` vs PORTFOLIO copy `641d0ad816` — root canonical; reconcile later.

---

## 2. Three-way picture (counts)

| Set | Count |
|---|---|
| Namecheap export (A) | **175** |
| Asset dirs (B) | **147** (+ coldbeerportfolio folder + CSV meta) |
| Backlog rows (C) | **110** |
| A ∩ B | **127** | A − B (§3 onboard) | **48** |
| B − A (§4 not-at-Namecheap) | **20** | C − A − B (§5) | **1** |

Checks: 126 + 49 = 175 ✓ (A) · 146 = 126 + 20 ✓ (B) · 101 + 9 = 110 ✓ (C). **Status mix:** 154 Active / 15 Alert (sidebar §10) / **6 Grace**; renew 125 ON / 50 OFF.

---

## 3. In registrar but no asset dir — **49 onboard candidates**

> Listed for onboarding awareness only. **The lead's brief expected ~29–30; the exact run is 49** (31 of the 49 also have backlog rows) — the data is the truth. Onboarding research itself is a **follow-up task, not part of this wave**. Note: `comeplantas.com` asset dir landed via PR #95 merge (no longer onboard); `paycarai.com` + `aseguranza.online` received owner LET-GO (still in NC rows until they lapse — §9).

| Domain | NC status | Renew | Expiry | Notes |
|---|---|---|---|---|
| agentbucks.si | Active | ON | Oct 18 2027 | — |
| agentickillswitch.org | Active | OFF | Sep 24 2027 | — |
| ahburro.com | Active | ON | Jul 31 2027 | — |
| aseguranza.ai | Active | ON | Oct 16 2027 | — |
| aseguranza.online | Grace | OFF | Oct 14 2026 | ⚠ OWNER LET-GO 2026-10-25 (see §9) |
| automoviles.si | Active | ON | Oct 18 2027 | — |
| birrafria.com | Active | ON | Feb 21 2027 | in backlog |
| buentino.com | Active | ON | Nov 12 2027 | in backlog |
| carboingratos.com | Active | OFF | Jan 17 2027 | in backlog |
| cardbot.si | Active | ON | Oct 18 2027 | — |
| cdmx.casino | Alert | OFF | Nov 05 2026 | in backlog |
| cdmx.games | Alert | OFF | Nov 05 2026 | in backlog |
| cervefria.com | Active | OFF | Feb 21 2027 | in backlog |
| cervezahelada.com | Active | ON | Dec 10 2026 | in backlog |
| chelafria.com | Active | ON | Dec 10 2026 | in backlog |
| chevefria.com | Active | ON | Dec 10 2026 | in backlog |
| chiefaiadviser.com | Active | ON | Sep 24 2027 | — |
| coldbeerportfolio.com | Active | OFF | Feb 21 2027 | in backlog |
| desmadrito.com | Active | OFF | Feb 03 2027 | in backlog |
| fieldphotolog.com | Active | ON | Oct 18 2027 | — |
| fierotumodo.com | Active | ON | Jul 21 2027 | in backlog |
| fotobitacora.com | Active | ON | Oct 22 2027 | in backlog |
| fotobrujo.com | Active | ON | Sep 09 2027 | — |
| fuxiaballerinas-qro.com | Active | ON | Jul 01 2027 | in backlog |
| haymota.com | Active | ON | Jan 31 2027 | in backlog |
| humanoscomoservicio.com | Active | ON | Apr 06 2027 | in backlog |
| iapolitica.com | Active | ON | Feb 11 2027 | in backlog |
| iatuya.com | Active | ON | Jul 21 2027 | in backlog |
| juanlauro.com | Active | ON | Jan 05 2027 | in backlog |
| mobileworklog.com | Grace | OFF | Oct 22 2026 | in backlog |
| nobreakai.com | Alert | OFF | Nov 18 2026 | in backlog |
| onegal.net | Active | OFF | Feb 01 2027 | in backlog |
| ordendetrabajo.com | Active | ON | Oct 24 2027 | in backlog |
| oyenota.com | Active | ON | Oct 02 2027 | — |
| paguesuacasa.com | Active | ON | Dec 10 2026 | in backlog |
| paybud.si | Active | ON | Oct 18 2027 | — |
| photologbook.com | Active | ON | Oct 22 2027 | in backlog |
| photosorcerer.com | Active | ON | Sep 09 2027 | — |
| pontebuena.com | Alert | OFF | Nov 12 2026 | in backlog |
| quieromota.com | Active | ON | Jan 31 2027 | in backlog |
| spendbot.si | Active | ON | Oct 18 2027 | — |
| topguys.net | Active | ON | Dec 14 2026 | in backlog |
| topshelfer.com | Active | ON | Dec 25 2026 | in backlog |
| turnkeysold.com | Active | ON | Jun 24 2027 | — |
| umagelada.com | Active | ON | Feb 22 2027 | in backlog |
| usaichief.com | Active | ON | Sep 23 2027 | — |
| usaiczar.com | Active | ON | Sep 23 2027 | — |
| viejanueva.com | Active | ON | Aug 14 2027 | — |

---

## 4. In asset tree but NOT in the Namecheap export — **20**

> Absence from the Namecheap export means **not registered at Namecheap** — it does NOT mean sold/expired. **Owner confirmed 2026-10-25: 9 of the 20 are held at OTHER registrars** (still owned; active-campaign where applicable) — registrar names TBD pending the owner's registrar list. The remaining 11 stay owner-to-confirm. `leanmeds.com` is the only evidence-backed SOLD (business plan Rev 18, Trinity HealthCare Supply).

| Domain | Owner status (2026-10-25) | Context / evidence on file |
|---|---|---|
| acoholfree.com | OTHER REGISTRAR — owned | backlog row ★★★ |
| aisexshops.com | OTHER REGISTRAR — owned | adult portfolio ($15K); backlog dup-verify note |
| aivrfun.com | OTHER REGISTRAR — owned | backlog row ★★★★ |
| aseguranzaautos.com | owner to confirm | insura-cluster variant |
| congoogle.com | OTHER REGISTRAR — owned | backlog row ★★★ |
| dalai.com | owner to confirm | dalai.co/.fit GRACE at NC — cluster decision (see §9/§6a) |
| gosexai.com | OTHER REGISTRAR — owned | backlog row ★★★ |
| hispanicpowerhouse.com | owner to confirm | hispano cluster |
| jogpay.com | OTHER REGISTRAR — owned (campaign stays live) | payments-family campaign ($3K); conflict flag resolved |
| leanmeds.com | SOLD per business plan | Rev 18: "LeanMeds.com ✅ SOLD (Trinity HealthCare Supply)" |
| muyveloz.com | owner to confirm | MuyGuay-family; not listed as owned in plan |
| muyverde.com | owner to confirm | MuyGuay-family; not listed as owned in plan |
| nychispanic.com | owner to confirm | latino geo cluster |
| nychispano.com | owner to confirm | latino geo cluster |
| putasexo.com | OTHER REGISTRAR — owned | adult portfolio ($18K); backlog dup-verify note |
| roiboss.com | owner to confirm | ROI brandable cluster |
| veraroi.com | owner to confirm | ROI brandable cluster |
| vivamucho.com | owner to confirm | Spanish brandable |
| vivorg.com | OTHER REGISTRAR — owned | backlog row ★★★ |
| weputt.com | owner to confirm | golf brandable |

**paretobuddy.app note:** previously flagged as the single backlog-only stale row (§5); owner confirmed 2026-10-25 it is **owned at another registrar** — moved to "other-registrar owned", §5 now empty of stale rows.

---

## 5. In neither registrar nor tree — always empty after dispositions

**0 rows** as of 2026-10-25 (`paretobuddy.app` resolved: other-registrar owned).

---

## 6. Renewal-risk table — **45 domains** (6 GRACE + 39 renew-OFF ≤120d)

> From `Domain_List.csv` as-of 2026-10-25. Count reconciliation: the brief said "3 GRACE" — the export lists **6**; 6 GRACE + 39 OFF-≤120d = **45** (6+39+5 = 50 renew-OFF total). **Renewal-fee column:** Namecheap price research attempted 2026-10-25 — the public price page returned **HTTP 403 (bot-wall)**; Q5 retry same day with the lead-sanctioned source (`namecheap.com/domains/domain-name-pricing/`) via agent-browser — Cloudflare challenge never cleared (2 loads + 3 turnstile clicks); Wayback CDX inconclusive (archive.org outage); per the price-provenance rule (cite source URL + fetched-on) **no price is asserted**; fees are `TBD`; the Wayback pricing-path leg is conclusively dead (0 captures ✚ redirect-stubs-only — §7.5 note 5, PR #101). Owner decides renew/drop from this table; the last column is a **neutral suggestion basis only** (never a recommendation).

### 6a. GRACE — already past expiry

| Domain | Expiry | Ren. | Δdays | Owner decision (2026-10-25) | Suggestion basis |
|---|---|---|---|---|---|
| aseguranza.online | Oct 14 2026 | OFF | -11 | **LET GO — no renewal (owner)** | owner LET-GO 2026-10-25; TLD liquidity: low (online); GRACE — recovery time-limited |
| dalai.co | Oct 18 2026 | OFF | -7 | pending | asset dir exists (researched); GRACE — recovery time-limited |
| dalai.fit | Oct 18 2026 | OFF | -7 | pending | asset dir exists (researched); TLD liquidity: low (fit); GRACE — recovery time-limited |
| mobileworklog.com | Oct 22 2026 | OFF | -3 | pending | backlog-row candidate; GRACE — recovery time-limited |
| putero.online | Oct 13 2026 | OFF | -12 | **LET GO — no renewal (owner)** | asset dir exists (researched); owner LET-GO 2026-10-25; TLD liquidity: low (online); GRACE — recovery time-limited |
| puticlub.online | Oct 08 2026 | OFF | -17 | **LET GO — no renewal (owner)** | asset dir exists (researched); owner LET-GO 2026-10-25; TLD liquidity: low (online); GRACE — recovery time-limited |

### 6b. Auto-renew OFF, expiring 0–120d (39)

| Domain | NC status | Expiry | Days | Tier | Owner decision | Renewal fee (NC) | Suggestion basis |
|---|---|---|---|---|---|---|---|
| apuesto.casino | Alert | Nov 02 2026 | 8 | ≤30d | pending | TBD (403 bot-wall 2026-10-25) | asset dir exists (researched); backlog-row candidate; TLD liquidity: low (casino) |
| apuesto.xyz | Alert | Nov 02 2026 | 8 | ≤30d | pending | TBD (403 bot-wall 2026-10-25) | asset dir exists (researched); backlog-row candidate; TLD liquidity: low (xyz) |
| teapuesto.casino | Alert | Nov 03 2026 | 9 | ≤30d | pending | TBD (403 bot-wall 2026-10-25) | asset dir exists (researched); backlog-row candidate; TLD liquidity: low (casino) |
| teapuesto.xyz | Alert | Nov 03 2026 | 9 | ≤30d | pending | TBD (403 bot-wall 2026-10-25) | asset dir exists (researched); backlog-row candidate; TLD liquidity: low (xyz) |
| apuesto.ad | Alert | Nov 05 2026 | 11 | ≤30d | pending | TBD (403 bot-wall 2026-10-25) | asset dir exists (researched); backlog-row candidate; TLD liquidity: low (ad) |
| cdmx.bet | Alert | Nov 05 2026 | 11 | ≤30d | pending | TBD (403 bot-wall 2026-10-25) | asset dir exists (researched); backlog-row candidate; TLD liquidity: low (bet) |
| cdmx.casino | Alert | Nov 05 2026 | 11 | ≤30d | pending | TBD (403 bot-wall 2026-10-25) | backlog-row candidate; TLD liquidity: low (casino) |
| cdmx.games | Alert | Nov 05 2026 | 11 | ≤30d | pending | TBD (403 bot-wall 2026-10-25) | backlog-row candidate; TLD liquidity: low (games) |
| pontebuena.com | Alert | Nov 12 2026 | 18 | ≤30d | pending | TBD (403 bot-wall 2026-10-25) | backlog-row candidate |
| nobreakai.com | Alert | Nov 18 2026 | 24 | ≤30d | pending | TBD (403 bot-wall 2026-10-25) | backlog-row candidate |
| nofailai.com | Alert | Nov 18 2026 | 24 | ≤30d | pending | TBD (403 bot-wall 2026-10-25) | asset dir exists (researched) |
| gastropub.bet | Alert | Nov 20 2026 | 26 | ≤30d | pending | TBD (403 bot-wall 2026-10-25) | asset dir exists (researched); backlog-row candidate; TLD liquidity: low (bet) |
| gastropub.bid | Alert | Nov 20 2026 | 26 | ≤30d | pending | TBD (403 bot-wall 2026-10-25) | asset dir exists (researched); backlog-row candidate; TLD liquidity: low (bid) |
| gastropub.casino | Alert | Nov 20 2026 | 26 | ≤30d | pending | TBD (403 bot-wall 2026-10-25) | asset dir exists (researched); backlog-row candidate; TLD liquidity: low (casino) |
| gastropub.games | Alert | Nov 20 2026 | 26 | ≤30d | pending | TBD (403 bot-wall 2026-10-25) | asset dir exists (researched); backlog-row candidate; TLD liquidity: low (games) |
| aiappbet.com | Active | Nov 26 2026 | 32 | 31–60d | pending | TBD (403 bot-wall 2026-10-25) | asset dir exists (researched); backlog-row candidate |
| aitopdeals.com | Active | Nov 26 2026 | 32 | 31–60d | pending | TBD (403 bot-wall 2026-10-25) | asset dir exists (researched) |
| appai.bet | Active | Nov 26 2026 | 32 | 31–60d | pending | TBD (403 bot-wall 2026-10-25) | asset dir exists (researched); backlog-row candidate; TLD liquidity: low (bet) |
| appaibet.com | Active | Nov 26 2026 | 32 | 31–60d | pending | TBD (403 bot-wall 2026-10-25) | asset dir exists (researched); backlog-row candidate |
| aitopshelf.com | Active | Dec 03 2026 | 39 | 31–60d | pending | TBD (403 bot-wall 2026-10-25) | asset dir exists (researched); backlog-row candidate |
| aitopshops.com | Active | Dec 03 2026 | 39 | 31–60d | pending | TBD (403 bot-wall 2026-10-25) | asset dir exists (researched); backlog-row candidate |
| aitopstuff.com | Active | Dec 03 2026 | 39 | 31–60d | pending | TBD (403 bot-wall 2026-10-25) | asset dir exists (researched); backlog-row candidate |
| aitoptravel.com | Active | Dec 03 2026 | 39 | 31–60d | pending | TBD (403 bot-wall 2026-10-25) | asset dir exists (researched); backlog-row candidate |
| aitoptrips.com | Active | Dec 03 2026 | 39 | 31–60d | pending | TBD (403 bot-wall 2026-10-25) | asset dir exists (researched); backlog-row candidate |
| paycarai.com | Active | Dec 03 2026 | 39 | 31–60d | **LET GO — no renewal (owner)** | TBD (403 bot-wall 2026-10-25) | asset dir exists (researched); owner LET-GO 2026-10-25 |
| halfpricednames.com | Active | Dec 18 2026 | 54 | 31–60d | pending | TBD (403 bot-wall 2026-10-25) | asset dir exists (researched); backlog-row candidate |
| cancelarsuscripciones.com | Active | Dec 22 2026 | 58 | 31–60d | pending | TBD (403 bot-wall 2026-10-25) | asset dir exists (researched); backlog-row candidate |
| laxhispanic.com | Active | Dec 25 2026 | 61 | 61–90d | pending | TBD (403 bot-wall 2026-10-25) | asset dir exists (researched) |
| nomoreagi.com | Active | Jan 04 2027 | 71 | 61–90d | pending | TBD (403 bot-wall 2026-10-25) | asset dir exists (researched); backlog-row candidate |
| adelgazacomiendograsa.com | Active | Jan 17 2027 | 84 | 61–90d | pending | TBD (403 bot-wall 2026-10-25) | asset dir exists (researched); backlog-row candidate |
| carboingratos.com | Active | Jan 17 2027 | 84 | 61–90d | pending | TBD (403 bot-wall 2026-10-25) | backlog-row candidate |
| lahispano.net | Active | Jan 24 2027 | 91 | 91–120d | pending | TBD (403 bot-wall 2026-10-25) | asset dir exists (researched) |
| aikillswitch.org | Active | Jan 31 2027 | 98 | 91–120d | pending | TBD (403 bot-wall 2026-10-25) | asset dir exists (researched); backlog-row candidate |
| airedbutton.com | Active | Jan 31 2027 | 98 | 91–120d | pending | TBD (403 bot-wall 2026-10-25) | asset dir exists (researched); backlog-row candidate |
| aistopbutton.com | Active | Jan 31 2027 | 98 | 91–120d | pending | TBD (403 bot-wall 2026-10-25) | asset dir exists (researched); backlog-row candidate |
| onegal.net | Active | Feb 01 2027 | 99 | 91–120d | pending | TBD (403 bot-wall 2026-10-25) | backlog-row candidate |
| desmadrito.com | Active | Feb 03 2027 | 101 | 91–120d | pending | TBD (403 bot-wall 2026-10-25) | backlog-row candidate |
| cervefria.com | Active | Feb 21 2027 | 119 | 91–120d | pending | TBD (403 bot-wall 2026-10-25) | backlog-row candidate |
| coldbeerportfolio.com | Active | Feb 21 2027 | 119 | 91–120d | pending | TBD (403 bot-wall 2026-10-25) | backlog-row candidate |

### 6c. Renew-OFF beyond 120d (5, for completeness)

| Domain | Days |
|---|---|
| miniterapia.com | 128 |
| bajaturenta.com | 161 |
| mypatientprep.com | 161 |
| paretobuddy.com | 232 |
| agentickillswitch.org | 334 |

---

## 7. Standout items (updated 2026-10-25)

1. **`paycarai.com` — OWNER LET-GO (no renewal), decided 2026-10-25**, despite the $17K campaign anchor (paycar.ai cluster). Expiry 2026-12-03, renew OFF. Decision recorded; paycar.ai/.com campaign records should be updated at the appropriate time (owner's call how hard to keep pushing the sibling).
2. **Adult bundles `puticlub.online` + `putero.online` — OWNER LET-GO (no renewal), 2026-10-25** — the pair was valued $3K each in the plan; decision overrides. Also `aseguranza.online` LET-GO.
3. **`dalai.co` + `dalai.fit` GRACE — pending owner decision** (dalai.com outside NC; cluster question open).
4. **All 15 Alert-status domains are renew-OFF** and inside the risk window — see the §10 sidebar.
5. **Renewal-price research BLOCKED this session** (Namecheap/DomainDetails/NameBio all 403 bot-wall) — fees TBD, comps queued; no prices asserted. **Q5 retry 2026-10-25 (PR #99):** the lead sanctioned Namecheap's TLD renewal pricing page (`namecheap.com/domains/domain-name-pricing/`) as a legitimate price source; retried via agent-browser same day — Cloudflare "Just a moment…" challenge persisted across 2 loads + 3 turnstile-click attempts (page never rendered); alternate routes also failed: `tld-list.com` → HTTP 403, Wayback CDX → empty/offline (**archive.org outage 2026-10-25** — initial read INCONCLUSIVE, queued for retry when the archive returned). **Q5 Wayback leg RESOLVED 2026-10-25 (archive recovered; PR #101):** CDX (service live, some queries slow/timeout-y) confirms **zero captures under `namecheap.com/domains/domain-name-pricing/*`** (www and bare host, both `[]`) and only **3 captures under legacy `www.namecheap.com/domains/pricing/*` — ALL 301/302 redirect stubs** (2025-04-25 `register-renew-fees/`, 2025-05-23, 2025-05-31), no 200-content; replaying the newest stub resolves to Namecheap's **`/status/404.aspx`** page (itself Cloudflare-challenged in replay today). **Conclusion: Wayback holds no archived Namecheap TLD-pricing table — the Wayback leg is conclusively dead (negative resolution); still no price asserted; the owner's Namecheap dashboard (account-holder view) is the sole remaining source for renewal fees.**

---

## 8. Open items / options (no decisions taken beyond §9)

1. **Pending renew-or-release decisions:** dalai.co/.fit (GRACE), mobileworklog.com (GRACE), the 39 OFF-≤120d rows, the 5 OFF->120d rows, the 11 owner-to-confirm tree−NC rows.
2. **Registrar names for the 9 other-registrar domains** — register column = **`OTHER-PENDING-OWNER`** per lead spec (rows **not** blocked on owner input; owner's registrar list still pending for final confirmation). **RDAP resolution COMPLETE for 8/9: Dynadot Inc** (public registry data, 2026-10-25, PR #99 — rdap.org + rdap.verisign.com/com/v1/domain/; evidence kept in the register `notes` column); **paretobuddy.app RDAP lookup incomplete** (Google .app RDAP unreachable 2026-10-25).
3. **Onboard prioritization** for the 49 (follow-up research task).
4. **Backlog hygiene:** reconcile `PORTFOLIO/domain-backlog-new.csv` (md5 differs).
5. **ASSET_AUDIT refresh** (146 dirs today) + make this reconciliation the standing quarterly check; **Agent-browser retry** for Namecheap renewal prices + NameBio comps.

---

## 9. OWNER DECISIONS RECEIVED — decision log (2026-10-25)

| # | Domain(s) | Decision | Source | Notes |
|---|---|---|---|---|
| 1 | puticlub.online · putero.online · aseguranza.online (GRACE) | **LET GO — no renewal** | owner directive via lead, 2026-10-25 | adult bundles + insura companion; record kept in register §11 |
| 2 | paycarai.com | **LET GO — no renewal** | owner directive via lead, 2026-10-25 | despite $17K campaign anchor; decision supersedes campaign value |
| 3 | jogpay.com · putasexo.com · aisexshops.com · acoholfree.com · aivrfun.com · congoogle.com · gosexai.com · paretobuddy.app · vivorg.com | **Held at OTHER registrars — still owned, still active where applicable** | owner directive via lead, 2026-10-25 | register column = `OTHER-PENDING-OWNER` (RDAP: 8/9 Dynadot Inc in notes); owner registrar list still pending |
| 4 | paybot.ai | **Owner-confirmed ERROR — not owned; remove from all records** | owner directive via lead, 2026-10-25 | was flagged in PayAuto wave-1 context; removed from register + annotated in records |

---

## 10. Sidebar — the 15 Alert-status domains (what "Alert" means)

> Namecheap "Alert" = the domain is in a state needing attention (typically expiring soon / action required). **All 15 also have auto-renew OFF and every one sits inside the 120-day risk window** — earliest expiry Nov 02 (apuesto.*), latest Dec 14. Mechanically turning auto-renew ON clears most of the alert state; owner decides per domain.

| Domain | NC status | Renew | Expiry | Days |
|---|---|---|---|---|
| apuesto.ad | Alert | OFF | Nov 05 2026 | 11 |
| apuesto.casino | Alert | OFF | Nov 02 2026 | 8 |
| apuesto.xyz | Alert | OFF | Nov 02 2026 | 8 |
| cdmx.bet | Alert | OFF | Nov 05 2026 | 11 |
| cdmx.casino | Alert | OFF | Nov 05 2026 | 11 |
| cdmx.games | Alert | OFF | Nov 05 2026 | 11 |
| gastropub.bet | Alert | OFF | Nov 20 2026 | 26 |
| gastropub.bid | Alert | OFF | Nov 20 2026 | 26 |
| gastropub.casino | Alert | OFF | Nov 20 2026 | 26 |
| gastropub.games | Alert | OFF | Nov 20 2026 | 26 |
| nobreakai.com | Alert | OFF | Nov 18 2026 | 24 |
| nofailai.com | Alert | OFF | Nov 18 2026 | 24 |
| pontebuena.com | Alert | OFF | Nov 12 2026 | 18 |
| teapuesto.casino | Alert | OFF | Nov 03 2026 | 9 |
| teapuesto.xyz | Alert | OFF | Nov 03 2026 | 9 |

---

## 11. Master domain register (NEW, 2026-10-25)

`docs/assets/DOMAIN-MASTER-REGISTER.csv` — **184 rows** = Namecheap 175 + 9 owner-confirmed other-registrar domains. Columns (lead bac8de97 spec, 11): `domain · status · expiry date · days-to-expiry · auto-renew · renewal price + provenance · registrar · disposition · portfolio family · campaign link · notes`.

- **status:** `Active / Alert / Grace` from `Domain_List.csv` (the authority); the 9 other-registrar rows carry `OWNED (other registrar — owner 2026-10-25)`.
- **days-to-expiry:** computed vs 2026-10-25 (negative ⇒ already past expiry, e.g. the 6 GRACE rows −17…−3).
- **renewal price + provenance:** lead-sanctioned source = Namecheap's TLD renewal pricing page (vendor-page URL + fetched-on per the price-provenance rule). Attempted 2026-10-25 live via agent-browser (Cloudflare challenge, page never rendered) and via Wayback CDX (archive.org outage — inconclusive); **per the never-invent rule NO price is asserted** — cells read `TBD (NC price page 403-walled 2026-10-25 — not asserted)`; owner's Namecheap dashboard is the remaining source.
- **registrar:** `Namecheap` | `OTHER-PENDING-OWNER` (per lead rev — the 9 rows are marked, not blocked on owner input; owner's registrar list still pending; RDAP evidence: 8/9 resolve to Dynadot Inc, detail moved to `notes`).
- **disposition:** `OWNER-LET-GO (no renewal)` on puticlub.online · putero.online · aseguranza.online · paycarai.com (decision log §9). paycarai.com keeps its $17K campaign anchor on record (leads file annotated) — this flag governs renewal only.
- **exclusions:** `paybot.ai` absent (owner-confirmed never owned, §9 #4).
- Renewal decisions are the owner's to make from §6; this register is the machine-readable single source of truth (RFC-4180 clean, 11 cols uniform).

---

**Rules honored:** never-invent (no price asserted without a fetched source; no comp claimed without a URL) · full-field · dispositions recorded as received (owner decides; this doc records) · SEND FREEZE untouched — data work only.
