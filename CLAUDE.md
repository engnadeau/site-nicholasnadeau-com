# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Important Notes

- Always run `pnpm check` before committing (CI runs the same checks on every PR)
- No traditional testing framework: correctness relies on static analysis and the build
- Path alias `~/*` maps to `src/*`
- Blog permalinks follow the pattern `/%slug%`
- Post files go in `src/content/post/YYYY/MM/` matching their `publishDate`, named exactly what the URL slug should be: kebab-case, no date prefix. The filename minus extension _is_ the slug, so the folders only organize files on disk (`2026/07/nobody-asked.mdx` publishes at `/nobody-asked`)
- `src/config.yaml` controls site metadata and feature toggles
