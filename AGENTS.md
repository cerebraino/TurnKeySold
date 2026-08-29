# AGENTS.md — for LLM agents connected to this repo

> **Mandatory first read:** **`REPO_INDEX.md`**
> Before doing any work against this repo (research, outreach, edits, audits), read `REPO_INDEX.md` in full. It maps every asset, the per-domain structure, the coverage tracker, content policies, and includes a hands-on **LLM Usage Playbook (§9)**.

**Quick orientation:**
- **Domains:** `DOMAINS/<domain>/` with `01-research/` (leads, contact sheets) + `02-outreach/` (briefs, email packs, micro-messages). Domain names are lowercase with TLD (e.g. `topsex.ai`).
- **Coverage truth:** `ASSET_AUDIT_2026-08-14.md` — read it for live numbers, don't re-derive.
- **Buyer contact gaps:** `docs/MISSING-CONTACT_2026-08-20.md` — the canonical owner follow-up list. **Never invent contacts** not H-verified there or in the contact sheets.
- **Outreach rules (non-negotiable):** pricing-free, no "I own", no links in first-touch, email bodies <100 words, no invented emails.

**Git discipline (shared clone at `/home/team/shared/repo-review`):**
- Branch fresh from `origin/main`; the lead holds push credentials — if `git push` prompts for a username, commit locally and notify the lead.
- Check `git branch --show-current` before committing (multiple agents share this clone).
- Land work via PR, not direct pushes to `main`.
