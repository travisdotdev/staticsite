import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


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

    def test_leafnode_repr(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(
            node.to_html(), '<a href="https://www.google.com">Click me!</a>'
        )

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(), "<div><span><b>grandchild</b></span></div>"
        )

    def test_to_html_no_tag(self):
        node = ParentNode(None, [LeafNode("b", "text")])
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_no_children(self):
        node = ParentNode("div", None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_nested_parents(self):
        node = ParentNode(
            "div",
            [
                ParentNode("p", [LeafNode("b", "Bold")]),
                LeafNode("span", "Text"),
            ],
        )
        self.assertEqual(
            node.to_html(), "<div><p><b>Bold</b></p><span>Text</span></div>"
        )

    def test_to_html_with_props(self):
        node = ParentNode(
            "div", [LeafNode("p", "text")], {"class": "container", "id": "main"}
        )
        html = node.to_html()
        self.assertIn("<div", html)
        self.assertIn('class="container"', html)
        self.assertIn('id="main"', html)
        self.assertIn("<p>text</p>", html)
        self.assertIn("</div>", html)

    def test_to_html_empty_children_list(self):
        node = ParentNode("div", [])
        self.assertEqual(node.to_html(), "<div></div>")


if __name__ == "__main__":
    unittest.main()
