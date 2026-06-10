# Agent instructions for the migration branch

This repository's `migration` branch is a Zensical compatibility track. It is
not the production source of truth.

## Branch responsibilities

- `main` is the only production and day-to-day content branch.
- `migration` periodically imports changes from `main` and validates them with
  Zensical.
- Never merge migration-only framework changes back into `main` unless the user
  explicitly requests a production migration.
- Never modify `.github/workflows/update.yml` while maintaining the migration
  track.
- Never deploy from `migration` or write generated files to `gh-pages`.
- Do not add `site/`, `.venv/`, `.zensical/`, or `.codex/` to Git.

## Refresh workflow

When asked to refresh or update the migration branch:

1. Confirm the current branch is `migration` and inspect the worktree.
2. Fetch the latest remote branches.
3. Merge `origin/main` into `migration`. Do not reset the branch, because the
   migration branch contains compatibility work that must be retained.
4. Resolve conflicts by preserving:
   - New content and general site changes from `main`.
   - The disabled custom `statistics` plugin in migration's `mkdocs.yml`.
   - Migration-only files: `AGENTS.md`, `ZENSICAL_MIGRATION.md`,
     `pyproject.toml`, `uv.lock`, `.github/workflows/zensical.yml`, and
     `scripts/validate_zensical_build.py`.
   - The MiniJinja-compatible `docs/overrides/main.html`.
5. Update the pinned Zensical version only when explicitly requested or when
   evaluating a new Zensical release. Regenerate `uv.lock` after version changes.
6. Run:

   ```sh
   uv sync --locked
   uv run zensical build --clean
   uv run python scripts/validate_zensical_build.py
   ```

7. Inspect representative generated pages and update `ZENSICAL_MIGRATION.md`
   when compatibility findings change.
8. Verify `.github/workflows/update.yml` is unchanged and generated files remain
   ignored before committing.

## Production blockers

Do not recommend replacing the production MkDocs deployment until all blockers
listed in `ZENSICAL_MIGRATION.md` pass. In particular, real Git authors and
dates, tag listings, and generated word-count statistics must work. Do not
replace missing values with static or fabricated data.
