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
