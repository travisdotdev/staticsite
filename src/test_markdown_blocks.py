import unittest
from markdown_blocks import markdown_to_blocks, block_to_block_type, BlockType


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
        block = """
1. hey hey hey
2. right hello Hi
3. Greetings bonjour23910
4. Hello
"""
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.ORDERED_LIST)

    def test_blocktype_invalid_ordered_list(self):
        block = """
1. hey hey hey
2. right hello Hi
31. Greetings bonjour23910
4. Hello
"""
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
        block = """
>these are quotes
>hello world
>testing testing
> for i am become death destroyer of worlds -Vishnu 
"""
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.QUOTE)

    def test_blocktype_unordered_list(self):
        block = """
- these are quotes
- hello world
- testing testing
- for i am become death destroyer of worlds -Vishnu 
"""
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.UNORDERED_LIST)

        #     def test_blocktype_paragraph(self):
        #         block = """
        # 1.HELLO
        # 3.greetings
        # - wow
        # > neo
        # ````
        # """
        # result = block_to_block_type(block)
        # self.assertEqual(result, BlockType.PARAGRAPH)


if __name__ == "__main__":
    unittest.main()
