from markdown_blocks import markdown_to_blocks, block_to_block_type, BlockType
from htmlnode import HTMLNode, ParentNode
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node, TextNode

# TODO
# You didn't finish this lesson on boot.dev where you manully create the html file CH4: Blocks L3:


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    return ParentNode("div", children, None)


def block_to_html_node(block):
    block_type = block_to_block_type(block)
    if block_type == BlockType.PARAGRAPH:
        return paragraph_to_html_node(block)
    if block_type == BlockType.HEADING:
        return heading_to_html_node(block)
    if block_type == BlockType.QUOTE:
        return quote_to_html_node(block)


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        child = text_node_to_html_node(text_node)
        children.append(child)
    return children


def paragraph_to_html_node(block):
    lines = block.split("\n")
    text = " ".join(lines)
    children = text_to_children(text)
    return ParentNode("p", children)


def heading_to_html_node(block):
    level = 0
    for ch in block:
        if ch == "#":
            level += 1
        else:
            break

    if level == 0 or len(block) <= level or block[level] != " ":
        raise ValueError("invalid heading")

    text = block[level + 1 :]
    children = text_to_children(text)
    return ParentNode(f"h{level}", children)


def code_to_html_node(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("invalid code block")
        text = block[4:-3]
        raw_text_node = TextNode(text, TextType.TEXT)
        child = text_node_to_html_node(raw_text_node)
        code = ParentNode("code", [child])
        return ParentNode("pre", [code])


def quote_block_to_text(block: str) -> str:
    lines = block.split("\n")
    cleaned = []
    for line in lines:
        line = line.lstrip()
        if not line.startswith(">"):
            raise ValueError("invalid quote block line")
        content = line[1:]
        if content.startswith(" "):
            content = content[1:]
        cleaned.append(content)
    return "n".join(cleaned)


def quote_to_html_node(block: str):
    text = quote_block_to_text(block)
    children = text_to_children(text)
    paragraph_node = ParentNode("p", children)
    return ParentNode("blockquote", [paragraph_node])


def main():
    pass


if __name__ == "__main__":
    main()
