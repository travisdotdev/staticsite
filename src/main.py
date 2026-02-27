from copystatic import copy_files_recursive, clean_up_structure
from gencontent import extract_title, generate_page

STATIC_PATH = "./static"
DESTINATION_PATH = "./public"
DESTINATION_PATH_HTML = "./public/index.html"
HTML_TEMPLATE_PATH = "./template.html"
MARKDOWN_PATH = "./content/index.md"


def main():
    clean_up_structure(DESTINATION_PATH)
    copy_files_recursive(STATIC_PATH, DESTINATION_PATH)
    generate_page(MARKDOWN_PATH, HTML_TEMPLATE_PATH, DESTINATION_PATH_HTML)


if __name__ == "__main__":
    main()
