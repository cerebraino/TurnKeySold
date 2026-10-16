# TurnKeySold — Team Code Workflow

This document is the team's living reference for code delivery in this repo. The platform also maintains a separate shared `WORKFLOW.md` for linked-repo configuration — that one is not ours to edit.

## Branching & Delivery
- Members work on feature branches named `docs/<topic>` (documentation/research) or `feat/<topic>` (site/code).
- Members push their branch and open a PR via `finish_task`; the LEAD reviews and merges (squash). Members do not push `main` directly.
- Commit/PR messages state what landed and why — one paragraph minimum for wave PRs.

## Review Standards (lead checklist)
- **REPO_INDEX.md completeness (owner directive 2026-09-21 — STANDING RULE):** every PR that adds, moves, renames, or materially changes repo artifacts must include its `REPO_INDEX.md` update in the same PR — Quick Reference row for new/notable assets; §10 wave-log line for every merged wave; §6 Data Files / §2 Directory Map for new root files or directories; §8 Future Work for pending items the wave creates. An artifact PR without its index update is sent back. Stale pointers (main-at-PR numbers, "pending merge" on merged PRs) are review-blocking drift.
- **Never-invent:** every factual claim traces to a published source or a file already in the repo; contacts are fireable only if literally published.
- **SEND FREEZE (owner directive 2026-09-04):** no sends of any kind — all outreach artifacts are ready-copy only.
- **Multi-contact principle (owner directive 2026-09-21):** multiple contacts at the same company are parallel outreach targets (verify each person's current role independently), never treated as conflicts.
- **Full-field ingest standard (owner directive 2026-09-21):** external research is integrated by reading the SOURCE FILE field-by-field (never from a summary/digest); every provided column is carried into the workbench with provenance flags.

## File Placement
- Lead lists + messages live in BOTH `/home/team/shared` AND the repo — pattern: `DOMAINS/<domain>/01-research/` + `02-outreach/` + `docs/outreach/`.
- Root-level canonical CSVs (`payauto_ai_acquisition_targets.csv`, `payquick_ai_acquisition_targets.csv`) are collaborator-research reference copies; annotated team workbenches live in the domain folders.
