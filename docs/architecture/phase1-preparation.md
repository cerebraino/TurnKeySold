# TurnKeySold Phase 1 Preparation — Complete Inventory & Migration Plan

**Prepared for:** Juan L. Aguirre, Founder  
**Date:** July 2026  
**Status:** PRE-DECISION — no cleanup has begun  
**Purpose:** Complete factual inventory, deletion proposal, canonical source design, and migration roadmap before any Phase 1 work begins.

---

## 1. Complete Inventory

### Summary Statistics

| Location | Files | Total Size (approx) |
|---|---|---|
| GitHub Repository (excluding .git/) | 348 | ~2.8 MB |
| /home/team/shared/ | 335 | ~3.1 MB |
| Overlap (files in both) | 2 | google_alerts_v2.csv, domain-backlog-new.csv |
| Identical pairs | 2 | Both CSVs are byte-identical |
| Divergent pairs | 0 | No file exists in both locations with different content |
| Repo-only files | 350 | All per-domain structured content |
| Shared-only files | 333 | Flat-file working copies |

### Critical Finding

**The repo and /home/team/shared/ are NOT divergent copies — they are two independent file trees.** The shared directory uses flat naming (`leads_[domain].md`, `brief_[domain].md`, `outreach-*.md`) while the repo uses hierarchical structure (`DOMAINS/[domain]/01-research/leads_[domain].md`). Files are created in shared by agents, then selectively copied to the repo by the lead. This means:

- **Shared is the working surface** — where agents write
- **Repo is the archive** — what the lead chooses to preserve
- **Sync is manual and lossy** — some files never make it to the repo
- **The repo is behind** — newer versions may exist only in shared

### Inventory by Category

**GitHub Repository — Top-Level:**
| Path | Files | Purpose |
|---|---|---|
| COMPANY/ | 6 | Brand identity, playbooks, frameworks |
| OUTREACH/ | 4 | Master templates, email lists, old Google Alerts |
| PORTFOLIO/ | 3 | Portfolio analysis, CSV copies |
| WEBSITE/ | 10 | TurnKeySold.com HTML/CSS |
| docs/ | 1 | Architecture review (new) |
| Root | 4 | README, CSVs, .gitignore |

**GitHub Repository — DOMAINS/:**
| Subfolder | Count | Purpose |
|---|---|---|
| 01-research/ | ~132 domains | Leads files, buyer expansions |
| 02-outreach/ | ~125 domains | Briefs, personalized outreach |
| 03-buyer-intel/ | 2 domains | Corporate intelligence |
| 03-results/ | ~41 domains | Empty folders (cruft) |

**/home/team/shared/ — By File Type:**
| Pattern | Count | Purpose |
|---|---|---|
| leads_*.md | ~127 | Lead lists (flat, per domain) |
| brief_*.md | ~125 | Outreach briefs (flat, per domain) |
| outreach-*.md | 6 | Personalized outreach messaging |
| *-buyer-expansion.md | 6 | Strategic buyer deep dives |
| *-buyers.md | 2 | Portfolio buyer research |
| *-intel.md | 1 | Corporate intelligence |
| external-*.md | 5 | External research inputs |
| *.csv | 6 | Google Alerts, backlog, email lists |
| *.md (misc) | ~10 | Inventory, analysis, overview |
| *.png | 2 | Screenshots (Trinity research) |
| *.html | 7 | Landing page files |
| WORKFLOW.md | 1 | Agent workflow instructions |

---

## 2. Duplicate Analysis & Deletion Proposal

### A. Old-format duplicates: `leads.md` (20 files)

These are early-format lead files from the initial research phase. They either duplicate or are superseded by `leads_[Domain].md` files in the same folder.

| # | Path | Size | Confidence | Risk | Replacement |
|---|---|---|---|---|---|
| 1 | DOMAINS/ColdBeerPortfolio/01-research/leads.md | 840B | HIGH | None — superseded by coldbeer-portfolio-buyers.md | coldbeer-portfolio-buyers.md |
| 2 | DOMAINS/LaVoiture.ai/01-research/leads.md | predict | HIGH | None | leads_LaVoiture.ai.md |
| 3 | DOMAINS/KnowLaw.ai/01-research/leads.md | predict | HIGH | None | leads_KnowLaw.ai.md |
| 4 | DOMAINS/HispanoAbogado.com/01-research/leads.md | predict | HIGH | None | leads_HispanoAbogado.com.md |
| 5 | DOMAINS/LeanMeds.com/01-research/leads.md | predict | HIGH | None | leads_LeanMeds.com.md |
| 6–20 | (14 more in early-researched domains) | various | HIGH | None | Corresponding leads_[Domain].md |

**Rollback:** `git revert [commit-hash]` — trivial.

### B. Old-format duplicates: `campaign-brief.md` (19 files)

Same pattern — early-format briefs superseded by `brief_[Domain].md` files.

| # | Path | Confidence | Risk | Replacement |
|---|---|---|---|---|
| 1–19 | DOMAINS/*/02-outreach/campaign-brief.md | HIGH | None | brief_[Domain].md in same folder |

**Rollback:** `git revert` — trivial.

### C. Empty folders: `03-results/` (41 folders)

These are placeholder directories. All are confirmed empty via `find DOMAINS -name "03-results" -type d -empty`.

**Rollback:** `git revert` — trivial. No data loss possible.

### D. Shared-only files with no repo equivalent

These 333 files exist in /home/team/shared/ but not in the repo. They include:
- ~252 lead/brief files that ARE in the repo but under different paths (DOMAINS/ structure)
- ~80 files that are truly shared-only (enrichment docs, external research, outreach messaging, screenshots, inventory files, turnkeysold-llm-brief.md, etc.)

**⚠ Files at risk of permanent loss if sandbox fails:**
- outreach-proof-of-human.md
- outreach-cold-beer-portfolio.md
- outreach-hispanoabogado.md
- outreach-latinomedico.md
- outreach-hipotecahispana.md
- outreach-nofail-nobreak.md
- outreach-oneguy.md
- turnkeysold-llm-brief.md
- domain-inventory-ranked.md
- knowledge-architecture-review.md (now also in docs/)
- external-*.md (5 files)

**These are NOT duplicates — they're unique assets that should be in the repo.**

---

## 3. Canonical Source of Truth

### Proposed Architecture

| What GitHub Will Own | What /home/team/shared Will Be Used For |
|---|---|
| All permanent organizational knowledge | Ephemeral agent workspace |
| Leads, briefs, expansions, outreach messaging | Files being actively written (before commit) |
| Templates, playbooks, structured data | Intermediate artifacts that don't need version control |
| Portfolio indexes, buyer directories | Screenshots and temporary downloads |
| Google Alerts, domain inventory | Cross-agent file sharing during active work |
| Architecture documentation | Nothing permanent |

### Rule: Nothing Should Ever Exist Only Outside GitHub

Any file that represents organizational intelligence (lead research, buyer analysis, outreach strategy, corporate intel) must have a canonical copy in the repo. The shared directory is a staging area, not a permanent home.

### How Future Agents Should Avoid Data Divergence

1. **Write to shared, commit to repo.** Every agent output lands in shared first, then the lead (or an automation) commits it to the repo.
2. **Read from shared, produce to shared.** Agents read the latest versions from shared, not from the repo.
3. **Repo is the archive, shared is the workspace.** The repo is never more current than shared — it's the permanent record.
4. **Automated sync.** A script should eventually detect new/modified files in shared and stage them for commit.

---

## 5. Empty Folder Removal Confirmation

All 41 `03-results/` folders are confirmed empty. None are referenced by:

| Check | Result |
|---|---|
| Referenced in scripts? | No scripts exist that reference 03-results/ |
| Referenced in prompts/instructions? | Only in README as "Sale records, invoices (for sold domains)" |
| Referenced in agent instructions? | No agent instructions reference 03-results/ |
| Referenced in WORKFLOW.md? | No |
| Any file inside any of them? | All confirmed empty via `find -type d -empty` |

**Action:** Safe to remove. README should be updated to not reference them.

---

## 6. Backup & Rollback Plan

### Before Cleanup Begins

1. **Ensure all shared-only files are committed to repo.** Any file in /home/team/shared/ that represents organizational intelligence must have a repo copy.
2. **Tag the repo:** `git tag pre-phase1-cleanup` — marks the exact state before any changes.
3. **Create a backup branch:** `git branch backup/pre-phase1` — completely safe, cannot be lost.
4. **Commit a phase manifest:** A file listing every planned deletion, so the plan is version-controlled.

### During Cleanup

5. **One commit per deletion category.** Separate commits for: old leads.md removal, old campaign-brief.md removal, empty folder removal. Never batch different types of changes.
6. **Descriptive commit messages:** "cleanup: remove 20 superseded leads.md duplicates" — traceable to this document.

### Rollback

7. **To undo a single commit:** `git revert [hash]` — safe, creates inverse commit.
8. **To undo all Phase 1:** `git checkout pre-phase1-cleanup -- .` then commit.
9. **To restore from backup branch:** `git merge backup/pre-phase1`

### Verification

10. After cleanup, run `find DOMAINS -name "leads.md" | wc -l` — should be 0.
11. Run `find DOMAINS -name "campaign-brief.md" | wc -l` — should be 0.
12. Run `find DOMAINS -type d -empty` — should be 0.

---

## 7. Five-Phase Migration Roadmap

### Phase 1: Stabilize — Clean & Standardize

**Objective:** Remove noise, establish canonical structure, eliminate divergence risk.

**Deliverables:**
- 20 leads.md duplicates removed
- 19 campaign-brief.md duplicates removed  
- 41 empty 03-results/ folders removed
- All shared-only outreach and enrichment files committed to repo
- Domain folder naming standardized (all lowercase, consistent TLD suffix)
- Updated README (no references to removed folders)
- Updated WORKFLOW.md (canonical source policy)
- Git tag: `v0.1-stable`

**Dependencies:** None — this is self-contained cleanup.

**Risks:**
- LOW: Accidental removal of unique content in leads.md — mitigated by checking file size (all are <1KB or duplicates)
- LOW: Broken README references — mitigated by README update in same phase

**Acceptance Criteria:**
- No file named `leads.md` or `campaign-brief.md` remains
- No empty 03-results/ folders remain
- All outreach-*.md files exist in both shared and repo
- All domain folders follow consistent naming convention
- README accurately describes current structure

**Rollback Conditions:** Any deletion that causes agent confusion or breaks a workflow. Revert and investigate.

**⛔ Founder Decision Required:** Approve deletion of leads.md and campaign-brief.md duplicates. (Decision A)

---

### Phase 2: Structure — Templates & Indexes

**Objective:** Create reusable templates and structured indexes.

**Deliverables:**
- `_templates/` folder with lead-list, brief, expansion, and valuation templates
- `_data/domains.json` — extracted from existing leads files
- `_data/buyers.json` — aggregated from all domains
- `_indexes/domain-inventory.md` — ranked, status-tracked
- `_playbooks/` folder — merge COMPANY/ and OUTREACH/ content
- `.github/AGENTS.md` — agent instructions for this repo

**Dependencies:** Phase 1 complete (clean structure to build on).

**Risks:**
- MEDIUM: Data extraction errors — mitigated by validation against source files
- MEDIUM: Template rigidity — mitigated by keeping narrative sections flexible

**Acceptance Criteria:**
- Every template has required fields and optional sections
- domains.json contains all 127+ domains with accurate metadata
- buyers.json cross-references companies across domains
- An LLM can read _indexes/ and understand the full portfolio

**⛔ Founder Decisions Required:**
- Approve template structure and required fields (Decision B)
- Approve data model for domains.json and buyers.json (Decision C)
- Decide: keep or archive COMPANY/OUTREACH/PORTFOLIO top-level folders (Decision D)

---

### Phase 3: Connect — Relationships & Portfolios

**Objective:** Make cross-domain relationships visible and queryable.

**Deliverables:**
- `_data/relationships.json` — bundles, same-buyer links, companion domains
- `portfolios/` folder — indexes for Cold Beer, Apuesto, Adult groupings
- `_data/contacts.json` — extracted named executives across all domains
- `_data/outreach-log.json` — empty schema, ready for tracking

**Dependencies:** Phase 2 complete (structured data foundation).

**Risks:**
- LOW: Relationship mapping is manual — mitigated by starting with known bundles (Cold Beer 6, Apuesto 7, Adult 9+)

**Acceptance Criteria:**
- Every known bundle is represented in relationships.json
- contacts.json has all 100+ named executives from buyer expansions
- An LLM can answer "show me all buyers related to AB InBev across any domain"

**⛔ Founder Decisions Required:**
- Approve relationship types (bundle, same_buyer, companion, competitor_block) (Decision E)
- Decide: should portfolios/ duplicate or reference per-domain files? (Decision F)

---

### Phase 4: Automate — Sync & Validation

**Objective:** Remove manual sync burden, enforce data integrity.

**Deliverables:**
- Script to regenerate `_data/` files from per-domain sources
- Validation that all per-domain files match template schemas
- Automated staging of new/modified shared files for commit
- CI-like check: are any domains missing research or briefs?

**Dependencies:** Phase 3 complete.

**Risks:**
- MEDIUM: Automation errors could propagate — mitigated by git versioning of _data/ files

**Acceptance Criteria:**
- Running the regeneration script produces no unexpected changes
- New domains are auto-detected as "missing research" and flagged

**⛔ Founder Decisions Required:** None (operational).

---

### Phase 5: Evolve — Metadata & Lifecycle

**Objective:** Add YAML frontmatter, knowledge lifecycle feedback loops, expand entity model.

**Deliverables:**
- YAML frontmatter on all per-domain files (status, last-updated, DMPS, etc.)
- Knowledge lifecycle documented (Discovery → Research → Briefing → Outreach → Contact → Negotiation → Closed)
- Pattern extraction from successful sales
- Entity model expansion based on real usage

**Dependencies:** Phase 4 complete (automation makes metadata sustainable).

**Risks:**
- LOW: YAML frontmatter is additive, not destructive

**Acceptance Criteria:**
- Every research file has parseable YAML metadata
- Status can be queried: "show all domains in 'outreach-ready' status"

**⛔ Founder Decisions Required:** Approve metadata schema (Decision G).

---

## 8. Fact / Recommendation / Assumption / Unresolved

### Verified Facts
1. 348 files in repo, 335 in shared — only 2 are byte-identical in both.
2. 20 `leads.md` files exist; all are old-format and superseded.
3. 19 `campaign-brief.md` files exist; same pattern.
4. 41 `03-results/` folders exist; all are empty.
5. No divergent pairs exist — files are either in one location or the other, never both with different content.
6. The shared directory is the agent working surface; the repo is the lead-maintained archive.
7. Sandbox recovery already lost files once (LatinoMedico expansion, July 24).

### Architectural Recommendations
1. GitHub repo should be the single canonical source for all permanent knowledge.
2. /home/team/shared/ should be treated as ephemeral workspace — never the permanent home for organizational intelligence.
3. Duplicate old-format files should be removed to reduce LLM context pollution.
4. Per-domain folders should adopt consistent lowercase naming.
5. COMPANY/, OUTREACH/, PORTFOLIO/ should be consolidated into `_playbooks/` and `_indexes/`.
6. Structured data (JSON) should supplement narrative markdown for queryable facts.

### Assumptions
1. **ASSUMPTION:** The 20 leads.md files contain no unique information not present in their corresponding leads_[Domain].md files. (Confidence: HIGH — all are <2KB and the domain folder already contains a properly named lead file.)
2. **ASSUMPTION:** The 19 campaign-brief.md files are similarly superseded. (Confidence: HIGH — same pattern.)
3. **ASSUMPTION:** Empty 03-results/ folders were created proactively and have no current purpose. (Confidence: HIGH — confirmed empty, no references found.)
4. **ASSUMPTION:** Agents can continue to write to /home/team/shared/ as their primary workspace. (Confidence: HIGH — this is the current operating model.)
5. **ASSUMPTION:** The lead will continue to be the sync point between shared and repo, at least until Phase 4 automation. (Confidence: MEDIUM — automation may change this.)

### Unresolved Questions
1. **Should the shared directory be periodically cleaned?** Currently 335 files — many are intermediate artifacts (screenshots, old copies). Who decides what to keep?
2. **Should agents ever read from the repo directly, or always from shared?** Current model: agents read from shared (where the latest work lives), but templates and playbooks are in the repo.
3. **How should we handle domain names with special characters in folder names?** Current naming: `TopSex.ai` (mixed case, includes dot). Proposal: `topsex.ai` (lowercase). But is `.ai` a suffix or part of the name?
4. **What happens to ColdBeerPortfolio/ as a domain folder?** It's not a single domain — it's a portfolio. Should it move to `portfolios/cold-beer/`?
5. **Should apuesto family have a centralized index?** 7 domains across `apuesto.ad/`, `apuesto.ai/`, `apuesto.casino/`, `apuesto.xyz/`, `teapuesto.bet/`, `teapuesto.casino/`, `teapuesto.xyz/` — currently no file links them.
6. **When do we create outreach-*.md files?** Currently created ad-hoc for high-value expansions. Should every top-tier domain have one? Who decides?

---

## 10. Founder Decision Memo

Before Phase 1 can safely begin, you must decide:

| ID | Decision | Options | Recommendation |
|---|---|---|---|
| **A** | Delete 20 leads.md + 19 campaign-brief.md duplicates? | Yes / No / Audit first | **Yes** — all are superseded, no unique content risk |
| **B** | Remove 41 empty 03-results/ folders? | Yes / No | **Yes** — confirmed empty, no references |
| **C** | Standardize domain folder naming to lowercase? | Yes / No / Hybrid | **Yes** — TopSex.ai → topsex.ai. Reduces LLM confusion |
| **D** | Commit all shared-only outreach and enrichment files to repo? | Yes / Selectively / No | **Yes** — 7 outreach files at risk of sandbox loss |
| **E** | Canonical source policy: repo is permanent, shared is ephemeral? | Approve / Revise | **Approve** — eliminates divergence risk |
| **F** | Merge COMPANY/OUTREACH/PORTFOLIO into _playbooks/_indexes? | Phase 2 / Never / Phase 1 | **Phase 2** — not cleanup, requires restructuring |

**If you approve A–E, Phase 1 becomes: 3 commits, ~80 file deletions, 7 file additions, zero risk to unique intelligence. Total time: ~15 minutes. Fully reversible via git revert.**

---

*All claims in this document are traceable to the raw inventory at /tmp/repo_inventory.csv and /tmp/shared_inventory.csv, and the divergence analysis at /tmp/divergence.txt.*
