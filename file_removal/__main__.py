import os
from json import load

from _types import Config
from file_removal.checks import is_target_file

config_file = open("config.json")
config = Config(**load(config_file))
config_file.close()


def remove_file(root_dir: str):
    for file_or_dir in os.listdir(root_dir):
        current_path = os.path.join(root_dir, file_or_dir)
        if os.path.isfile(current_path) and is_target_file(file_or_dir, config.file_ext):
            # os.remove(current_path)
            print(f"Removing {file_or_dir}...")
        elif os.path.isdir(current_path):
            remove_file(current_path)


if __name__ == '__main__':
    remove_file(config.root_dir)
    print("Done!")
