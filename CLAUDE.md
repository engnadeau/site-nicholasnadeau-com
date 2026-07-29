# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is Nicholas Nadeau's personal website built with Astro v5, a modern static site generator. The site features a blog with MDX support and is optimized for performance and SEO.

## Tech Stack

- **Framework**: Astro v5.7.5 (static site generator)
- **Language**: TypeScript
- **Styling**: Tailwind CSS v3.4 with Typography plugin
- **Content**: MDX/Markdown files in `src/content/post/`
- **Package Manager**: pnpm v10.8.1
- **Node**: v18.17.1+ or v20.3.0+ or v21.0.0+

## Essential Commands

```bash
# Development
pnpm dev          # Start development server (or pnpm start)
pnpm build        # Build for production
pnpm preview      # Preview production build locally

# Code Quality (ALWAYS run before committing)
pnpm check        # Run all checks (Astro, ESLint, Prettier)
pnpm check:astro  # Type check Astro files
pnpm check:eslint # Lint code
pnpm check:prettier # Check formatting
pnpm format       # Format code with Prettier
pnpm fix:eslint   # Auto-fix ESLint issues
```

## Project Architecture

### Key Directories

- `src/content/post/`: Blog posts organized by year (2023/, 2024/, 2025/)
- `src/components/`: Reusable Astro components
  - `blog/`: Blog-specific components
  - `common/`: Shared components
  - `ui/`: UI primitives
  - `widgets/`: Page sections
- `src/pages/`: Route definitions (file-based routing)
  - `[...blog]/`: Dynamic blog routes
  - `index.astro`: Homepage
- `src/layouts/`: Page layouts
- `src/assets/`: Processed assets (images, styles)
- `public/`: Static assets served as-is

### Configuration Files

- `astro.config.ts`: Astro configuration with integrations (Tailwind, MDX, Sitemap, etc.)
- `src/config.yaml`: Site metadata, SEO settings, and blog configuration
- `tailwind.config.js`: Tailwind customizations (colors, fonts, animations)
- `tsconfig.json`: TypeScript config with path alias `~/*` → `src/*`

### Writing Style

**No em dashes in prose or copy.** Simple punctuation only: periods, commas, and colons carry the load. The reason is that heavy em dash use is one of the loudest tells of machine-written text, and this site is a personal byline. This applies to sentences and body copy everywhere in the repo: blog posts, page copy, `src/config.yaml` metadata, component strings, commit messages, and PR descriptions.

Avoid these characters and their entities:

- `—` em dash (U+2014) and `&mdash;`
- `–` en dash (U+2013) and `&ndash;`. Numeric ranges spell it out: `2023 to 2025`, not `2023–2025`
- `…` ellipsis (U+2026). Use three periods only when quoting an actual elision
- Prefer to avoid semicolons too. They usually mark a sentence that wants to be two

Hyphens in compound words (`zero-to-one`, `AI-driven`) are fine.

**Recast, do not substitute.** Swapping an em dash for a comma leaves a limp sentence. Split it into two sentences, or promote the aside to a colon. An em dash pair wrapping a long appositive usually wants to become a colon plus a list.

**MDX trap:** Astro's markdown SmartyPants is on by default, so `--` renders as an en dash and `---` as an em dash even though the source file looks clean. Never type consecutive hyphens in prose.

#### The one exception: press release datelines

A press release opens with a dateline, and the dash after the city is the format, not a stylistic choice. Leave those alone:

```markdown
**Montreal, Canada** — [SmartOne](...) announced today the acquisition of...
**Montréal, QC – January 20, 2025** – [AI Salon](...), a global network of...
```

The exception is that opening dash only. The body of a press release follows the same no em dash rule as everything else. Do not invent new exceptions: if a dash feels necessary somewhere else, the sentence needs recasting instead.

#### Verify before committing

```bash
grep -rn '[—–…]\|&mdash;\|&ndash;\|&hellip;' src/   # the characters themselves
grep -rn '[^-]--[^-]' src/content/post/             # SmartyPants sources
```

The second should print nothing. The first should print nothing except the two known press release datelines above, in `2024-02-15_smartone-acquires-nadeau-innovations.md` and `2025-01_ai-salon-montreal.mdx`. Any other hit is a bug.

The `--` check is scoped to `src/content/post/` on purpose: CSS custom properties (`--aw-color-primary`) would flood it otherwise.

For a single prose file, `LC_ALL=C grep -n '[^ -~]' <file>` lists every non-ASCII character. Expect only deliberate ones (accents like Montréal, emoji); anything else is a smart quote or a stray dash.

### Content Management

Blog posts use MDX format with frontmatter:

- Located in `src/content/post/YYYY/YYY-MM_post-slug.mdx`
- Supports components within markdown
- Automatic reading time calculation
- Image optimization and lazy loading
- Responsive tables

### Deployment

The site is deployed to Netlify (primary) with CI/CD via GitHub Actions:

- Automatic checks on PRs to main branch
- Build verification before deployment
- Security scanning with CodeQL

## Development Workflow

1. Create/edit blog posts in `src/content/post/YYYY/`
2. Use existing components from `src/components/` when possible
3. Run `pnpm dev` to preview changes
4. Always run `pnpm check` before committing
5. The CI pipeline will verify builds on push/PR

## Important Notes

- No traditional testing framework - relies on static analysis and build checks
- Path alias `~/*` is configured for imports from `src/*`
- Images in `src/assets/images/` are automatically optimized
- Blog permalinks follow pattern: `/%slug%`
- Site configuration in `src/config.yaml` controls metadata and features
