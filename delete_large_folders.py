import os
import shutil
import logging

logging.basicConfig(level=logging.INFO, filename="C:/Users/katya/pythonProject/caddy-proxy-test/deleting.log", filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s", datefmt='%H:%M:%S')


def delete_large_folders(path, size_limit):
    for foldername, subfolders, filenames in os.walk(path):
        folder_size = 0
        for filename in filenames:
            filepath = os.path.join(foldername, filename)
            folder_size += os.path.getsize(filepath)
        if folder_size > size_limit * 1024:
            shutil.rmtree(foldername)
            logging.info("Deleted")
        else:
            logging.info("NOT deleted")

delete_large_folders("C:/Users/katya/Downloads/test", 1)
