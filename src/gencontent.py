import os
from markdown_blocks import markdown_to_html_node

content_path = "content/index.md"


def extract_title(markdown):
    lines = markdown.splitlines()
    for line in lines:
        if line.startswith("# "):
            return line[2:].strip()
    raise ValueError("Title not found")


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r", encoding="utf-8") as f:
        markdown = f.read()
    title = extract_title(markdown)
    md_to_html = markdown_to_html_node(markdown)
    with open(template_path, "r", encoding="utf-8") as f2:
        html_file = f2.read()
    html_file = html_file.replace("{{ Title }}", title)
    html_file = html_file.replace("{{ Content }}", md_to_html.to_html())
    parent = os.path.dirname(dest_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(html_file)
    print("HTML File Created")
