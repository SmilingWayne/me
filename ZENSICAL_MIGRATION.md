# Zensical migration track

This branch is a compatibility track for Zensical. The production site continues
to build and deploy from `main` with MkDocs until every production gate below
passes.

## Current approach

- Keep `mkdocs.yml` as the only site configuration source. Zensical supports the
  existing format, and maintaining a second copy of the large navigation tree
  would create unnecessary drift.
- Pin Zensical and Python through `pyproject.toml` and `uv.lock`.
- Build all documents in CI and upload `site/` as a short-lived artifact.
- Follow `AGENTS.md` when an AI agent refreshes this branch from `main`.
- Do not deploy from this branch and do not write generated files to
  `gh-pages`.
- Keep the existing production workflow in `.github/workflows/update.yml`
  unchanged.

Local validation:

```sh
uv sync --locked
uv run zensical build --clean
```

## Compatibility matrix

| Capability | Current migration status | Production gate |
| --- | --- | --- |
| Full document build | Verified: 691 Markdown sources build successfully | Required |
| Representative existing URLs | Verified; complete URL diff still pending | Required |
| Classic Material theme and navigation | Verified in generated HTML | Required |
| Custom CSS and JavaScript | Verified in generated HTML | Required |
| MiniJinja template overrides | Verified after adjusting `main.html` | Required |
| Search | Verified: `site/search.json` is generated | Required |
| Tags | Blocked: tag page builds without tag listing data | Required |
| Mermaid, math, tables, code, admonitions | Verified in generated HTML | Required |
| Page source and commit-history links | Verified in generated HTML | Required |
| Git authors and contributors | Blocked: absent from generated pages | Required |
| Git creation and revision dates | Blocked: absent from generated pages | Required |
| Custom word-count statistics | Blocked: `{{words}}` remains in output | Required |
| Client-side visit counter | Verified: existing script is retained | Required |

## Known findings

The first Zensical 0.0.45 build processed the complete documentation tree but
failed on `docs/overrides/main.html` because MiniJinja does not allow
`{{ super() }}` outside a template block. The migration branch removes that
invalid call.

The build also reports existing unresolved-link warnings from Markdown content.
These warnings predate the migration and are recorded separately from framework
compatibility. They do not block a non-strict compatibility build.

After the MiniJinja fix, a complete Zensical 0.0.45 build finishes successfully
in about 13 seconds locally. It generates 695 HTML files for 691 Markdown
sources, including representative homepage, deep-navigation, tags, Mermaid, and
math pages. The build currently reports 278 existing unresolved-link issues.

The current build confirms that search, custom assets, theme palettes, visit
counting, and the custom source/history links are present. It also confirms that
tag listing data, Git authors, Git dates, and generated word counts are not yet
available, so this branch is not ready to replace production.

The custom `statistics` MkDocs plugin is intentionally disabled. Its observable
contract is:

- Pages opt in through `statistics: true` front matter.
- The plugin replaces `{{words}}` in page content with a generated word count.
- The homepage currently exposes that value in its statistics panel.

Do not replace this value with static or fabricated data. Port the behavior only
after Zensical publishes a stable third-party module API.

## Production switch gates

Do not replace the MkDocs production workflow until all of the following have
been compared against the current production output and accepted:

- The complete site builds and representative URLs remain unchanged.
- Homepage, deep navigation, tags, search, math, Mermaid, tables, code blocks,
  admonitions, CSS, JavaScript, fonts, visit counter, and theme palettes work.
- Page source and commit-history links are correct.
- Git authors, contributors, creation dates, and revision dates match the
  current MkDocs output.
- Word-count statistics are restored with real generated values.

After these gates pass, migrate production to GitHub's official Pages artifact
deployment using `actions/upload-pages-artifact` and `actions/deploy-pages`.
That deployment must replace, rather than append to, the generated site and
must not retain static-site history in `gh-pages`.
