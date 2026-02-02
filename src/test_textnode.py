import unittest

from textnode import TextNode, TextType, text_node_to_html_node


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


if __name__ == "__main__":
    unittest.main()
