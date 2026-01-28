from textnode import TextNode, TextType
import re


def split_nodes_delimiter(old_nodes, delimiter, text_type) -> list[TextNode]:
    result = []
    parts = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            parts = node.text.split(delimiter)
            if (len(parts) - 1) % 2 == 0:
                for index, value in enumerate(parts):
                    if index % 2 != 0 and value != "":
                        new_node = TextNode(value, text_type)
                        result.append(new_node)
                    elif value != "":
                        new_node = TextNode(value, TextType.TEXT)
                        result.append(new_node)
            else:
                raise Exception("Unclosed delimiter")
        else:
            result.append(node)
    return result


def extract_markdown_images(text):
    extracted_images = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return extracted_images


def extract_markdown_links(text):
    extracted_links = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return extracted_links
