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

**No em dashes in prose or copy.** Simple punctuation only: periods, commas, and colons carry the load. The reason is that heavy em dash use is one of the loudest tells of machine-written text, and this site is a personal byline.

The rule covers anything a reader reads as writing: blog posts, page copy, component strings, the `description` fields in `src/config.yaml`, commit messages, and PR descriptions. It does not cover page metadata, where a dash is a structural separator rather than punctuation in a sentence. See the exceptions below.

Avoid these characters and their entities:

- `—` em dash (U+2014) and `&mdash;`
- `–` en dash (U+2013) and `&ndash;`. Numeric ranges spell it out: `2023 to 2025`, not `2023–2025`
- `…` ellipsis (U+2026). Typing `...` does not dodge this: SmartyPants converts it to the character at build time. Only use it inside a verbatim quotation
- Prefer to avoid semicolons too. They usually mark a sentence that wants to be two

Hyphens in compound words (`zero-to-one`, `AI-driven`) are fine.

**Recast, do not substitute.** Swapping an em dash for a comma leaves a limp sentence. Split it into two sentences, or promote the aside to a colon. An em dash pair wrapping a long appositive usually wants to become a colon plus a list.

**MDX trap:** markdown SmartyPants is on by default, so the source file can grep clean and still render a banned character. `--` becomes an en dash, `---` becomes an em dash, and `...` becomes a `…`. Never type consecutive hyphens or three periods in prose. Checking the source is not enough, which is why the checks below include a `dist/` pass.

### Exception 1: page metadata

Page titles are structure, not prose. A dash separating a title from a qualifier is doing a layout job that a comma cannot do, so leave these alone:

- `metadata.title.template` in `src/config.yaml`, which appends the site name to every `<title>`
- the `— Page N` suffix in the blog, tag, and category pagination titles under `src/pages/[...blog]/`

This covers the `<title>` and the `og:` and `twitter:` title tags that Astro derives from it. It does not extend to `description` fields, which are sentences and follow the rule.

### Exception 2: press release datelines

A press release opens with a dateline, and the dash after the city is the format, not a stylistic choice. Leave those alone:

```markdown
**Montreal, Canada** — [SmartOne](...) announced today the acquisition of...
**Montréal, QC – January 20, 2025** – [AI Salon](...), a global network of...
```

That opening dash only. The body of a press release follows the same no em dash rule as everything else.

Two exceptions is the whole list. Do not add a third: if a dash feels necessary in a sentence, the sentence needs recasting instead.

### Verify before committing

```bash
grep -rn '[—–…]\|&mdash;\|&ndash;\|&hellip;' src/content/post/   # the characters themselves
grep -rn '[^-]--[^-]\|\.\.\.' src/content/post/                 # SmartyPants sources

# Rendered copy, with <head> stripped so exempt page titles do not drown the signal.
# Run pnpm build first.
grep -rl '[—–…]' dist --include=index.html | while read -r f; do
  sed 's|.*</head>||' "$f" | grep -q '[—–…]' && echo "$f"
done
```

All three should return only these known hits, so anything else is a bug:

- the two press release datelines above, in `2024/02/smartone-acquires-nadeau-innovations.md` and `2025/01/ai-salon-montreal.mdx`
- `2026/07/esther-dyson-trade-offs-and-transparency.mdx`, where a `...` sits inside a verbatim quotation and renders as `…`

The source checks are scoped to `src/content/post/` deliberately. Running them over all of `src/` buries the signal under exempt page titles, CSS custom properties (`--aw-color-primary`), and a vendored `.ellipsis:after { content: "…" }` rule. The `dist/` check is the one that covers page copy and component strings, and it is the only check that sees what SmartyPants actually produced.

For a single prose file, `LC_ALL=C grep -n '[^ -~]' <file>` lists every non-ASCII character. Expect only deliberate ones (accents like Montréal, emoji); anything else is a smart quote or a stray dash.
