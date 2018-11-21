import shutil


def copy_files(files, destination_folder):
    for f in files:
        shutil.copy(f, destination_folder)
