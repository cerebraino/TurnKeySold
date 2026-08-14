# full_portfolio_ranked.csv — Methodology Note

**Built:** 2026-08-12 by domain-researcher (task 173d2bb9, owner request "FULL PORTFOLIO ranked CSV").
**Revised:** 2026-08-14 — fixed the 15 "not yet researched" rows whose leads files were missed by the original case-sensitive scan (uppercase filenames like leads_Puticlub.online.md / leads_Dalai.co.md, plus lowercase ones like leads_paycarai.com.md); filled buyer categories + top-3 companies in place from each domain's own leads file, and resolved automoviles.ai's value from its $5K–$20K appraisal range ($12,500 midpoint). Column 5 (micro-messages, architect's part 2) untouched.
**Source:** every domain dir under `DOMAINS/` in the repo (146 dirs = 145 domains + coldbeerportfolio bundle).
**Output:** `/home/team/shared/DOMAINS/CSV/full_portfolio_ranked.csv` — 5 columns, 146 data rows, ranked most → least valuable.

## Columns
1. **Domain** — folder name under `DOMAINS/`.
2. **Approx Defensible Market Value** — taken from each domain's existing 01-research appraisal/valuation, NOT a new appraisal. Priority of source: Genspark "Central (recommended)" > Asking Anchor > Anchor > Conservative mid > Optimistic mid > "Value range" mid > appraisal-table row > Final Score. Midpoint of any range is used. Labeled with the source tag (e.g. "(asking anchor $35,000-$45,000)"). **This is a defensible estimate, not a guaranteed sale price.** Every domain has a value except the coldbeerportfolio bundle (flagged "not yet researched" for categories/companies — genuinely no leads file).
3. **Main 3 Buyer Categories** — derived from the top-3 leads' intent signals in the domain's leads file (first segment of each intent cell, truncated). Where intent is absent, falls back to the top-3 company names.
4. **Top-3 Companies to Reach** — top 3 by DMPS from the domain's leads file (multiple leads files merged where present), with named exec where the leads file provides one.
5. **Sample Micro-Message** — Three-Line framework (their world → their stakes → the name that fits), no pricing, no links, Spanish where the market is Spanish-speaking. **Column 5 is the outreach-architect's deliverable (task 2a491f81, approved 2026-08-14)** — built from each domain's 02-outreach/micro-messages_*.md files and the top lead's intent signal; 146/146 filled. This column is owned by the architect; do not edit as part of research changes.

## Ranking methodology
- Primary key: the **defensible-value midpoint** extracted above, descending (most valuable first).
- Domains without a value estimate rank last, alphabetical.
- NOTE: `coldbeerportfolio` is a **portfolio bundle** (multiple beer domains) whose $350K anchor is a bundle-level figure — it ranks #1 but must not be read as a single-domain value.
- Company lists use DMPS (the team's Domain-Market-Prospect Score from the leads files); execs are named only where the leads file names them — no execs invented.

## Caveats
- Values are as-recorded in each domain's own research files (which use different appraisal styles: Genspark model, team anchor, comparables-based). The CSV does not re-appraise — it surfaces each domain's best existing estimate consistently.
- 145/146 domains have parsed top-3 companies + buyer categories from their own leads files (case-insensitive leads_* scan); only `coldbeerportfolio` (a bundle of beer domains, no leads file) is marked "not yet researched" — genuinely no-leads, flagged per the task rule rather than invented.
- Cross-referenced the owner doc `Domain_Buyer_Prospecting_Research_10_Domains.md`: its 10 domains (NoBreak, NoFail, Automovil, KnowLaw, PayCar, HipotecaHispana, HispanoAbogado, LatinoMedico, OneGuy, PossibleAGI) all already have leads files in the repo; their primary buyers are reflected in the CSV via those files.
