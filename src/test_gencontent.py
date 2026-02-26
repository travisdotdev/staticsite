import unittest
from gencontent import extract_title


class testGenContent(unittest.TestCase):
    def test_extract_title(self):
        markdown = """
# Hello
##greetings
hello world
        """
        title = extract_title(markdown)
        self.assertEqual("Hello", title)

    def test_no_title(self):
        markdown = """
hello
greetings
hello world
        """
        with self.assertRaises(ValueError):
            extract_title(markdown)

    def test_invalid_hash_title(self):
        markdown = """
## Hello
greetings
        """
        with self.assertRaises(ValueError):
            extract_title(markdown)
