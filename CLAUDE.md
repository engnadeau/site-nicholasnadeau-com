# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Important Notes

- Always run `pnpm check` before committing (CI runs the same checks on every PR)
- No traditional testing framework: correctness relies on static analysis and the build
- Path alias `~/*` maps to `src/*`
- Blog permalinks follow the pattern `/%slug%`
- Post files go in `src/content/post/YYYY/MM/` matching their `publishDate`, named exactly what the URL slug should be: kebab-case, no date prefix. The filename minus extension _is_ the slug, so the folders only organize files on disk (`2026/07/nobody-asked.mdx` publishes at `/nobody-asked`)
- `src/config.yaml` controls site metadata and feature toggles

## Writing Style

**No em dashes in prose or copy.** Simple punctuation only: periods, commas, and colons carry the load. The reason is that heavy em dash use is one of the loudest tells of machine-written text, and this site is a personal byline. This applies to sentences and body copy everywhere in the repo: blog posts, page copy, `src/config.yaml` metadata, component strings, commit messages, and PR descriptions.

Avoid these characters and their entities:

- `—` em dash (U+2014) and `&mdash;`
- `–` en dash (U+2013) and `&ndash;`. Numeric ranges spell it out: `2023 to 2025`, not `2023–2025`
- `…` ellipsis (U+2026). Typing `...` does not dodge this: SmartyPants converts it to the character at build time. Only use it inside a verbatim quotation
- Prefer to avoid semicolons too. They usually mark a sentence that wants to be two

Hyphens in compound words (`zero-to-one`, `AI-driven`) are fine.

**Recast, do not substitute.** Swapping an em dash for a comma leaves a limp sentence. Split it into two sentences, or promote the aside to a colon. An em dash pair wrapping a long appositive usually wants to become a colon plus a list.

**MDX trap:** markdown SmartyPants is on by default, so the source file can grep clean and still render a banned character. `--` becomes an en dash, `---` becomes an em dash, and `...` becomes a `…`. Never type consecutive hyphens or three periods in prose. Checking the source is not enough, which is why the checks below include a `dist/` pass.

### The one exception: press release datelines

A press release opens with a dateline, and the dash after the city is the format, not a stylistic choice. Leave those alone:

```markdown
**Montreal, Canada** — [SmartOne](...) announced today the acquisition of...
**Montréal, QC – January 20, 2025** – [AI Salon](...), a global network of...
```

The exception is that opening dash only. The body of a press release follows the same no em dash rule as everything else. Do not invent new exceptions: if a dash feels necessary somewhere else, the sentence needs recasting instead.

### Verify before committing

```bash
grep -rn '[—–…]\|&mdash;\|&ndash;\|&hellip;' src/       # the characters themselves
grep -rn '[^-]--[^-]\|\.\.\.' src/content/post/         # SmartyPants sources
grep -rlo '[—–…]' dist/ --exclude-dir=_astro            # what actually shipped
```

Known hits, so anything else is a bug:

- the two press release datelines above, in `2024/02/smartone-acquires-nadeau-innovations.md` and `2025/01/ai-salon-montreal.mdx`
- `esther-dyson-trade-offs-and-transparency.mdx`, where a `...` sits inside a verbatim quotation and renders as `…`
- `src/pages/[...blog]/[category]/[...page].astro`, which puts a dash in the paginated category page title, so every paginated category page in `dist/` carries one. That is an outstanding violation, not an exception, and should be fixed on its own.

The `--` check is scoped to `src/content/post/` on purpose: CSS custom properties (`--aw-color-primary`) would flood it otherwise. The `dist/` check skips `_astro` for the same reason, since a vendored `.ellipsis:after { content: "…" }` rule lives in the bundled CSS.

For a single prose file, `LC_ALL=C grep -n '[^ -~]' <file>` lists every non-ASCII character. Expect only deliberate ones (accents like Montréal, emoji); anything else is a smart quote or a stray dash.
