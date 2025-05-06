Blog posts in `src/content/post/YYYY/` should follow this structure:

1.  **Frontmatter:** Ensure the following YAML frontmatter fields are present:
    - `publishDate`: YYYY-MM-DD
    - `author`: Nicholas Nadeau
    - `title`: Concise and informative title (no emojis).
    - `description`: Brief (1-2 sentences) SEO-focused summary of the post.
    - `image`: Path following conventions in `image-handling.mdc`.
    - `category`: Must be one of: `Technology`, `Events`, `Community`.
    - `tags`: Max 5 relevant lowercase keywords. Prioritize core tags (`ai`, `startup`, `montreal` if relevant). See `tagging-strategy.mdc`.
2.  **Body:**
    - Start with a concise opening summarizing the main point.
    - Use headings or bullet points for structure.
    - Highlight key takeaways, people, or companies.
    - Acknowledge sponsors/partners briefly if applicable.
    - Maintain tone from `tone-style.mdc`.
3.  **Linking:**
    - If based on external content (e.g., LinkedIn), end with: `See the original post on [Platform](mdc:URL)`.

Example Frontmatter:

```yaml
---
publishDate: YYYY-MM-DD
author: Nicholas Nadeau
title: 'Example Post Title'
description: 'A concise description for SEO about the example post.'
image: ~/assets/images/post/YYYY/YYYY-MM_example.jpg
category: Technology # Or Events, Community
tags:
  - ai
  - startup
  - specific-tag-1
  - specific-tag-2
  - specific-tag-3
---
```

- example
- tag

---

```

```
