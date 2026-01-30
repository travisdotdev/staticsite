import unittest

from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import HTMLNode
from markdown_blocks import markdown_to_blocks
from inline_markdown import (
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_image,
    split_nodes_link,
    text_to_textnodes,
)


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a textnode", TextType.BOLD)
        node2 = TextNode("This is a textnode", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a textnode", TextType.BOLD)
        node2 = TextNode("This is a different textnode", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_not_eq2(self):
        node = TextNode("String1", TextType.BOLD)
        node2 = TextNode("String", TextType.BOLD)
        self.assertNotEqual(repr(node), repr(node2))

    def test_nodes_eq_url(self):
        node1 = TextNode("String", TextType.TEXT, "https://example.com")
        node2 = TextNode("String", TextType.TEXT, "https://example.com")
        self.assertEqual(node1, node2)

    def test_text_type_not_eq(self):
        node = TextNode("String", TextType.TEXT)
        node2 = TextNode("String", TextType.BOLD)
        self.assertNotEqual(node.text_type.value, node2.text_type.value)

    def test_nodes_not_equal_url(self):
        node1 = TextNode("String", TextType.TEXT, "https://a.com")
        node2 = TextNode("String", TextType.TEXT, "https://b.com")
        self.assertNotEqual(node1, node2)

    def test_url_is_none(self):
        node = TextNode("This is a textnode", TextType.BOLD)
        self.assertIsNone(node.url)

    def test_text_is_string(self):
        node = TextNode("String", TextType.TEXT)
        self.assertTrue(isinstance(node.text, str))

    def test_repr(self):
        node = TextNode("String", TextType.TEXT, "https://a.com")
        self.assertEqual("TextNode(String, text, https://a.com)", repr(node))

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_text_image(self):
        node = TextNode("This is an image", TextType.IMAGE, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://www.boot.dev", "alt": "This is an image"},
        )

    def test_text_bold(self):
        node = TextNode("This is a bold text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold text node")

    def test_text_invalid_type(self):
        node = TextNode("This is an invalid text node", "invalid type")
        with self.assertRaises(ValueError):
            text_node_to_html_node(node)

    def test_inline_markdown_delimiter_split(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ],
        )

    def test_inline_markdown_invalid_delimiter(self):
        node = TextNode("This is **broken text", TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "**", TextType.BOLD)

    def test_inline_markdown_multiple_delimiter_splits(self):
        node = TextNode("**Hello** Text **Greetings**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(
            new_nodes,
            [
                TextNode("Hello", TextType.BOLD),
                TextNode(" Text ", TextType.TEXT),
                TextNode("Greetings", TextType.BOLD),
            ],
        )

    def test_inline_markdown_multiple_nodes(self):
        node = [
            TextNode("before **x**", TextType.TEXT),
            TextNode("keep", TextType.BOLD),
        ]
        new_nodes = split_nodes_delimiter(node, "**", TextType.BOLD)
        self.assertEqual(
            new_nodes,
            [
                TextNode("before ", TextType.TEXT),
                TextNode("x", TextType.BOLD),
                TextNode("keep", TextType.BOLD),
            ],
        )

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extact_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        )
        self.assertListEqual(
            matches,
            [
                ("to boot dev", "https://www.boot.dev"),
                ("to youtube", "https://www.youtube.com/@bootdotdev"),
            ],
        )

    def test_split_image(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            ],
            new_nodes,
        )

    def test_split_image_single(self):
        node = TextNode(
            "![image](https://www.example.COM/IMAGE.PNG)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "https://www.example.COM/IMAGE.PNG"),
            ],
            new_nodes,
        )

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a link ", TextType.TEXT),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode(
                    "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
                ),
            ],
            new_nodes,
        )

    def test_text_to_textnodes(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        new_nodes = text_to_textnodes(text)
        self.assertListEqual(
            new_nodes,
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode(
                    "obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"
                ),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
        )


if __name__ == "__main__":
    unittest.main()
