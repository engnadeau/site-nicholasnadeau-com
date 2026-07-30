[![Netlify Status](https://api.netlify.com/api/v1/badges/10d83a12-0f48-46d9-a25a-e967a785297e/deploy-status)](https://app.netlify.com/sites/nicholasnadeau/deploys)
[![CI](https://github.com/engnadeau/site-nicholasnadeau-com/actions/workflows/ci.yaml/badge.svg)](https://github.com/engnadeau/site-nicholasnadeau-com/actions/workflows/ci.yaml)
[![CodeQL](https://github.com/engnadeau/site-nicholasnadeau-com/actions/workflows/github-code-scanning/codeql/badge.svg)](https://github.com/engnadeau/site-nicholasnadeau-com/actions/workflows/github-code-scanning/codeql)
[![Dependabot Updates](https://github.com/engnadeau/site-nicholasnadeau-com/actions/workflows/dependabot/dependabot-updates/badge.svg)](https://github.com/engnadeau/site-nicholasnadeau-com/actions/workflows/dependabot/dependabot-updates)

# Nicholas' Site

This project uses `.astro` or `.md` files in the `src/pages/` directory to define routes by file name.

Static assets can be added in `public/` (for non-transforming assets) or `src/assets/` (for direct imports and transformations).

## Blog posts

File the post under the year and month of its `publishDate`, and name the file exactly what the URL should be:

```
src/content/post/2026/07/nobody-asked.mdx   →   nicholasnadeau.com/nobody-asked
```

Kebab-case, no date prefix in the file name. The file name minus its extension _is_ the slug, so the `YYYY/MM/` folders only organize files on disk and never appear in the URL.
