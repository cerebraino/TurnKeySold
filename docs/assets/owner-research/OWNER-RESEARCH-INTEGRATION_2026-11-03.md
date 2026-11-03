# Owner buyer-research workbook — integration + verification (2026-11-03)

**Wave:** owner-supplied buyer research integration (`cerebraino-patch-3`, commit `9bcb9f6`) · **Author:** domain-researcher · **Status:** research/data only · **⏸️ SEND FREEZE INTACT — nothing sends, no email tool touched, no copy authored.**

---

## §0 What landed

| Item | Value |
|---|---|
| Owner source file | `Domains Target Buyers.xlsx` (branch `cerebraino-patch-3`, commit `9bcb9f6`) |
| Verbatim repo copy | `docs/assets/owner-research/Domains-Target-Buyers_2026-11-03.xlsx` |
| Bytes / MD5 | 29,003 · `697962de028bf14cf9b9afae274d2ff5` (byte-identical to the branch original) |
| Sheet | `Sheet 1 - findings_log` (only sheet) |
| Rows | 55 total · **data rows 3–55 = 53 findings** · row 1 title, row 2 header |
| Distinct domains | **41** |
| Finding dates | 2026-09-07 → 2026-11-02 |
| Canonical CSV | `docs/assets/owner-research/OWNER-BUYER-FINDINGS_2026-11-03.csv` (53 × 14, verbatim cells + decode note) |
| Verification CSV | `docs/assets/owner-research/OWNER-BUYER-FINDINGS-VERIFICATION_2026-11-03.csv` (adds verdict, note, HTTP status, fetched-on, route gate) |
| Per-domain files | 41 × `DOMAINS/<domain>/01-research/OWNER-FINDINGS-2026-11-03.md` + a dated section appended to each existing `leads_*.md` |

**Two corrections to the delegation brief (verified with openpyxl against the raw XML, not assumed):**
1. **The data is rows 3–55 (53 findings), not rows 6–55 (50).** Row 2 is the header (`date | domain | company_buyer | contact_person | contact_info | motivation_rationale | confidence | urgency | source_url | suggested_outreach_angle | matched_buyer_category`); row 1 is the sheet title `findings_log`. Reading from row 6 would have silently dropped 3 findings.
2. **The column shift is real but rarer than described.** Only **3 of 53** rows are mis-aligned, and the direction differs: **one row shifted +1** (F18, Adam & Eve — `F` present but empty, so rationale lands in `G`, fit `H`, urgency `I`, url `J`, angle `K`, category `L`) and **two rows shifted −1** (F07 Visa, F10 iCarros — the blank cell is *earlier* in the row, so fit lands in `F`, urgency `G`, url `H`, angle `I`, category `J`). Rows where only `contact_person` is blank (nychispano ×2, paguesucasa, nofailai.com, poweraiready, muyloca, teapuesto.xyz, vivamucho, lavoiture/Wayve, automoveis/Auto Avaliar) are **not** shifted — the empty cell is styled and present. Each affected row carries its decode in the CSV `decode_note` column and in the per-domain file.

## §1 Column mapping (settled)

Read positionally with `openpyxl` `values_only` by column letter; never by skipping empties.

| Sheet col | Header (row 2) | Canonical CSV field | Handling |
|---|---|---|---|
| A | date | `finding_date` | as stored (ISO) |
| B | domain | `domain` | whitespace-normalised (one cell wrapped `losangeleshispanic.com` across a line break) |
| C | company_buyer | `company_buyer` | verbatim |
| D | contact_person | `contact_person` | verbatim; blank where the owner left it empty (10 rows) |
| E | contact_info | `contact_info` | verbatim (mostly the literal string `none published`) |
| F | motivation_rationale | `motivation_rationale` | verbatim; **empty for F07 (blank in source)**; for F10 the value sits in E (shift −1) |
| G | confidence (fit 1–5) | `fit_score` | integer as stored |
| H | urgency (timing 1–5) | `timing_score` | integer as stored |
| I | source_url | `source_url` | verbatim URL (single value per row) |
| J | suggested_outreach_angle | `suggested_outreach_angle` | verbatim — **recorded, not adopted** (see §6) |
| K | matched_buyer_category | `matched_buyer_category` | verbatim |
| L, M | *(unnumbered)* | `matched_buyer_category` | extra category values appended with ` \| ` — used by 2 rows only (F01 Stellantis: `autonomous driving`, `AI mobility`) |

Shift decode rule used: locate the `http` cell (= `source_url`), take its column offset from `I`, and read rationale/fit/urgency/angle/category relative to it. This is the only rule that survives both shift directions without inventing values.

## §2 Verification pass — method

- Every one of the **51 unique source URLs** was fetched on **2026-11-03** with `curl -sL` (desktop browser UA, 25 s timeout), body saved and searched for the specific figures/names the row claims.
- **Verdict classes:** `VERIFIED` (page supports the claim, timing still live) · `VERIFIED-EXPIRED` (claim supported but the event/window has passed) · `PARTIAL` (page live, part of the claim not literally supported) · `NOT-VERIFIED` (404 / no support on the page) · `BLOCKED` (WAF challenge / 401 / 403 / 429 — **claim neither confirmed nor denied, no bypass attempted**).
- **Never-invent:** a blocked or dead source produces a recorded verdict, never an asserted fact. No figure from a blocked page is repeated as ours.
- **No WAF/anti-bot evasion:** Cloudflare/`Access Denied`/`429` responses were recorded as blocked. NameBio was not touched (standing IP-block rule).
- **Contacts:** only literally published contact points pass the gate. Press *quotes* do not.

### §2a Verdict tally (53 findings)

| Verdict | Count |
|---|---|
| VERIFIED | **23** |
| VERIFIED-EXPIRED | **6** |
| PARTIAL | **6** |
| NOT-VERIFIED | **4** |
| BLOCKED | **14** |
| **Total** | **53** |

Read it plainly: **29 of 53 findings (55%) are usable as verified company context** (23 live + 6 expired-timing), **6 are partial**, **4 are not supported by their own cited URL**, and **14 sit behind a bot wall** — i.e. roughly a quarter of this workbook could not be checked from our egress and must not be quoted as fact until re-checked owner-side.

### §2b Key figures the brief asked about

| Claim in workbook | Finding | What the fetched page actually shows | Verdict |
|---|---|---|---|
| Harvey $200M at $11B (CNBC 2026-03-25) | F09 | CNBC headline verbatim: *"Legal AI startup Harvey raises $200 million at $11 billion valuation"* | **VERIFIED** |
| Chime acquires Stride Bank for $590M | F37 | Cryptonomist: *"Chime Stride Bank Acquisition Finalized for $590M"* ($590 ×11, Stride ×50) | **VERIFIED** |
| Clay $7B pre-money / $115M Wellington round | F38 | TFN headline: *"Clay hits $7.1B valuation with $115M raise…"*, Wellington present | **VERIFIED** (headline states $7.1B valuation; "$7B pre-money" is the source's reading, not verbatim) |
| Webmotors buys 51%/control of Auto Avaliar, R$1.1B (UOL) | F55 | UOL returns **HTTP 403 Access Denied** | **BLOCKED** — not asserted |
| MercadoLibre BRL 57B Brazil investment | F11 | `reuters.com/company/mercadolibre-inc` returns **HTTP 401** auth stub (544 bytes) | **BLOCKED** — not asserted |
| CoreWeave × NVIDIA Vera CPU | F48 | StorageNewsletter headline verbatim | **VERIFIED** |
| Datadog DASH launches (Journey Monitoring, Bits Testing) | F42 | Stockwirex piece confirms both, DASH ×26 | **VERIFIED** |
| G2 added 27 new AI categories since Feb 2026 | F33 | G2 post title + "27"/"categories"/"February" all present | **VERIFIED** |
| PagerDuty Jeli EOL 2026-12-22 | F08 | Aurora SRE post: "December 22" ×9, "end of life" ×20 | **VERIFIED** |
| Codere Online = NFL official betting partner in Mexico | F35 | GlobeNewswire release confirmed | **VERIFIED** |
| HubSpot × Clay session Sept 16–18 | F20 | UNBOUND session page live; **window has passed** | **VERIFIED-EXPIRED** |
| LA mayoral debate on KVEA Oct 13 | F44 | `nbc.com/noticias-telemundo` is a generic station page — no "mayoral", "October 13" or "KVEA" (0 hits) | **NOT-VERIFIED** (and the date has passed) |
| Chase mortgage rate sale "through October 4" | F45 | NMM piece confirms a "rate sale"/"limited-time" offer; the literal deadline is not on the page | **VERIFIED-EXPIRED** |

### §2c Dead or unsupported sources (do not cite)

- **F16 · aisexshops.com · Adam & Eve** — HTTP 404 · PR Newswire URL returns HTTP 404 ("404 Page Not Found") — the Adam & Eve × The Boys / Ambrosius claim is NOT verifiable from the cited source.
- **F17 · aisexshops.com · Lovense** — HTTP 404 · reformer.com URL returns HTTP 404 ("404 - reformer") — Lovense CES 2026 / Diamo claim NOT verifiable from the cited source.
- **F26 · halfpricednames.com · Namecheap** — HTTP 200 · Namecheap status page is live (HTTP 200) but carries none of the claimed content ("Namecheap Market" 0, "September 22" 0) — status feed is transient; the Sept 22 maintenance claim is unsupported.
- **F42 · losangeleshispanic.com · Telemundo 52 (KVEA)** — HTTP 200 · nbc.com/noticias-telemundo is a generic station page: no "mayoral", "October 13" or "KVEA" (0 hits). The LA debate claim is NOT supported by the cited URL — and the Oct 13 event has passed.

### §2d Blocked sources (documented, not circumvented)

| Finding | Domain · buyer | URL | Block type |
|---|---|---|---|
| F08 | automoveis.ai · iCarros | `https://app.dealroom.co/news/feed/conectcar-acquires-icarros-automotive-classifieds-platform-fr` | HTTP 403 |
| F09 | automoviles.ai · Mercado Libre | `https://reuters.com/company/mercadolibre-inc` | HTTP 401 |
| F19 | cheapslimmeds.com · Hims & Hers | `https://investors.hims.com/news/news-details/2026/Hims--Hers-Announces-Strategic-Shift-for-US-W` | HTTP 403 |
| F23 | nychispano.com · NYC Hispanic Chamber of Commerce | `https://hispanicchamber.nyc/events/` | HTTP 403 |
| F25 | jogpay.com · Strava | `https://the5krunner.com/2026/09/15/strava-september-update/` | HTTP 403 |
| F27 | payauto.ai · Natural | `https://www.fintechfutures.com/venture-capital-funding/natural-bags-30m-launches-agentic-paymen` | HTTP 403 |
| F28 | payauto.ai · Mastercard | `https://www.mastercard.com/us/en/news-and-trends/press/2026/june/mastercard-launches-agent-pay-` | HTTP 403 |
| F29 | automovel.ai · Webmotors | `https://tiinside.com.br/08/09/2026/webmotors-implementa-ia-no-whatsapp-para-reduzir-tempo-de-cr` | HTTP 403 |
| F38 | bestslimmeds.com · WeightWatchers (WW) | `https://corporate.ww.com/news/news-details/2026/Weight-Watchers-Expands-Its-Integrated-GLP-1-Pl` | HTTP 403 |
| F41 | mypatientprep.com · Zocdoc | `https://www.zocdoc.com/about/news` | HTTP 403 |
| F48 | apuesto.xyz · Stake.com | `https://stake.com/blog/new-casino-releases-2026-10-09` | HTTP 403 |
| F51 | vivamucho.com · Expedia Group | `https://www.expedia.com/newsroom/fall-2026-product-release-expedia-group-launches-ai-powered-to` | HTTP 429 |
| F52 | lavoiture.ai · Wayve | `https://www.media.stellantis.com/uk-en/corporate/press/wayve-stellantis-and-nvidia-collaborate-` | HTTP 403 |
| F53 | automoveis.ai · Auto Avaliar | `https://economia.uol.com.br/colunas/monica-scaramuzzo/2026/10/27/exclusivo-webmotors-compra-con` | HTTP 403 |

## §3 Contact / route gate (never-invent ledger)

Only **three** rows carry anything other than the literal string `none published`, and exactly **one** address in the whole workbook is a real published contact point:

| Finding | Party | Contact as written | Gate |
|---|---|---|---|
| F04 | Stripe (Viraj Gupta) | `viraj.gupta@stripe.com (quoted in press coverage)` | NOT-FIREABLE — press QUOTE ("quoted in press coverage"), not a published contact |
| F05 | Visa International (Rubail Birwadker) | `Rubail Birwadker, SVP head of growth products and partnerships at Visa, quoted in Stripe blog post on agentic commerce expansion` | PARTIAL — person named, no published route |
| F16 | Adam & Eve (Katy Zvolerin) | `919.644.8100 x3121; 402358@email4pr.com (PR)` | FIREABLE-GATED per owner gate — BUT citing page returns HTTP 404; re-source before firing |
| F52 | Wayve (no name) | `hello@wayve.ai; +44 20 4574 5971` | FIREABLE-GATED (literal published general contact) — citing page HTTP 403, re-open before firing |

**The Stripe row is the trap the brief flagged, and the gate holds:** `viraj.gupta@stripe.com` is annotated in the owner's own sheet as *"(quoted in press coverage)"* — a press **quote**, not a published contact address. Recorded **NOT-FIREABLE**. It must never enter a send list on the strength of this row.
**Wayve** (`hello@wayve.ai`, `+44 20 4574 5971`) is a genuine published general contact, so it passes the literal-publication gate — but the citing Stellantis page returned **403**, so the provenance link needs re-opening owner-side before it is used. **Adam & Eve**'s PR phone/`402358@email4pr.com` are literal in the sheet, but their citing PR Newswire page is **404** — re-source first; a third-party PR wire address is also a poor route for a strategic domain conversation.
**Everything else: no route.** 49 of 53 findings record no published contact at all. No address was constructed, inferred or pattern-guessed anywhere in this wave.

## §4 Ownership reconciliation (all 41 domains)

Checked against `docs/assets/DOMAIN-MASTER-REGISTER.csv` (184 rows). **37 of 41 domains reconcile cleanly; 4 do not.**

*`days` is the register's own `days-to-expiry` value, computed when the register was built (2026-10-25) — recompute before acting on any renewal date.*

| Domain | Findings | Register status | Expiry / days | Renew | Verdict |
|---|---|---|---|---|---|
| `aiapp.bet` | 1 | Active | Nov 26 2026 / 32d | ON | OWNED ✅ |
| `aisexshops.com` | 2 | OWNED (other registrar — owner 2026-10-25) | — (other-registrar row, not in NC export) | — | OWNED ✅ |
| `apuesto.ai` | 1 | Active | Nov 02 2027 / 373d | ON | OWNED ✅ |
| `apuesto.xyz` | 1 | Alert | Nov 02 2026 / 8d | OFF | OWNED ✅ |
| `automoveis.ai` | 2 | Active | May 17 2028 / 570d | ON | OWNED ✅ |
| `automovel.ai` | 1 | Active | May 17 2028 / 570d | ON | OWNED ✅ |
| `automovil.ai` | 1 | Active | Nov 29 2027 / 400d | ON | OWNED ✅ |
| `automoviles.ai` | 1 | Active | Oct 14 2027 / 354d | ON | OWNED ✅ |
| `bestslimmeds.com` | 1 | Active | Dec 01 2026 / 37d | ON | OWNED ✅ |
| `cheapslimmeds.com` | 1 | Active | Dec 01 2026 / 37d | ON | OWNED ✅ |
| `dalai.com` | 1 | NOT IN REGISTER | — | — | **OWNERSHIP UNCONFIRMED — OWNER DECISION** ⚠️ |
| `fusebot.ai` | 1 | Active | Sep 29 2027 / 339d | ON | OWNED ✅ |
| `halfpricednames.com` | 1 | Active | Dec 18 2026 / 54d | OFF | OWNED ✅ |
| `jogpay.com` | 1 | OWNED (other registrar — owner 2026-10-25) | — (other-registrar row, not in NC export) | — | OWNED ✅ |
| `knowlaw.ai` | 1 | Active | Oct 14 2027 / 354d | ON | OWNED ✅ |
| `latinoabogado.com` | 1 | Active | Jan 06 2027 / 73d | ON | OWNED ✅ |
| `latinomedico.com` | 1 | Active | Jan 06 2027 / 73d | ON | OWNED ✅ |
| `lavoiture.ai` | 3 | Active | Jun 04 2028 / 588d | ON | OWNED ✅ |
| `losangeleshispanic.com` | 1 | Active | Dec 25 2026 / 61d | ON | OWNED ✅ |
| `muyloca.com` | 1 | Active | Dec 18 2026 / 54d | ON | OWNED ✅ |
| `mypatientprep.com` | 1 | Active | Apr 04 2027 / 161d | OFF | OWNED ✅ |
| `nofail.ai` | 1 | Active | Oct 26 2027 / 366d | ON | OWNED ✅ |
| `nofailai.com` | 1 | Alert | Nov 18 2026 / 24d | OFF | OWNED ✅ |
| `nychispano.com` | 2 | NOT IN REGISTER | — | — | **OWNERSHIP UNCONFIRMED — OWNER DECISION** ⚠️ |
| `pagatucasa.com` | 1 | Active | Dec 07 2026 / 43d | ON | OWNED ✅ |
| `paguesucasa.com` | 1 | Active | Feb 10 2027 / 108d | ON | OWNED ✅ |
| `parardebeber.com` | 1 | Active | Dec 22 2026 / 58d | ON | OWNED ✅ |
| `paretobuddy.com` | 4 | Active | Jun 14 2027 / 232d | OFF | OWNED ✅ |
| `payauto.ai` | 4 | Active | Dec 15 2027 / 416d | ON | OWNED ✅ |
| `paybet.ai` | 1 | Active | Dec 15 2027 / 416d | ON | OWNED ✅ |
| `paybud.ai` | 1 | Active | Dec 15 2027 / 416d | ON | OWNED ✅ |
| `platicar.ai` | 1 | Active | Oct 08 2027 / 348d | ON | OWNED ✅ |
| `poweraiready.com` | 1 | Active | Jun 03 2027 / 221d | ON | OWNED ✅ |
| `sandbagai.com` | 1 | Active | Jan 04 2027 / 71d | ON | OWNED ✅ |
| `teapuesto.xyz` | 1 | Alert | Nov 03 2026 / 9d | OFF | OWNED ✅ |
| `theaicustomeracquisition.com` | 2 | Active | Jan 18 2027 / 85d | ON | OWNED ✅ |
| `theaileadgenerator.com` | 1 | Active | Jan 18 2027 / 85d | ON | OWNED ✅ |
| `topproducts.ai` | 1 | Active | Mar 05 2027 / 131d | ON | OWNED ✅ |
| `topsex.ai` | 1 | Active | Dec 26 2027 / 427d | ON | OWNED ✅ |
| `veraroi.com` | 1 | NOT IN REGISTER | — | — | **OWNERSHIP UNCONFIRMED — OWNER DECISION** ⚠️ |
| `vivamucho.com` | 1 | NOT IN REGISTER | — | — | **OWNERSHIP UNCONFIRMED — OWNER DECISION** ⚠️ |

### §4a The four unresolved holdings

| Domain | Situation | Recommendation |
|---|---|---|
| `vivamucho.com` | Register holds **`vivemucho.com`** (Active, 2027-01-28, renew ON) but not `vivamucho.com`. The two spellings are a documented 2-domain pack (Genspark research), and a `DOMAINS/vivamucho.com/` tree already exists — but the register does not list the name. | **Owner: confirm which spelling is actually registered.** Until then no campaign work on `vivamucho.com`; treat the finding (Expedia) as belonging to the vivemucho/vivamucho pack. |
| `dalai.com` | Tree exists; register has only `dalai.co` and `dalai.fit`, **both GRACE, expired 2026-10-18, renew OFF**. The plan already carries this as a "registrar anomaly: outside NC". | **Owner: registrar + renewal decision for the whole dalai cluster.** `dalai.com`'s status is the open question; the siblings are already in grace. |
| `nychispano.com` | Tree exists (`leads_nychispano.com.md`), **not in the register at all** — no NC row, no other-registrar row. | **Owner: confirm ownership.** 2 findings (NYC Hispanic Chamber, New York Hispano) are held pending that confirmation. |
| `veraroi.com` | Tree exists, **not in the register at all**. | **Owner: confirm ownership.** 1 finding (Datadog) held pending. |

### §4b Assumption in the brief that was wrong

The brief asked me to resolve `paretobuddy.com` as "register holds `paretobuddy.APP`". **It does not — the register holds both `paretobuddy.com` (Active, 2027-06-14, renew **OFF**) and `paretobuddy.app`.** No reconciliation gap; the only thing to note is that the `.com`'s auto-renew is off and its 4 findings are the largest single block in the workbook.

## §5 Renewal-risk intersections (findings on domains that may lapse)

These are the rows where the workbook's research value is at risk from an ownership decision — worth the owner's eye before anyone invests in them:

| Domain | Expiry | Days | Renew | Findings sitting on it |
|---|---|---|---|---|
| `apuesto.xyz` | Nov 02 2026 | 8 | OFF | 1 |
| `teapuesto.xyz` | Nov 03 2026 | 9 | OFF | 1 |
| `nofailai.com` | Nov 18 2026 | 24 | OFF | 1 |
| `halfpricednames.com` | Dec 18 2026 | 54 | OFF | 1 |
| `paretobuddy.com` | Jun 14 2027 | 232 | OFF | 4 |
| `mypatientprep.com` | Apr 04 2027 | 161 | OFF | 1 |
| `dalai.com` | not in register | — | — | 1 |

`apuesto.xyz` (expiry 2026-11-02, renew OFF) and `teapuesto.xyz` (expiry **2026-11-03 — today**, renew OFF) are already at or past expiry: their findings (Stake.com, Polymarket) should be treated as **drop-candidates** unless the owner renews. `nofailai.com` (2026-11-18, 15 days, renew OFF) is the urgent one.

## §6 Rows I recommend we treat as stale or drop

Not a deletion list — a triage list, so the lead/owner can decide with the evidence in front of them.

| Bucket | Findings | Why |
|---|---|---|
| **Drop-candidates (dead source + no route)** | F18 Adam & Eve (PR Newswire 404), F19 Lovense (Reformer 404), F28 Namecheap (status page carries none of the claim), F44 Telemundo 52 (generic page, no debate) | Nothing checkable survives; nothing to act on. |
| **Expired-timing (context only, no live trigger)** | F20 HubSpot, F22 SxxxAI launch week, F24 NAHREP report, F45 Chase rate sale, F49 Billboard Latin Music Week, F52 Polymarket/Brazil runoff | The event the row is built around has passed; the company facts survive, the urgency does not. |
| **Internally inconsistent** | F17 Sunsama — a 2026-09-08 finding cites a "Nov 2026" consolidation wave (future-dated at the time of writing) | Treat the "imminent acquisition target" framing as unverified. |
| **Reputationally sensitive — research only** | F23 Anthropic/Joe Benton (`sandbagai.com`) | The sheet itself says research-only and "do not frame the news negatively". Honoured. |
| **Blocked, high value if it checks out** | F55 Auto Avaliar/Webmotors (R$1.1B), F54 Wayve/Stellantis/NVIDIA France, F53 Expedia, F29 Natural, F30 Mastercard, F40 WW | Worth an owner-side re-check from a different egress — these are the strongest strategic rows in the sheet and we could not read any of them. |
| **Low-value / thin-fit (flag, keep for record)** | F33 G2→`topproducts.ai`, F27 Strava→`jogpay.com`, F36 Calm→`dalai.com`, F50 Stake→`apuesto.xyz` | Category-adjacent only; no naming need demonstrated. Same precedent as `paybet.ai`/`jogpay.com` thin-fit flags. |

## §7 Integration inventory (what was written where)

| Artifact | Count | Path |
|---|---|---|
| Owner workbook (verbatim) | 1 | `docs/assets/owner-research/Domains-Target-Buyers_2026-11-03.xlsx` |
| Canonical CSV | 1 | `docs/assets/owner-research/OWNER-BUYER-FINDINGS_2026-11-03.csv` |
| Verification CSV | 1 | `docs/assets/owner-research/OWNER-BUYER-FINDINGS-VERIFICATION_2026-11-03.csv` |
| This document | 1 | `docs/assets/owner-research/OWNER-RESEARCH-INTEGRATION_2026-11-03.md` |
| Per-domain findings files | 41 | `DOMAINS/<domain>/01-research/OWNER-FINDINGS-2026-11-03.md` |
| `leads_*.md` sections appended | 41 | `DOMAINS/<domain>/01-research/leads_*.md` (dated section at end of file) |

**New-lead yield (heuristic, company-name match against the existing leads file): 12 of 53 rows name a company not already in that domain's leads file** — the rest are companies the file already covers, now carrying a fresh dated signal and a verification verdict. Treated as a heuristic because company-name matching over-counts generic names.

## §8 What this wave does NOT do

- **No fresh deep research.** Depth was explicitly out of scope: no new buyer discovery, no contact sourcing, no valuation work. These are the owner's findings, integrated and checked — nothing more.
- **No copy, no pricing, no cadence.** The sheet's `suggested_outreach_angle` column is recorded verbatim per row for later use; it is **not** adopted, and no first-touch message, subject line or price is written in this wave. Pricing rules stay where they were.
- **No sending of any kind.** SEND FREEZE intact; no email tool, no list, no schedule.
- **No invented contacts.** 49/53 rows have no route; the one published address (Wayve) is flagged with its blocked provenance page.

## §9 Open items for the owner / lead

1. **Ownership rulings:** `vivamucho.com` vs `vivemucho.com` · `dalai.com` (+ the dalai.co/.fit grace pair) · `nychispano.com` · `veraroi.com`.
2. **Renewal rulings** on the six findings-bearing renew-OFF domains in §5 (`apuesto.xyz` and `teapuesto.xyz` are already at/past expiry).
3. **Blocked-source re-check** from an owner-side egress for the 14 blocked rows — especially F55 (Auto Avaliar), F54 (Wayve), F53 (Expedia), F29 (Natural), F30 (Mastercard), F40 (WW).
4. **Owner decision on whether any of this becomes outreach** — nothing here authorises a send, and the freeze stands until an explicit per-send instruction.

