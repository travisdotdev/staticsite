import unittest

from htmlnode import HTMLNode


class testHtmlNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode()
        repr = f"HTMLNode({None}, {None}, {None}, {None})"
        self.assertEqual(node.__repr__(), repr)

    def test_props_to_html_multiple_props(self):
        node = HTMLNode(
            tag="a",
            value="link",
            props={
                "href": "https://www.google.com",
                "target": "_blank",
            },
        )
        result = node.props_to_html()
        expected = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(result, expected)

    def test_props_to_html_none_or_empty(self):
        node_none = HTMLNode(props=None)
        self.assertEqual(node_none.props_to_html(), "")

        node_empty = HTMLNode(props={})
        self.assertEqual(node_none.props_to_html(), "")


if __name__ == "__main__":
    unittest.main()
