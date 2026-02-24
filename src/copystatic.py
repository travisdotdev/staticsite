import os
import shutil

dir_path_destination = "../public"
dir_path_source = "../static"

if not os.path.exists(dir_path_destination):
    os.mkdir(dir_path_destination)


def copy_files_recursive(source, destination):
    if not os.path.exists(destination):
        os.mkdir(destination)
    print(os.listdir(source))
    for directory in os.listdir(source):
        if "." in directory:
            shutil.copy(directory, destination)
        else:
            destination_path = os.path.join(dir_path_destination, directory)
            source_path = os.path.join(dir_path_source, directory)
            copy_files_recursive(source_path, destination_path)


copy_files_recursive(dir_path_source, dir_path_destination)
