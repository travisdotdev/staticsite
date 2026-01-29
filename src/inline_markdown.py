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


def split_nodes_image(old_nodes):
    regex_extracted_nodes = []
    new_nodes = []
    original_text = ""
    for node in old_nodes:
        regex_extracted_nodes = extract_markdown_images(node.text)
        if not regex_extracted_nodes:
            new_nodes.append(node)
        else:
            original_text = node.text
            split_text = []
            for image in regex_extracted_nodes:
                split_text = original_text.split(f"![{image[0]}]({image[1]})", 1)
                if split_text[0]:
                    new_node = TextNode(split_text[0], TextType.TEXT)
                    new_nodes.append(new_node)
                new_node = TextNode(image[0], TextType.IMAGE, image[1])
                new_nodes.append(new_node)
                original_text = split_text[1]
            if original_text:
                new_node = TextNode(original_text, TextType.TEXT)
                new_nodes.append(new_node)
    return new_nodes


def split_nodes_link(old_nodes):
    regex_extracted_nodes = []
    new_nodes = []
    original_text = ""
    for node in old_nodes:
        regex_extracted_nodes = extract_markdown_links(node.text)
        if not regex_extracted_nodes:
            new_nodes.append(node)
        else:
            original_text = node.text
            split_text = []
            for link in regex_extracted_nodes:
                split_text = original_text.split(f"[{link[0]}]({link[1]})", 1)
                if split_text[0]:
                    new_node = TextNode(split_text[0], TextType.TEXT)
                    new_nodes.append(new_node)
                new_node = TextNode(link[0], TextType.LINK, link[1])
                new_nodes.append(new_node)
                original_text = split_text[1]
        if original_text:
            new_node = TextNode(original_text, TextType.TEXT)
            new_nodes.append(new_node)
    return new_nodes
