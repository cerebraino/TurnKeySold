# RESEARCH PROMPT — Fill Missing Executive Contact Information
**For:** Owner's research agent (external, has web browsing + lookup tools)
**Purpose:** Obtain verified contact details for named executives so TurnKeySold can send outreach to the right decision-makers.
**Companion doc:** `MISSING-CONTACT_2026-08-20.md` (the master list this prompt resolves).

---

## YOUR TASK

I am researching named executives as part of a B2B outbound-sales operation. For each executive below I need **verified, traceable contact information** — a direct work email and/or a personal LinkedIn URL — plus confirmation of their **current title**. Nothing may be invented or guessed. Where you cannot verify a detail, say so explicitly (label it `MISSING`), do not fabricate it.

**Hard rules (non-negotiable):**
1. **Never invent an email or LinkedIn URL.** A "probable" address (e.g. `first.last@company.com` guessed from the domain) is NOT a verified contact — label it `FORMAT-INFERRED`, never present it as real.
2. **Only two confidence labels:**
   - `H` = published on an official source I can see (company website, official press release, official social/YouTube/LinkedIn company page, credible news outlet, SEC/registry filings, the exec's own verified LinkedIn). Give me the exact URL where you saw it.
   - `MISSING` = could not verify. (Treat anything format-inferred as MISSING unless you confirm it against a second independent source.)
3. **Confirm current title** as of 2026 — many CEOs/founders change roles. If the title is uncertain, say "as of <date/source>, <title>".
4. Prefer the **official company source** over aggregator sites. If you use an aggregator (LinkedIn is fine), note it.
5. **Output only what you actually found.** One verified email per exec is enough; two is better (office + direct if published). A personal LinkedIn is extremely valuable — often more valuable than a generic `info@`.

## OUTPUT FORMAT

Return a table with one row per executive, exactly these columns (or a CSV with this header):

```
# | Domain | Company | Executive | Current Title | Email (verified) | Email Source URL | LinkedIn (personal) | LinkedIn Source URL | Confidence (H/MISSING) | Notes
```

Fill every cell. If something is missing, write `MISSING`. For each `H` row, the source URL must be present and reproducible.

---

## PRIORITY 1 — the FIVE most important (do these first, they unblock live campaigns)

| # | Domain | Company | Executive | What to find |
|---|--------|---------|-----------|--------------|
| 1 | NoBreak.ai | NoBreak Security (nobreak.ca) | **Yuval Olsha** (Founder) | Direct email + personal LinkedIn. (Their site only publishes `admin@nobreak.ca`.) |
| 2 | HipotecaHispana.com | Supreme Lending / Supreme CASA (supremelending.com) | **CEO** (name unknown — identify) | CEO name + direct email + LinkedIn. (Site is WAF-blocked for crawlers; try news, press releases, LinkedIn.) |
| 3 | LatinoMedico.com | Zócalo Health (zocalo.health) | **Erik Cardenas** (Co-founder & CEO) | Personal LinkedIn + direct email. (Site publishes `hello@zocalo.health`.) |
| 4 | PayCar.ai / automovil.ai | Kavak / Kavak Crédito (kavak.com) | **Carlos García Ottati** (CEO/Founder) | Personal LinkedIn + any public/PR email. (kavak.com is WAF-blocked; try news, LinkedIn, press.) |
| 5 | KnowLaw.ai | KnowLaw AI (knowlawai.com) | **founder** (name unknown — identify) | Founder name + email + LinkedIn. (Site is live but publishes no contact info.) |

## PRIORITY 2 — rest of the Tier-1/Wave-1 buyers

| # | Domain | Company | Executive | What to find |
|---|--------|---------|-----------|--------------|
| 6 | NoBreak.ai | Veeam | **Anand Eswaran** (CEO) | Media/public email + personal LinkedIn (company LI: linkedin.com/company/veeam-software). |
| 7 | NoBreak.ai | Datadog | **Olivier Pomel** (CEO) | Exec email + personal LinkedIn (company LI: linkedin.com/company/datadog). |
| 8 | NoBreak.ai / NoFail.ai | PagerDuty | **Jennifer Tejada** (CEO) | Exec direct email (only `sales@pagerduty.com` found so far) + personal LinkedIn. |
| 9 | NoFail.ai | Sazabi | **founder** (name unknown — identify) | Founder name + email + personal LinkedIn (company LI: linkedin.com/company/sazabi). |
| 10 | NoFail.ai | Braintrust | **Ankur Goyal** (CEO) | Personal LinkedIn (site publishes `hello@braintrust.dev`). |
| 11 | NoFail.ai | InsightFinder | **CEO** (name unknown — identify) | CEO name + email + personal LinkedIn (company LI: linkedin.com/company/insightfinder-inc). |
| 12 | NoFail.ai | Groundcover | **CEO** (name unknown — identify) | CEO name + email (company LI: linkedin.com/company/groundcover-com). |
| 13 | NoFail.ai | CodeRabbit | **CEO** (name unknown — identify) | CEO name + personal LinkedIn (site publishes pr@ and support@coderabbit.ai). |
| 14 | HipotecaHispana.com | Movement Mortgage | **CEO** (name unknown — identify) | CEO name + email (site publishes press@ and servicing@movement.com). |
| 15 | LatinoMedico.com | Tú TeleDoc | **Jeremy Roberts** (CEO/Founder) | Exec email + LinkedIn (site was returning 503 — verify it's live, then find his contact). |
| 16 | LatinoMedico.com | MiSalud Health | **CEO** (name unknown — identify) | CEO name + email (company LI: linkedin.com/company/misaludhealth). |
| 17 | OneGuy.org | Taskade | **John Xie** (Co-founder & CEO) | Confirm his direct email — is `john@taskade.com` the right one? (personal LI: linkedin.com/in/johnxie is already found). |
| 18 | OneGuy.org | Founder Institute | **Adeo Ressi** (CEO) | Confirm current title + his preferred founder email (site publishes regional@fi.co; LI: linkedin.com/in/adeoressi). |
| 19 | OneGuy.org | OPC.community | **CEO/founder** (name unknown — identify) | Founder name + direct email (site publishes support@opc.community). |
| 20 | PayCar.ai | Nexu | **CEO** (name unknown — identify) | CEO name + direct email (site publishes info@nexu.mx). |
| 21 | PayCar.ai / Automovil.ai | Ever (evercars.com) | **CEO** (name unknown — identify) | CEO name + personal LinkedIn (site publishes contact@ and press@evercars.com). |
| 22 | Automovil.ai / Automoviles.ai | Cafler | **CEO** (name unknown — identify) | CEO name + direct email (site publishes soporte@cafler.com — Spanish support; prefer the exec's direct). |
| 23 | KnowLaw.ai | KnowLaw.in | **founder** (name unknown — identify) | Founder name + email + LinkedIn (secondary/opportunistic target). |

## PRIORITY 3 — remaining outstanding exec contacts, by domain

For each domain below, find the listed executives' **current title + verified email + personal LinkedIn** (same rules as above). The company name is given; identify the exec where one is not named.

- **latinomedico.com** (digital-health vertical): Zocdoc (Oliver Kharraz), Doctoralia (Mariusz Gralewski), UnitedHealth/Optum (Andrew Witty), Healthgrades (Rob Draughon), Kaiser Permanente (Greg Adams), Centene (Sarah London), Molina Healthcare (Joseph Zubretsky), HCA Healthcare (Sam Hazen), Oak Street Health (Mike Pykosz), Teladoc (Chuck Divita).
- **putero.ai / puticlub.ai / puticlub.online** (adult-industry vertical): Aylo (Feras Antoon — verify whether any published email exists; if not, say MISSING), Stripchat, Chaturbate, WGCZ/xvideos, AdultTime — founder/CEO contacts. NOTE: these are private companies that publish little; realistic expectation is company/PR emails or LinkedIn only.
- **tipsketo.com** (keto vertical): Wholesome Yum (Maya Krampf), Diet Doctor (Andreas Eenfeldt), Carb Manager (David Jackson), Ruled.Me (Craig Clarke), KetoConnect (Matt & Megha), Perfect Keto (Anthony Gustin), Trifecta (Greg Connolly).
- **coldbeerportfolio** (beer vertical): AB InBev (Michel Doukeris), Constellation Brands (Bill Newlands), Heineken (Dolf van den Brink), Molson Coors (Gavin Hattersley).
- **automoviles.ai** (car-marketplace vertical): Mercado Libre (Marcos Galperin), OLX Autos, Kavak (Carlos García Ottati — may already be found in Priority 1 #4), Carro, InstaCarro (Diego Fischer), Coches.net, Autocosmos, DeMotores, NeoAuto, Claro.
- **rentapersona.com** (caregiver/help vertical): Care.com (Brad Wilson), Cuideo (Roberto Valdés), Cronoshare, TaskRabbit (Ania Smith), Superprof (Wilfried Granier), Zaask, Mil Anuncios, Pawshake.
- **roiexa.com** (marketing/AI vertical): HubSpot (Yamini Rangan), Salesforce (Marc Benioff), Ahrefs (Dmytro Gerasymenko), SEMrush (Oleg Shchegolev), Datadog (Olivier Pomel — may already be found in Priority 2 #7), Mixpanel (Amir Movafaghi), Amplitude (Spenser Skates), Heap.
- **topaiguys.com** (AI-tools vertical): FutureTools (Matt Wolfe), There's An AI For That, AI Tool Hunt, Toolify.ai, Ben's Bites (Ben Tossell), The Rundown AI, Superhuman AI.

---

## HOW TO VERIFY (quick method)

1. **Search the exec name + company** on your search engine. Prefer results from the company domain, LinkedIn, and credible press.
2. **LinkedIn:** the exec's own profile (URL must look like `linkedin.com/in/<handle>`) is H for the LinkedIn field, and confirms current title. Company LinkedIn pages are H for the company, but do NOT give you the exec's personal contact.
3. **Email:** look for it literally published on the company site (contact page, about page, team page, press page, press release). A pattern-based guess is NOT verified — if you can't find it published, return `MISSING` (and note the company's email format if you confirmed it, e.g. "format is first.last@company.com per 2 sources", so we can use it with care later).
4. **Cross-check:** a good confidence boost is finding the same email on two independent official sources. One official source is acceptable for H.

## FINAL REPORT

When done, return:
1. The full results table (all rows, including MISSING ones).
2. A short "top successes" list: the 5–10 execs where you found the best verified direct contacts.
3. A "still MISSING" list: exactly what remains unverified, so I can decide whether to pursue alternatives (LinkedIn DM route, etc.).

If you need to go deeper on any single executive (e.g. you found their LinkedIn but no email), a LinkedIn profile alone is still valuable — report it as H for LinkedIn / MISSING for email.
