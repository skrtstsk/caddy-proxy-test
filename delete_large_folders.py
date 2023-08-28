import os


def check_large_folders(path, size_limit):
    count = 0
    for foldername, subfolders, filenames in os.walk(path):
        folder_size = 0
        for filename in filenames:
            filepath = os.path.join(foldername, filename)
            folder_size += os.path.getsize(filepath)
        if folder_size > size_limit * 1024 * 1024:
            print(os.path.split(os.path.split(filepath)[0])[1], "500")
        else:
            count += 1
    if count == 0:
        return 200


check_large_folders("C:/Users/katya/Downloads/test", 1)  # размер в Мб
