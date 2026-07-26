# TurnKeySold — Architecture Principles

**Version:** 1.0  
**Ratified:** July 2026  
**Authority:** Non-negotiable — all future repository changes must comply.  
**Amendments:** Require founder approval.

---

## P1 — Single Canonical Source

> The GitHub repository is the single permanent source of truth for all organizational knowledge.

- Nothing that represents organizational intelligence may exist only outside the repo.
- `/home/team/shared/` is an ephemeral workspace — a staging area, never a permanent home.
- Every knowledge artifact must have exactly one canonical location in the repo.
- When an artifact exists in both shared and repo, the repo copy is authoritative.

**Why:** The sandbox can be reset. Shared files were already lost once. The repo survives everything.

---

## P2 — Structured Over Narrative for Facts

> Facts that can be queried, compared, or cross-referenced must reside in structured data, not narrative prose.

- Domain names, values, DMPS scores, buyer companies, executive names, contact status — these are facts.
- Narrative markdown (leads files, briefs, expansions) should reference structured data, not duplicate it.
- Any question that begins with "which" or "how many" should be answerable without reading 130 files.

**Why:** An LLM reading one JSON file should answer "show me all buyers with DMPS > 90" — not 130 markdown files.

---

## P3 — Relationships Are First-Class Citizens

> Every relationship between domains, buyers, and contacts must be explicitly modeled.

- Bundles (Cold Beer 6 domains, Apuesto 7 domains) are relationships, not accidents of folder layout.
- Same-buyer links (AB InBev → Cold Beer AND apuesto) must be visible.
- A buyer identified for one domain should automatically surface for related domains.

**Why:** Our intelligence compounds when connections are visible, not hidden across 130 folders.

---

## P4 — Templates Over Examples

> Agents should receive templates with schemas, not examples to reverse-engineer.

- Every knowledge artifact type (lead list, brief, expansion, valuation) has a defined template.
- Templates enforce required fields, optional sections, and naming conventions.
- A new agent's instructions should say "use template X" — never "look at domain Y and do something similar."

**Why:** Consistency is the foundation of queryability. Inconsistent formats produce unqueryable data.

---

## P5 — Provenance Is Mandatory

> Every important knowledge artifact must record its origin, confidence, and review history.

- Who created this? When? From what sources? With what confidence?
- Has it been reviewed? By whom? When?
- What evidence supports it?

**Why:** Without provenance, we cannot distinguish verified intelligence from plausible-sounding speculation. This is how hallucinated domains entered our research.

---

## P6 — Naming Is Infrastructure

> File and folder names are part of the API that agents and LLMs use to navigate the repository.

- Names must be consistent, predictable, and machine-parseable.
- Domain folders: lowercase, dot-included (`topsex.ai`, not `TopSex.ai` or `topsexai`).
- Research files: `leads.md`, `valuation.md`, `expansion.md` (consistent across domains).
- Outreach files: `brief.md`, `messaging.md` (consistent across domains).
- Never: `leads_TopSex.ai.md` in one folder and `leads.md` in another.

**Why:** An LLM should be able to construct a file path programmatically: `domains/[name]/research/leads.md` — every time.

---

## P7 — Delete Is Safer Than Duplicate

> Two copies of the same information is riskier than one copy and a backup.

- Duplicate files (leads.md + leads_[Domain].md in the same folder) create ambiguity.
- Which one is authoritative? Which one was updated last? Which should an LLM read?
- When in doubt, keep one canonical copy and delete the rest.

**Why:** LLMs with finite context windows should not waste tokens on duplicate content.

---

## P8 — Backward Compatibility Through Git

> Every change must be independently revertible through Git.

- One commit per logical change (never batch deletions with additions).
- Descriptive commit messages that reference this document.
- Git tags at stable checkpoints (`v0.1-stable`, `v0.2-structured`).
- No change that cannot be undone with `git revert`.

**Why:** Architecture mistakes should cost one command, not hours of reconstruction.

---

## P9 — Knowledge Lifecycle Tracking

> Every artifact passes through defined stages, and its status is always knowable.

- Domain lifecycle: `unresearched → researched → briefed → outreach-ready → contacted → negotiating → sold`
- Buyer lifecycle: `identified → scored → messaged → contacted → responded → closed`
- Status must be machine-readable (YAML frontmatter or JSON), not buried in prose.

**Why:** "What should I work on today?" should be answerable by querying status, not by reading.

---

## P10 — Optimize for LLM Navigation

> The repository's primary consumers are AI agents. Human readability is secondary but never sacrificed.

- `README.md` is the LLM entry point — must describe structure, conventions, and key files.
- `.github/AGENTS.md` provides agent-specific instructions.
- `_indexes/` provide pre-computed cross-references that save LLMs from scanning.
- `_data/` provides structured, queryable facts in JSON format.
- Folder names and file names must be predictable enough for programmatic path construction.

**Why:** The company's intelligence compounds when agents can navigate autonomously, not when a human must guide them.

---

## Design Decisions Log

| Date | Decision | Principle | Rationale |
|---|---|---|---|
| 2026-07 | Repo as canonical source | P1 | Sandbox recovery lost files; repo survives |
| 2026-07 | Structured data layer | P2 | Queryability requires structure |
| 2026-07 | Templates over examples | P4 | Consistency enables automation |
| 2026-07 | Lowercase domain folders | P6 | Predictable path construction |
| 2026-07 | One commit per logical change | P8 | Reversible architecture decisions |

---

*These principles govern all future repository changes. Violations require either an amendment (founder approval) or a fix to comply.*
