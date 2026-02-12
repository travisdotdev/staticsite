import unittest
from markdown_blocks import (
    markdown_to_blocks,
    block_to_block_type,
    markdown_to_html_node,
    BlockType,
)


class TestMarkdownBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        text = """
# This is a heading

This is a paragraph of text. It has some **bold** and _italic_ words inside of it.

- This is the first list item in a list block
- This is a list item
- This is another list item"""
        result = markdown_to_blocks(text)
        self.assertEqual(
            result,
            [
                "# This is a heading",
                "This is a paragraph of text. It has some **bold** and _italic_ words inside of it.",
                "- This is the first list item in a list block\n- This is a list item\n- This is another list item",
            ],
        )

    def test_markdown_to_blocks_multiple_new_lines(self):
        md = """
This is **bolded** paragraph



This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_blocktype_ordered_list(self):
        block = """1. hey hey hey
2. right hello Hi
3. Greetings bonjour23910
4. Hello"""
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.ORDERED_LIST)

    def test_blocktype_invalid_ordered_list(self):
        block = """1. hey hey hey
2. right hello Hi
31. Greetings bonjour23910
4. Hello"""
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.PARAGRAPH)

    def test_blocktype_heading(self):
        block = """### HEADING"""
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.HEADING)

    def test_blocktype_code(self):
        block = """```
print(this_is_code)
```"""
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.CODE)

    def test_blocktype_quote(self):
        block = """>these are quotes
>hello world
>testing testing
> for i am become death destroyer of worlds -Vishnu """
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.QUOTE)

    def test_blocktype_unordered_list(self):
        block = """- these are quotes
- hello world
- testing testing
- for i am become death destroyer of worlds -Vishnu"""
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.UNORDERED_LIST)

    def test_blocktype_paragraph(self):
        block = """ 1.HELLO
3.greetings
- wow
> neo
````"""
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.PARAGRAPH)

    def test_paragraph_single(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p></div>",
        )

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_lists(self):
        md = """
- This is a list
- with items
- and _more_ items

1. This is an `ordered` list
2. with items
3. and more items

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>",
        )

    def test_headings(self):
        md = """
# this is an h1

this is paragraph text

## this is an h2
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>this is an h1</h1><p>this is paragraph text</p><h2>this is an h2</h2></div>",
        )

    def test_blockquote(self):
        md = """
> This is a
> blockquote block

this is paragraph text

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
        )

    def test_code(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )


if __name__ == "__main__":
    unittest.main()
