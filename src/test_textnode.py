import unittest

from textnode import TextNode, TextType


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


if __name__ == "__main__":
    unittest.main()
