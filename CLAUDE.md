# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Important Notes

- Always run `pnpm check` before committing (CI runs the same checks on every PR)
- No traditional testing framework: correctness relies on static analysis and the build
- Path alias `~/*` maps to `src/*`
- Blog permalinks follow the pattern `/%slug%`
- `src/config.yaml` controls site metadata and feature toggles
