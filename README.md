# ⚡ Static Site Generator

> A command-line tool that transforms raw Markdown files into a fully rendered HTML website — built from scratch in pure Python 3, with no third-party parsing libraries.

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

---

## Overview

This project is a fully hand-rolled static site generator. Feed it a directory of Markdown files and a HTML template, and it produces a complete, ready-to-serve website, preserving your folder structure, syncing your static assets, and injecting generated HTML into your layout automatically.

The goal was to build something that works **without** relying on tools like Jekyll, Hugo, or any Markdown parsing libraries.

## 🌐 Live Demo

The generated output is deployed via **GitHub Pages** and can be viewed live at:

**[travisdotdev.github.io/staticsite](https://travisdotdev.github.io/staticsite)**

This is the real output of the build pipeline. The HTML you see there was generated directly from the Markdown source files in `content/` using this tool.

---

## Features

### Custom HTML Node System

An object-oriented DOM representation built from three classes: `HTMLNode`, `LeafNode`, and `ParentNode` — that handles arbitrary nesting and renders valid HTML strings from a tree structure.

### Multi-Stage Markdown Parser

A hand-built parsing pipeline that processes Markdown in two distinct phases:

- **Block-level parsing** — splits documents into typed blocks (headings, code fences, blockquotes, ordered/unordered lists, and paragraphs) using regex and structural rules.
- **Inline-level parsing** — recursively identifies and converts inline styles (bold, italic, inline code, hyperlinks, and images) within each block.

### Recursive Page Generation

Walks the entire `content/` directory tree and generates a matching HTML file for every `.md` file found, preserving the original folder hierarchy in the `public/` output directory.

### Automated Build Pipeline

The build process is fully automated and repeatable:

1. **Cleanup** — safely deletes and recreates the `public/` directory to prevent stale files.
2. **Asset sync** — recursively copies `static/` assets (CSS, images) to `public/` without hardcoded paths.
3. **Template injection** — wraps generated HTML content in a `template.html` layout using a `{{ Content }}` placeholder.

---

## 📁 Project Structure

```
staticsite/
├── content/          # Markdown source files (mirrors output structure)
├── src/              # Python source code
├── static/           # Raw assets: CSS, images, fonts
├── public/           # Generated output (auto-created, do not edit)
├── docs/             # Project documentation
├── template.html     # HTML layout with {{ Content }} placeholder
├── main.sh           # Convenience script: build + serve
├── build.sh          # Standalone build script
└── test.sh           # Standalone test runner
```

---

## Getting Started

### Prerequisites

- Python 3.13+ (see `.python-version`)
- No external dependencies required

### 1. Clone the repository

```bash
git clone https://github.com/travisdotdev/staticsite.git
cd staticsite
```

### 2. Add your content

Place your `.md` files in the `content/` directory. Subdirectories are supported and will be mirrored in the output.

### 3. Generate the site

```bash
python3 src/main.py
```

The `public/` directory will be created (or rebuilt) with your rendered HTML files and synced assets.

### 4. Preview locally

```bash
python3 -m http.server 8888 --directory public
```

Then open [http://localhost:8888](http://localhost:8888) in your browser.

### 5. Convenience scripts

```bash
./main.sh    # Build and serve in one step
./build.sh   # Build only
```

---

## Technical Architecture

The generator follows a **block-to-inline** two-pass parsing strategy, which mirrors how real Markdown renderers work:

```
Markdown File
     │
     ▼
[ Block Splitter ]       ← Splits document into typed block segments
     │
     ▼
[ Block Type Classifier ] ← Uses regex & structural rules to label each block
     │
     ▼
[ Inline Parser ]         ← Recursively resolves bold, italic, code, links, images
     │
     ▼
[ HTML Node Tree ]        ← HTMLNode / LeafNode / ParentNode hierarchy
     │
     ▼
[ HTML String Renderer ]  ← Converts tree to valid HTML string
     │
     ▼
[ Template Injector ]     ← Inserts HTML into template.html via {{ Content }}
     │
     ▼
  public/*.html
```

This separation of concerns means each stage is independently testable and the parser can be extended (e.g. adding new block types) without touching the rendering layer.

---

## Testing

Unit tests cover every stage of the pipeline — from block splitting and type classification through inline parsing and HTML node rendering.

```bash
# Run all tests
python3 src/test_main.py

# Or use the test script
./test.sh
```

Tests are co-located with source in `src/` and named per module for easy navigation.

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
