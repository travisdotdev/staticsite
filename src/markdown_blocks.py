from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks


def block_to_block_type(block):
    split_block = block.strip().split(" ", 1)
    is_heading = (
        len(split_block) == 2
        and 1 <= len(split_block[0]) <= 6
        and all(char == "#" for char in split_block[0])
        and split_block[1].strip != ""
    )
    if is_heading:
        return BlockType.HEADING
    is_code = block.startswith("```\n") and block.endswith("```")
    if is_code:
        return BlockType.CODE
    split_block = block.strip().split("\n")
    is_quote = [line.startswith(">") for line in split_block]
    if all(is_quote):
        return BlockType.QUOTE
    split_block = block.strip().split("\n")
    is_unordered_list = [line.startswith("- ") for line in split_block]
    if all(is_unordered_list):
        return BlockType.UNORDERED_LIST
    split_block = block.strip().split("\n")
    split_block2 = []
    fullstop_present = False
    incrementing_by_one = False
    incrementing_list = []
    for line in split_block:
        split_block2.append(line.strip().split(" ", 1))
    for line2 in split_block2:
        if not line2[0].endswith("."):
            fullstop_present = False
        else:
            fullstop_present = True
        incrementing_list.append(int(line2[0].strip(".")))
    if incrementing_list == list(range(1, len(incrementing_list) + 1)):
        incrementing_by_one = True
    is_ordered_list = incrementing_by_one and fullstop_present
    if is_ordered_list:
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH
