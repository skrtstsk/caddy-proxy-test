import argparse
import os

def check_folder(folder_path, folder_size_limit):
    for root, _, files in os.walk(folder_path):
        for file in files:
            complete_path = os.path.join(root, f)
            try:
                if os.path.getsize(complete_path) > folder_size_limit:
                    print(f'{complete_path} beats the limit.')
                    os.remove(complete_path)
            except FileNotFoundError:
                    print("This file does not exist"+ complete_path)


parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)

parser.add_argument("path", help="Folder location")
parser.add_argument("limit", help="Folder size limit")

args = parser.parse_args()
print(args)