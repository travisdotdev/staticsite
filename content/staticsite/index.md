# ⚡ Static Site Generator

_Python · HTML/CSS · Markdown_

A command-line tool that transforms Markdown files into a fully rendered HTML website — built from scratch in pure Python 3, with no third-party parsing libraries.

[View on GitHub](https://github.com/travisdotdev/staticsite)

## How it works

The parser runs in two passes:

1. **Block-level** — splits the document into typed segments: headings, code fences, blockquotes, lists, and paragraphs
2. **Inline-level** — recursively resolves bold, italic, inline code, links, and images within each block

The resulting tree of `HTMLNode` objects is then rendered to a string and injected into a `template.html` layout via a `{{ Content }}` placeholder.

## Features

- Custom HTML node system (`HTMLNode`, `LeafNode`, `ParentNode`) for tree-based rendering
- Recursive page generation — walks the entire `content/` directory and mirrors the structure in `public/`
- Automated build pipeline — cleans, syncs static assets, and regenerates on every run
- No external dependencies

## Running it locally

```
git clone https://github.com/travisdotdev/staticsite.git
cd staticsite
python3 src/main.py
python3 -m http.server 8888 --directory public
```

[← Projects](/projects)
