from copystatic import copy_files_recursive, clean_up_structure

STATIC_PATH = "./static"
DESTINATION_PATH = "./public"


def main():
    clean_up_structure(DESTINATION_PATH)
    copy_files_recursive(STATIC_PATH, DESTINATION_PATH)


if __name__ == "__main__":
    main()
