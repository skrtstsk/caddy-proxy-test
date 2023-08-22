import os
import shutil


def delete_large_folders(path, size_limit):
    for foldername, subfolders, filenames in os.walk(path):
        folder_size = 0
        for filename in filenames:
            filepath = os.path.join(foldername, filename)
            folder_size += os.path.getsize(filepath)
        if folder_size > size_limit * 1024:
            shutil.rmtree(foldername)
            print(foldername + " deleted")


delete_large_folders("C:/Users/katya/Downloads/test", 100)
