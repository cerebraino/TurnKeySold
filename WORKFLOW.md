
## REPO_INDEX Maintenance (owner directive 2026-09-21 — STANDING RULE)
Every PR that adds, moves, renames, or materially changes repo artifacts MUST include the matching `REPO_INDEX.md` update in the same PR:
- **Quick Reference row** for any new asset type or notable asset (location + status + provenance flags).
- **§10 wave-log entry** (one line, PR number + what landed) for every merged wave.
- **§6 Data Files / §2 Directory Map** when new root files or directories appear.
- **§8 Future Work** when the wave creates pending items (owner confirmations, next builds).
The lead verifies index completeness at review time; an artifact PR without its index update gets sent back. Stale pointers (main-at-PR numbers, "pending merge" on merged PRs) are treated as review-blocking drift.
