content_path = "content/index.md"

with open(content_path, "r", encoding="utf-8") as f:
    md = f.read()


def extract_title(markdown):
    lines = markdown.splitlines()
    for line in lines:
        if line.startswith("# "):
            return line[2:].strip()
    raise ValueError("Title not found")
