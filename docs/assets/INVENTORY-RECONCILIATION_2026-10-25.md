# TurnKeySold Domains — Inventory Reconciliation (Namecheap export vs asset tree vs backlog)

**Date:** 2026-10-25 · **As-of anchor:** Namecheap CSV export merged to `main` (owner branch `Updated-Namecheap-Domains` → merge commit `3ea86bd`) · **Author:** domain-researcher (task bfbb20e6)

> **Disposition rule:** every list below is a **documented situation + options**, not a decision. Whether to renew, drop, or onboard any domain is the **owner's call** — nothing here is an assumed action. No emails, no registrar changes: this is research/data work under the standing SEND FREEZE.

---

## 1. Sources & normalization

| Source | Location | Rows / size | Authority |
|---|---|---|---|
| **Namecheap export (authoritative inventory baseline)** | `Domain_List.csv` (repo root; unchanged copy also at `/home/team/shared/Domain_List.csv`) | **175 domains** (175 unique) | Registrar export — the owner's own list of what is at Namecheap. Columns: domain · privacy · NC status · auto-renew · expiry |
| **DOMAINS/ asset tree** | `DOMAINS/*/` on `main` | **146 domain dirs** + `DOMAINS/coldbeerportfolio/` bundle folder + `DOMAINS/CSV/` meta-dir (portfolio CSVs, skip) | Research/outreach assets per domain (leads, packs, verification) — coverage, not ownership proof |
| **Backlog CSV** | `domain-backlog-new.csv` (repo root; canonical copy for this pass) | **110 rows** | Planning/subset file — candidate ideas + rough estimates. **Not authoritative for ownership** (some rows are research notes, dup-verifies, or stale) |

**Normalization:** all domain keys lowercased, trailing dots stripped, compared case-insensitively across the three sources (grep-style scans of this repo must be case-insensitive — uppercase dir stems exist, e.g. `leads_Puticlub.online.md`). No fuzzy matching; a domain either matches exactly or it does not.

**Delta vs August audit:** `ASSET_AUDIT_2026-08-14.md` recorded **145 domain dirs + coldbeerportfolio = 146 assets**. The current tree has **146 domain dirs** (+ coldbeerportfolio + CSV meta) — i.e. **+1 domain dir since the audit** (dirs added by later waves; audit refresh listed as follow-up, §8).

**Backlog copies:** `PORTFOLIO/domain-backlog-new.csv` exists as a second copy whose md5 differs from the root file (recipient: root `cd027a3b0d`, PORTFOLIO `641d0ad816`). Root treated as canonical here; reconcile later (§8).

---

## 2. Three-way picture (counts)

| Set | Count |
|---|---|
| Namecheap export (A) | **175** |
| Asset dirs (B) | **146** (+ coldbeerportfolio folder + CSV meta) |
| Backlog rows (C) | **110** |
| A ∩ B — in registrar AND has asset dir | **126** |
| A − B — registrar, **no** asset dir (§3, onboard) | **49** |
| B − A — asset dir, **not** in registrar list (§4) | **20** |
| A ∩ C | **101** |
| B ∩ C | **78** |
| C − A − B — backlog row in neither (§5) | **1** |

Checks: 126 + 49 = 175 ✓ (A) · 146 = 126 + 20 ✓ (B) · 101 + 9 = 110 ✓ (C) · every backlog domain is in A or B **except 1** (§5).

---

## 3. In registrar but no asset dir — **49 onboard candidates**

> These are owned at Namecheap but have no `DOMAINS/<name>/` asset package (no leads/brief research, no outreach workbench). Onboarding = create the dir + lead file when the domain joins an active wave. **Not all 49 are equal** — the curated notes mark the ones this report knows: active-campaign (paycarai.com), incoming (comeplantas.com — dir lands with PR #95), parent-brand (turnkeysold.com), GRACE-at-risk (§6), .si casino cluster, geo/companion clusters.

| Domain | NC status | Renew | Expiry | Notes |
|---|---|---|---|---|
| agentbucks.si | Active | ON | Oct 18 2027 | .si casino TLD cluster (cardbot.si / automoviles.si / spendbot.si) |
| agentickillswitch.org | Active | OFF | Sep 24 2027 | renew-OFF 334d (>120d) — next window |
| ahburro.com | Active | ON | Jul 31 2027 | — |
| aseguranza.ai | Active | ON | Oct 16 2027 | — |
| aseguranza.online | Grace | OFF | Oct 14 2026 | ⚠ GRACE — see §6 (expired) |
| automoviles.si | Active | ON | Oct 18 2027 | .si casino TLD cluster |
| birrafria.com | Active | ON | Feb 21 2027 | in backlog (Spanish Beverage; est $500–$3K) |
| buentino.com | Active | ON | Nov 12 2027 | in backlog (Brandable/Spanish; est $500–$2K) |
| carboingratos.com | Active | OFF | Jan 17 2027 | in backlog (Food/Spanish; est $500–$2K) |
| cardbot.si | Active | ON | Oct 18 2027 | .si casino TLD cluster |
| cdmx.casino | Alert | OFF | Nov 05 2026 | Alert + renew-OFF — see §6 |
| cdmx.games | Alert | OFF | Nov 05 2026 | Alert + renew-OFF — see §6 |
| cervefria.com | Active | OFF | Feb 21 2027 | in backlog (Spanish Beverage; est $500–$3K) |
| cervezahelada.com | Active | ON | Dec 10 2026 | in backlog (Spanish Beverage; est $500–$3K) |
| chelafria.com | Active | ON | Dec 10 2026 | in backlog (Spanish Beverage; est $500–$3K) |
| chevefria.com | Active | ON | Dec 10 2026 | in backlog (Spanish Beverage; est $500–$3K) |
| chiefaiadviser.com | Active | ON | Sep 24 2027 | — |
| coldbeerportfolio.com | Active | OFF | Feb 21 2027 | Companion to DOMAINS/coldbeerportfolio/ bundle folder; ⚠ renew-OFF 119d — see §6 |
| comeplantas.com | Active | ON | Dec 18 2026 | Active campaign of 2026-10-25 wave — asset dir arrives with PR #95 (DOMAINS/comeplantas.com/) |
| desmadrito.com | Active | OFF | Feb 03 2027 | in backlog (Brandable/Spanish; est $500–$2K) |
| fieldphotolog.com | Active | ON | Oct 18 2027 | — |
| fierotumodo.com | Active | ON | Jul 21 2027 | in backlog (Brandable/Spanish; est $500–$2K) |
| fotobitacora.com | Active | ON | Oct 22 2027 | in backlog (Enterprise/Spanish; est $500–$2K) |
| fotobrujo.com | Active | ON | Sep 09 2027 | — |
| fuxiaballerinas-qro.com | Active | ON | Jul 01 2027 | in backlog (Commercial; est $100–$300) |
| haymota.com | Active | ON | Jan 31 2027 | in backlog (Cannabis/Spanish; est $500–$3K) |
| humanoscomoservicio.com | Active | ON | Apr 06 2027 | in backlog (Tech/Spanish; est $500–$2K) |
| iapolitica.com | Active | ON | Feb 11 2027 | in backlog (Brandable/Spanish; est $500–$2K) |
| iatuya.com | Active | ON | Jul 21 2027 | in backlog (Brandable/Spanish; est $500–$2K) |
| juanlauro.com | Active | ON | Jan 05 2027 | in backlog (Personal; est $300–$1K) |
| mobileworklog.com | Grace | OFF | Oct 22 2026 | ⚠ GRACE — see §6 (expired) |
| nobreakai.com | Alert | OFF | Nov 18 2026 | Companion to nobreak.ai (dir exists) |
| onegal.net | Active | OFF | Feb 01 2027 | Companion cluster to oneguy.org / topguys.net / topaiguys.com |
| ordendetrabajo.com | Active | ON | Oct 24 2027 | in backlog (Enterprise/Spanish; est $500–$2K) |
| oyenota.com | Active | ON | Oct 02 2027 | — |
| paguesuacasa.com | Active | ON | Dec 10 2026 | casa-variant of tree family paguesucasa.com / quitesuacasa.com |
| paybud.si | Active | ON | Oct 18 2027 | Companion to paybud.ai (payments family) |
| photologbook.com | Active | ON | Oct 22 2027 | in backlog (Enterprise/Mobile; est $500–$2K) |
| photosorcerer.com | Active | ON | Sep 09 2027 | — |
| pontebuena.com | Alert | OFF | Nov 12 2026 | in backlog (Brandable/Spanish; est $500–$2K) |
| quieromota.com | Active | ON | Jan 31 2027 | in backlog (Cannabis/Spanish; est $500–$3K) |
| spendbot.si | Active | ON | Oct 18 2027 | .si casino TLD cluster |
| topguys.net | Active | ON | Dec 14 2026 | Companion cluster to oneguy.org / topaiguys.com |
| topshelfer.com | Active | ON | Dec 25 2026 | in backlog (Brandable/English; est $500–$2K) |
| turnkeysold.com | Active | ON | Jun 24 2027 | Parent brand — business domain, not a sellable asset (keep) |
| umagelada.com | Active | ON | Feb 22 2027 | in backlog (Spanish Beverage; est $500–$3K) |
| usaichief.com | Active | ON | Sep 23 2027 | AI-office brandables (chiefaiadviser / usaichief / usaiczar) |
| usaiczar.com | Active | ON | Sep 23 2027 | AI-office brandables (chiefaiadviser / usaichief / usaiczar) |
| viejanueva.com | Active | ON | Aug 14 2027 | — |

**Onboard-row highlights (curated):**
- `paycarai.com` — **renew-OFF, expires 2026-12-03 (39d)**; hard flag, see §6.
- `comeplantas.com` — renew-ON, Active; asset dir incoming via PR #95 (owner-directed campaign, 2026-10-25 wave).
- `turnkeysold.com` — parent brand; keep as business domain, not a sellable asset.
- `aseguranza.online` / `mobileworklog.com` — already in strong GRACE (expired); see §6 before any onboarding.
- .si casino TLD quartet: `agentbucks.si`, `cardbot.si`, `automoviles.si`, `spendbot.si` (all Active, renew OFF).
- Companions: `nobreakai.com` (nobreak.ai) · `paguesuacasa.com` (paguesucasa.com dir) · `paybud.si` (paybud.ai) · `onegal.net`/`topguys.net` (oneguy.org-family) · `coldbeerportfolio.com` (bundle folder) · `paguesucasa.com` sibling.

---

## 4. In asset tree but NOT in the Namecheap export — **20**

> ⚠️ **Read carefully:** absence from the Namecheap export means the domain is **not registered at Namecheap**. It does **not** by itself mean sold/expired — the owner may hold many of these at **another registrar**. The adult portfolio is the proof: 7 of its 9 domains ARE in the export, but `putasexo.com` and `aisexshops.com` are not — and the backlog itself flags those two as adult-portfolio members with an explicit "verify if dup" note. **Nothing below is called "sold" without evidence.** Every row: options only — owner to confirm.

**8 of the 20 also have backlog rows; 12 are tree-only (no backlog, no NC).**

| Domain | In backlog | Context / evidence on file | Provisional read |
|---|---|---|---|
| acoholfree.com | yes | Backlog row (★★★; alcohol-free lifestyle brandable). No NC row. | absence vs backlog: owner to confirm |
| aisexshops.com | yes | Backlog row: "⚠ Already in Adult Portfolio as AIsexshops.com — verify if dup". Business plan lists it in Adult Portfolio ($15K). | Adult-portfolio member NOT at Namecheap — likely another registrar; owner to confirm (not treated as sold) |
| aivrfun.com | yes | Backlog row (★★★★; AI+VR+fun). No NC row. | absence vs backlog: owner to confirm |
| aseguranzaautos.com | no | Insura-cluster (aseguranza.ai / .online at NC). No NC row for this .com. | absence vs NC: owner to confirm |
| congoogle.com | yes | Backlog row (★★★; "with Google"). No NC row. | absence vs backlog: owner to confirm |
| dalai.com | no | Tree dir exists; dalai.co + dalai.fit at Namecheap are GRACE/expired (see §6). dalai.com itself has NO NC row. | ⚠ Dalai cluster — core domain outside Namecheap (or never owned); owner to confirm ownership + renew sisters |
| gosexai.com | yes | Backlog row (★★★; adult-AI). No NC row. | absence vs backlog: owner to confirm |
| hispanicpowerhouse.com | no | Hispano/Latino cluster dir; no NC row. | absence vs NC: owner to confirm |
| jogpay.com | yes | Business plan lists jogpay.com as ACTIVE payments-family campaign ($3K, own-research complete). Absent from NC export. | ⚠ CONFLICT FLAG — live campaign claims vs registrar export; owner to confirm (moved registrar / dropped / expiry) |
| leanmeds.com | no | Business plan Rev 18: "LeanMeds.com ✅ SOLD (Trinity HealthCare Supply)". Not in backlog rows. | SOLD per plan — remove from active lists; keep dir as record |
| muyveloz.com | no | MuyGuay-family ("muy veloz"); business plan does not list it as owned. No NC row. | likely other registrar or dropped; owner to confirm |
| muyverde.com | no | MuyGuay-family ("muy verde"); business plan does not list it as owned. No NC row. | likely other registrar or dropped; owner to confirm |
| nychispanic.com | no | Latino geo-cluster dirs (nychispanic / nychispano); no NC rows. | absence vs NC: owner to confirm |
| nychispano.com | no | Latino geo-cluster dirs (nychispanic / nychispano); no NC rows. | absence vs NC: owner to confirm |
| putasexo.com | yes | Backlog row: "⚠ Already in Adult Portfolio as PutaSexo.com — verify if dup". Business plan lists PutaSexo.com ($18K). | Adult-portfolio member NOT at Namecheap — likely another registrar; owner to confirm (not treated as sold) |
| roiboss.com | no | ROI-brandable cluster (roiboss / veraroi / roiexa). No NC rows for these. | absence vs NC: owner to confirm |
| veraroi.com | no | ROI-brandable cluster (roiboss / veraroi / roiexa). No NC rows for these. | absence vs NC: owner to confirm |
| vivamucho.com | no | Spanish brandable ("viva mucho"); no NC row. | absence vs NC: owner to confirm |
| vivorg.com | yes | Backlog row (★★★; "Live"+org). No NC row. | absence vs backlog: owner to confirm |
| weputt.com | no | Golf brandable (weputt); no NC row. | absence vs NC: owner to confirm |

**Evidence-anchored rows worth the owner's eye first:** `leanmeds.com` (SOLD per business plan) · `aisexshops.com` + `putasexo.com` (adult portfolio — likely another registrar) · `jogpay.com` (⚠ live campaign claim vs registrar absence — conflict) · `dalai.com` (sisters `dalai.co`/`dalai.fit` are GRACE at NC — cluster risk) · `muyveloz.com`/`muyverde.com` (MuyGuay-family, not listed as owned in plan).

---

## 5. In neither registrar nor tree — backlog-only staleness

**1 row:** `paretobuddy.app` — backlog notes: "Companion to paretobuddy.com — .app extension" (Category Productivity, est $500–$2K). The .app variant is **not registered** at Namecheap and has no asset dir. Expectation was "nothing should be in-neither" → this single row is the exception; candidate for backlog cleanup (or deliberate keep as reasoning trail). `paretobuddy.com` itself is in the export (renew-OFF, 232d — see §6 note scope).

---

## 6. Renewal-risk table — **45 domains** (6 GRACE + 39 renew-OFF expiring ≤120d)

> Derived **entirely from `Domain_List.csv`** (as-of 2026-10-25): all domains whose auto-renew is OFF and whose expiry is inside the 120-day window, plus every GRACE-status domain (all 6 are past expiry, all renew-OFF). Count reconciliation: the brief note read "3 GRACE" — the export itself lists **6** (puticlub.online, putero.online, aseguranza.online, **dalai.co, dalai.fit, mobileworklog.com**). Total at risk = 6 GRACE + 39 OFF-≤120d = **45** — the numbers hold together (6+39+5 = 50 renew-OFF total; the remaining 5 are >120d and listed after the table).

**⚠ All 15 Alert-status domains also have renew OFF** — every Alert row appears in this table (Alert at Namecheap ~ expiring/action-needed).

### 6a. GRACE — already past expiry (highest risk; time-limited recovery)

| Domain | NC status | Expiry | Ren. | Days rel. today | Flags |
|---|---|---|---|---|---|
| aseguranza.online | Grace | Oct 14 2026 | OFF | -11 | GRACE — companion to aseguranza.ai |
| dalai.co | Grace | Oct 18 2026 | OFF | -7 | ⚠ Dalai cluster — sister dalai.com has no NC row |
| dalai.fit | Grace | Oct 18 2026 | OFF | -7 | ⚠ Dalai cluster — sister dalai.com has no NC row |
| mobileworklog.com | Grace | Oct 22 2026 | OFF | -3 | GRACE — NC-only (no asset dir) |
| putero.online | Grace | Oct 13 2026 | OFF | -12 | Adult-portfolio bundle ($3K pair with puticlub.online) — GRACE |
| puticlub.online | Grace | Oct 08 2026 | OFF | -17 | Adult-portfolio bundle ($3K pair with putero.online) — GRACE, expiring irreversibly |

### 6b. Auto-renew OFF, expiring 0–120d (39)

NC-status mix of the 39: Active=24, Alert=15.

| Domain | NC status | Expiry | Ren. | Days | Tier | Flags |
|---|---|---|---|---|---|---|
| apuesto.casino | Alert | Nov 02 2026 | OFF | 8 | ≤30d | Alert + OFF (bet-play cluster apuesto.*) |
| apuesto.xyz | Alert | Nov 02 2026 | OFF | 8 | ≤30d | Alert + OFF (bet-play cluster apuesto.*) |
| teapuesto.casino | Alert | Nov 03 2026 | OFF | 9 | ≤30d | Alert + OFF (bet-play cluster teapuesto.*) |
| teapuesto.xyz | Alert | Nov 03 2026 | OFF | 9 | ≤30d | Alert + OFF (bet-play cluster teapuesto.*) |
| apuesto.ad | Alert | Nov 05 2026 | OFF | 11 | ≤30d | Alert + OFF (bet-play cluster apuesto.*) |
| cdmx.bet | Alert | Nov 05 2026 | OFF | 11 | ≤30d | — |
| cdmx.casino | Alert | Nov 05 2026 | OFF | 11 | ≤30d | Alert + OFF (CDMX geo cluster) |
| cdmx.games | Alert | Nov 05 2026 | OFF | 11 | ≤30d | Alert + OFF (CDMX geo cluster) |
| pontebuena.com | Alert | Nov 12 2026 | OFF | 18 | ≤30d | — |
| nobreakai.com | Alert | Nov 18 2026 | OFF | 24 | ≤30d | — |
| nofailai.com | Alert | Nov 18 2026 | OFF | 24 | ≤30d | — |
| gastropub.bet | Alert | Nov 20 2026 | OFF | 26 | ≤30d | — |
| gastropub.bid | Alert | Nov 20 2026 | OFF | 26 | ≤30d | Alert + OFF (gastropub cluster) |
| gastropub.casino | Alert | Nov 20 2026 | OFF | 26 | ≤30d | — |
| gastropub.games | Alert | Nov 20 2026 | OFF | 26 | ≤30d | — |
| aiappbet.com | Active | Nov 26 2026 | OFF | 32 | 31–60d | — |
| aitopdeals.com | Active | Nov 26 2026 | OFF | 32 | 31–60d | — |
| appai.bet | Active | Nov 26 2026 | OFF | 32 | 31–60d | — |
| appaibet.com | Active | Nov 26 2026 | OFF | 32 | 31–60d | — |
| aitopshelf.com | Active | Dec 03 2026 | OFF | 39 | 31–60d | — |
| aitopshops.com | Active | Dec 03 2026 | OFF | 39 | 31–60d | — |
| aitopstuff.com | Active | Dec 03 2026 | OFF | 39 | 31–60d | — |
| aitoptravel.com | Active | Dec 03 2026 | OFF | 39 | 31–60d | — |
| aitoptrips.com | Active | Dec 03 2026 | OFF | 39 | 31–60d | — |
| paycarai.com | Active | Dec 03 2026 | OFF | 39 | 31–60d | ⚠️ HARD FLAG — active campaign (paycar.ai/paycarai.com cluster). Renew OFF + 39d: real loss risk |
| halfpricednames.com | Active | Dec 18 2026 | OFF | 54 | 31–60d | — |
| cancelarsuscripciones.com | Active | Dec 22 2026 | OFF | 58 | 31–60d | — |
| laxhispanic.com | Active | Dec 25 2026 | OFF | 61 | 61–90d | — |
| nomoreagi.com | Active | Jan 04 2027 | OFF | 71 | 61–90d | — |
| adelgazacomiendograsa.com | Active | Jan 17 2027 | OFF | 84 | 61–90d | — |
| carboingratos.com | Active | Jan 17 2027 | OFF | 84 | 61–90d | — |
| lahispano.net | Active | Jan 24 2027 | OFF | 91 | 91–120d | — |
| aikillswitch.org | Active | Jan 31 2027 | OFF | 98 | 91–120d | — |
| airedbutton.com | Active | Jan 31 2027 | OFF | 98 | 91–120d | — |
| aistopbutton.com | Active | Jan 31 2027 | OFF | 98 | 91–120d | — |
| onegal.net | Active | Feb 01 2027 | OFF | 99 | 91–120d | — |
| desmadrito.com | Active | Feb 03 2027 | OFF | 101 | 91–120d | — |
| cervefria.com | Active | Feb 21 2027 | OFF | 119 | 91–120d | Beer family (cervefria / cervezahelada / chelafria / chevefria / birrafria / umagelada) |
| coldbeerportfolio.com | Active | Feb 21 2027 | OFF | 119 | 91–120d | Companion to DOMAINS/coldbeerportfolio/ bundle folder |

### 6c. Renew-OFF beyond 120d (5, for completeness)

| Domain | Days |
|---|---|
| miniterapia.com | 128 |
| bajaturenta.com | 161 |
| mypatientprep.com | 161 |
| paretobuddy.com | 232 |
| agentickillswitch.org | 334 |

---

## 7. Standout items

1. **`paycarai.com` (39d, renew OFF, Active) — HARD FLAG.** Paycar.ai/paycarai.com is an **active campaign cluster** (payments family, own-research complete, mapped CarMax/Carvana/Stripe buyer set). Auto-renew OFF + 39 days to expiry means an idle expiry is a real loss-path. **Owner decision needed before ~2026-11-25:** renew + turn auto-renew ON (recommended option), or explicitly let expire.
2. **Adult-portfolio bundles `puticlub.online` + `putero.online` are in GRACE (expired Oct 08 / Oct 13).** The pair is valued as a $3K-each bundle in the plan. Grace recovery is time-limited — decision window is the immediate one.
3. **`dalai.co` + `dalai.fit` GRACE (expired Oct 18) with `dalai.com` outside the export** — the Dalai cluster is at a decision point as a set, not per-domain.
4. **15 of 175 domains are in Alert with renew OFF** — a mechanical sweep (turn auto-renew ON for anything to keep) removes most of §6b from the risk list.

---

## 8. Open items / options (no decisions taken)

1. **Renew-or-release now:** GRACE six (esp. puticlub.online/putero.online bundles, dalai.co/dalai.fit, mobileworklog.com, aseguranza.online). Options: renew all / renew subset / release. Owner.
2. **paycarai.com renewal** (39d) — recommended renew + auto-renew ON. Owner.
3. **The 20 not-at-Namecheap:** options — (a) confirm names at another registrar (portfolio-wide", "another registrar scan" would need the owner's other-registrar list), (b) treat as sold/expired (owner recollection), (c) re-verify leanmeds (sold) vs the other 19. Owner.
4. **Onboard prioritization for the 49** — which get asset dirs first is a lead/owner call; this report only lists them.
5. **Backlog hygiene:** drop or annotate `paretobuddy.app`; reconcile `PORTFOLIO/domain-backlog-new.csv` vs root (md5 differs).
6. **ASSET_AUDIT refresh** (146 domain dirs today vs 145 in the Aug audit) + make this reconciliation the standing quarterly check against fresh registrar exports.

---

**Rules honored:** never-invent (every claim traces to the CSV, the backlog file, or the business plan) · full-field (no paraphrase of row content — quotes are verbatim) · disposition left to the owner (options only) · SEND FREEZE untouched (data work, nothing sent).
