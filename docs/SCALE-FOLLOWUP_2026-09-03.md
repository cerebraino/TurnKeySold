# Scale-Report Follow-Up — WAF Re-Verification + Contact Paths (4 Expansion Domains)
**Prepared by:** domain-researcher | **Date:** 2026-09-03
**Task:** 6fb2708a (Phase 1 of 4-domain full expansion — curebyketo.com, fusebot.ai, weputt.com, paretobuddy.com)
**Method rules applied:** never-invent (every claim = literally-published real source with URL; aggregator-sourced = candidate-H/LinkedIn-DM only, never email), no pricing in any copy, research only — **nothing composed, nothing sent.**

---

## Part A — WAF-Flag Re-Verification (5 candidates from scale report §constraints)

Re-tested 2026-09-03: curl sweeps vs alternate paths (brand page, app subdomain) AND real-browser (agent-browser / Chrome) loads.

| Candidate | Curl status (all paths) | Real-browser (agent-browser) | Verdict |
|---|---|---|---|
| **Klook** (klook.com) | 403 (DataDome) | Reached www.klook.com; DataDome CAPTCHA iframe | **Live but bot-walled** — content not verifiable in-env; unverify-in-env |
| **Viator** (viator.com) | 403 (DataDome) | Reached www.viator.com; DataDome CAPTCHA iframe | **Live but bot-walled** — unverify-in-env |
| **Hard Rock Bet** (hardrock.bet) | 403 | Browser rendered **full real site** (sportsbook/casino, state pages, promo nav) | **✅ VERIFIED LIVE** (403 over-curl = bot-wall only) |
| **Roadster** (roadster.com) | 403 (Cloudflare) | Reached roadster.com; "Just a moment…" Cloudflare challenge | **Live but bot-walled** — unverify-in-env |
| **Karafun** (karafun.com) | 406 | Browser rendered **full real site** (karaoke catalog, apps, subscribe) | **✅ VERIFIED LIVE** (406 over-curl = bot-wall only) |

**Takeaways for campaign use:** Hard Rock Bet + Karafun = confirmed live targets (contact-path work proceeds normally). Klook/Viator/Roadster = live but heavily bot-walled (DataDome/Cloudflare); pursue via LinkedIn/exec DM rather than site-scraped contact paths; deeper live-content verification requires manual browsing.

---

## Part B — Contact-Path Research: NEW Leads on the 4 Expansion Domains

All emails below were **literally scraped from the company's own live page** (URL given). Anything from aggregators/patterns is marked **candidate-H / LinkedIn-DM only**.

### curebyketo.com (weight-loss/keto)
| NEW Lead | Contact route (fireable = published email w/ URL) | DM candidate (LinkedIn) | Status |
|---|---|---|---|
| **Perfect Keto** | `deidre@perfectketo.com` — Deidre Mares, Director of Partnerships (their press-room page) + `hello@perfectketo.com` | CEO Anthony Gustin (press/LinkedIn) | ✅ usable |
| **Carb Manager** | `support@carbmanager.com` (their help/contact docs) | CEO **Jessie Q.** (RocketReach=aggregator → candidate-H only; LinkedIn `in/jessie-qi-28397923` verified real) | ✅ support route; DM for exec |
| **HVMN / Ketone-IQ** | Rebranded **Ketone-IQ** (ketone.com) — "LETSGO" direct-contact button on team page | Co-founder/Exec-Chairman Geoffrey Woo (`in/gwoo`), CEO Michael Brandt (`in/mbrandt` — confirm before firing) | ✅ contact-button route; DM for execs |
| **Bulletproof** | `care@bulletproof.com` (contact page: bulletproof.com/contact — live 2026-09-03) | CEO/press — bulletproof exec team (DM; name verify Phase 2) | ✅ fireable support |
| **KetoLogic** | `customersupport@ketologic.com` (homepage HTML, live 2026-09-03; **/contact 404s**) | CEO (DM; name verify Phase 2) | ✅ fireable support |
| **Ketoned Bodies** | ⚠️ **FLAG** — ketonedbodies.com now serves gambling spam ("Situs Slot Gacor… Taipa88", 14 spam-term hits vs 4 keto remnants, 2026-09-03). **Company site dead/repurposed — lead likely invalid; needs re-check or drop.** | — | 🚩 invalid (verify/drop) |
| **KetoneAid** | `support@ketoneaid.com` (homepage, live 2026-09-03) | Founder (DM; name verify Phase 2) | ✅ fireable support |
| **Adapt Your Life** | Contact form only: adaptyourlifeacademy.com/contact/ (live) + LinkedIn company (in/company/adaptyourlife) | Founder **Dr. Dominic D'Agostino** (DM; name/link verify Phase 2) | ✅ form + DM |

### fusebot.ai (AI-agent / automation)
| NEW Lead | Contact route | DM candidate (LinkedIn) | Status |
|---|---|---|---|
| **Retool** | `david@retool.com` — founded/CEO David Hsu literally posted "email me at david AT retool.com" (his own HN comment; real source) + personal site `d@davidh.su` | David Hsu (`in/` verify Phase 2) | ✅ fireable (published by the person) |
| **Gumloop** | `max@gumloop.com` — CEO Max Brodeur-Urbas literally "please email me at max@gumloop.com" (their own handbook page) | Max Brodeur-Urbas | ✅ fireable |
| **Bardeen** | `support@bardeen.ai` (bardeen.ai/contact — live 200, scraped) | CEO (DM; name verify Phase 2) | ✅ fireable support |
| **Voiceflow** | Implied only: CEO Braden Ream's LinkedIn literally says "Get in touch: Braden at Voiceflow.com" → `braden@voiceflow.com` is **format-inferred, not a literal full string** → **candidate-H / owner judgment** | Braden Ream (`in/bradenream` verified real) | 🟡 candidate-H (never-invent) |
| **Botpress** | No published email — contact page is form/demo only; GitHub (`github.com/botpress/botpress`) + community | CEO (DM; name verify Phase 2) | 🟡 form + DM |
| **Activepieces** | No published email — homepage links GitHub + Discord community only | Founder (DM; name verify Phase 2) | 🟡 community + DM |
| **Leapwork** | No published email — contact page form-only (browser-rendered; support portal login) | CEO (DM; name verify Phase 2) | 🟡 form + DM |

### weputt.com (golf tech)
| NEW Lead | Contact route | DM candidate (LinkedIn) | Status |
|---|---|---|---|
| **Foresight Sports** | `sales@foresightsports.com` (support/contact page) + media `Mark.Buntz@revelyst.com` (their contact page) | CEO/CMO (DM) | ✅ fireable |
| **TrackMan** | `sales@trackmangolf.com`, `marketing@trackman.com` (their contact page) | CEO Klaus Eldrup-Jørgensen (co-founder; `klaus@trackman.com` = **guess, NOT fireable** → DM) | ✅ fireable sales routes |
| **Toptracer** | `info@toptracer.com` (toptracer.com/contact — live, scraped) | Head of Product (DM) | ✅ fireable |
| **Blast Motion** | `support@blastmotion.com` (blastmotion.com/about/contact-us-sales/ — browser-rendered live 2026-09-03; curl was Cloudflare-blocked) | CEO/Founder (DM; note: homepage email `arek.zalewski@winreality.com` = web-agency credit, **NOT** company contact — excluded) | ✅ fireable |
| **SwingU** | `support@swingu.com` (homepage — live, scraped; **/contact 404s** on Framer site) | CEO/Founder (DM) | ✅ fireable |
| **IZZO Golf** | `sales@izzo.com` (izzogolf.com homepage — live, scraped; note domain-root email @izzo.com) | CEO/CMO (DM) | ✅ fireable |

### paretobuddy.com (productivity)
| NEW Lead | Contact route | DM candidate (LinkedIn) | Status |
|---|---|---|---|
| **Sunsama** | `support@sunsama.com` (homepage — published) | Co-founder/CEO Ashutosh Priyadarshy (YC W19; `in/ashutoshpriyadarshy` verified), CPO Travis Meyer | ✅ fireable support |
| **Rize** | `info@rize.io` (rize.io/contact — live, scraped) | Founder (DM) | ✅ fireable |
| **Toggl** | `support@hire.toggl.com` (toggl.com/contact — live, scraped) | CEO Suhas Chormale (DM) | ✅ fireable support |
| **TickTick** | `support@ticktick.com` (help.ticktick.com — live, scraped) | Product lead (DM; TickTick = Appest/overseas) | ✅ fireable |
| **Any.do** | `customers@any.do` (any.do homepage — live, scraped) | CEO/CMO (DM) | ✅ fireable |
| **Routine** | ⚠️ **FLAG** — getroutine.com serves a 114-byte placeholder (200 OK, empty) → **site dead/abandoned; lead likely invalid** | — | 🚩 invalid (verify/drop) |

---

## Part C — Coverage Flags (what the lead asked: which NEW leads already have usable contact paths vs need deeper work)

**curebyketo.com — 8 NEW: 7 usable (5 fireable emails + LETSGO button + support routes), 1 🚩 flagged** (Ketoned Bodies — domain now gambling spam).
**fusebot.ai — 7 NEW: 3 fireable (Retool/Gumloop/Bardeen) + 2 form/DM (Botpress, Leapwork) + 1 community/DM (Activepieces) + 1 🟡 candidate-H (Voiceflow implied-email — owner judgment).**
**weputt.com — 6 NEW: 6 usable (all fireable sales/support emails).**
**paretobuddy.com — 6 NEW: 5 usable (all fireable) + 1 🚩 flagged** (Routine — dead placeholder site).

### Deep-work needed (Phase 2 candidates)
1. **Ketoned Bodies** — re-verify company existence/brand; if the domain has been repurposed, drop the lead (never fire against a dead/spam domain).
2. **Routine** — same treatment (placeholder site).
3. **Exec-level DM names/LinkedIn slugs** for: Bulletproof exec, KetoLogic CEO, KetoneAid founder, Adapt Your Life (Dr D'Agostino), Botpress CEO, Activepieces founder, Leapwork CEO, Voiceflow (pending owner call on implied email), IZZO, SwingU, Rize, Any.do — flagged "name verify Phase 2" (never-invent; I deliberately did NOT fabricate slugs I couldn't verify this session).
4. **Voiceflow** — decision needed: does "Get in touch: Braden at Voiceflow.com" (their own LinkedIn, published by the exec) count as fireable intent? Recommended: treat as fireable-with-format-caution or LinkedIn-DM — owner/lead judgment.

---

## Part D — Honest Constraints
- **No emails composed, none sent.** Research only — all firing decisions remain with lead/owner (same as first 3 sends 2026-09-03).
- Fireable emails above = **literally published on the company's own live page** (URLs verified 2026-09-03 via curl or agent-browser). Candidate-H rows = aggregator/pattern sources ONLY — flagged, never fireable.
- Web-search quota was capped this session (~50 results); all deep-linking done via direct curl/browser page scrapes (no quota) on official /contact|/about|home pages.
- Klook/Viator/Roadster remain "live but bot-walled" — bot protection (DataDome/Cloudflare) prevents content-level verification in this environment; the browser confirmed the sites load but present CAPTCHA/challenge. Not a dead-site finding.
- Machine-term flakes this session (terminal echo lags) resolved via fresh sessions; browser closed after use.

## References
- Scale report: `docs/OUTBOUND-SCALE-15DOMAINS_2026-08-30.md` (WAF flags §constraints); contact list `docs/CONTACT-RESEARCH-LIST_15DOMAINS_2026-08-30.md`
- Pilot: `docs/OUTBOUND-PILOT_8DOMAINS_2026-08-30.md`
- Prior exec-contact research: `EXEC-CONTACT-RESEARCH_2026-08-31.md`, `EXEC-CONTACT-RESEARCH-2ND_2026-08-30.md`