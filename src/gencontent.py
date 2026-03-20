import os
from markdown_blocks import markdown_to_html_node
import shutil

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


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)
        print(f"Path {dest_dir_path} created")
    for entry in os.listdir(dir_path_content):
        source_path = os.path.join(dir_path_content, entry)
        if os.path.isfile(source_path) and source_path.endswith(".md"):
            print(f"Markdown File found at: {source_path} copied to {dest_dir_path}")
            html_path = os.path.join(dest_dir_path, f"{entry.replace('.md', '.html')}")
            generate_page(source_path, template_path, html_path)
        elif os.path.isdir(source_path):
            destination_path = os.path.join(dest_dir_path, entry)
            generate_pages_recursive(source_path, template_path, destination_path)


def copy_files_recursive(source, destination):
    if not os.path.exists(destination):
        print(f"Path {destination} created")
        os.mkdir(destination)
    for entry in os.listdir(source):
        source_path = os.path.join(source, entry)
        if os.path.isfile(source_path):
            print(f"File at: {source_path} copied to {destination}")
            shutil.copy(source_path, destination)
        else:
            destination_path = os.path.join(destination, entry)
            copy_files_recursive(source_path, destination_path)
