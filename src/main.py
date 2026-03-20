from copystatic import copy_files_recursive, clean_up_structure
from gencontent import generate_pages_recursive
import sys

STATIC_PATH = "./static"
DESTINATION_PATH = "./docs"
HTML_TEMPLATE_PATH = "./template.html"
CONTENT_PATH = "./content"


def main():
    if len(sys.argv) > 1:
        base_path = sys.argv[1]
    else:
        base_path = "/"

    clean_up_structure(DESTINATION_PATH)
    copy_files_recursive(STATIC_PATH, DESTINATION_PATH)
    generate_pages_recursive(
        CONTENT_PATH, HTML_TEMPLATE_PATH, DESTINATION_PATH, base_path
    )


if __name__ == "__main__":
    main()
