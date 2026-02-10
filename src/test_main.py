import unittest

from main import markdown_to_html_node


class TestMain(unittest.TestCase):
    def test_paragraph_single(self):
        md = "This is **bolded** paragraph"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph</p></div>",
        )
