import os
import shutil


def clean_up_structure(destination):
    if os.path.exists(destination):
        print("Deleting pre-existing public directory")
        shutil.rmtree(destination)
    print("Creating new public directory")
    os.mkdir(destination)


def copy_files_recursive(source, destination):
    if not os.path.exists(destination):
        print(f"Path {destination} created")
        os.mkdir(destination)
    for entry in os.listdir(source):
        source_path = os.path.join(source, entry)
        if os.path.isfile(source_path):
            print(f"File at: {source_path} copied to {destination}")
            shutil.copy(source_path, destination)
        else:
            destination_path = os.path.join(destination, entry)
            copy_files_recursive(source_path, destination_path)
