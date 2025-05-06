Blog post images must follow these conventions:

1.  **Location:** Images should be placed in the corresponding year's directory within `src/assets/images/post/`, e.g., `src/assets/images/post/YYYY/`.
2.  **Naming:** Image files must be named using the format `YYYY-MM_image-slug.ext`, where:
    - `YYYY` is the four-digit year.
    - `MM` is the two-digit month.
    - `image-slug` is a concise, lowercase, hyphenated description of the image content.
    - `.ext` is the image file extension (e.g., `.jpg`, `.png`).
3.  **Linking in Frontmatter:** The `image` field in the post's frontmatter must link to the image using a path starting with `~/assets/images/post/YYYY/`, for example:
    `image: ~/assets/images/post/YYYY/YYYY-MM_image-slug.jpg`
