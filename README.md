# Nicholas' Site

[![Netlify Status](https://api.netlify.com/api/v1/badges/10d83a12-0f48-46d9-a25a-e967a785297e/deploy-status)](https://app.netlify.com/sites/nicholasnadeau/deploys)

This project is based on [AstroWind](https://github.com/onwidget/astrowind), using `.astro` or `.md` files in the `src/pages/` directory to define routes by file name.

Static assets can be added in `public/` (for non-transforming assets) or `assets/` (for direct imports).

## Commands

Run these from the project root in the terminal:

| Command               | Description                                |
| --------------------- | ------------------------------------------ |
| `pnpm install`        | Install dependencies                       |
| `pnpm run dev`        | Start local dev server at `localhost:3000` |
| `pnpm run build`      | Build for production to `./dist/`          |
| `pnpm run preview`    | Preview production build locally           |
| `pnpm run check`      | Check for project errors                   |
| `pnpm run fix`        | Lint and format code with Prettier         |
