import os
import shutil
from pathlib import Path

BASE_FS_PATH = 'zeon_fs3'


def check_file(file_path: str, dir_path: str = '') -> bool:
    if not Path(os.path.join(dir_path, file_path)).exists():
        return False

    return True


def add_file(dir_path, *args) -> bool:
    if not len(args) == 1:
        print("Command 'add' take 1 argument - file path!")
        return False

    file_path = args[0]
    base_dir_path = os.path.join(dir_path, BASE_FS_PATH)

    if not check_file(file_path, dir_path):
        print("File not found!")
        return False

    file_name = Path(file_path).name

    if check_file(file_name, base_dir_path):
        print('File already exists!')
        return False

    shutil.copyfile(file_path, f"{base_dir_path}/{file_name}")
    print("Success added")


def del_file(dir_path, *args) -> bool:
    if len(args) != 1:
        print("Command 'del' take 1 argument - file path!")
        return False

    file_path = f"{dir_path}/{BASE_FS_PATH}/{args[0]}"

    if not check_file(file_path):
        print("File not found!")
        return False

    os.remove(file_path)
    print("The file has been deleted")
    return True


def init_fs(dir_path, *args) -> bool:
    if len(args) != 0:
        print("Command 'init' doesn't take arguments!")
        return False

    fs_path = os.path.join(dir_path, BASE_FS_PATH)

    if check_file(fs_path):
        print("FS already initialized!")
        return False

    os.makedirs(fs_path, exist_ok=True)
    print("FS success initialized!")
    return True


def file_list(dir_path, *args) -> list:
    if len(args) != 0:
        print("Command 'list' doesn't take arguments!")
        return []

    fs_path = os.path.join(dir_path, BASE_FS_PATH)

    if not Path(fs_path).exists():
        print("FS not initialized!")
        return []

    data = os.listdir(fs_path)

    print(f"Files: {len(data)}\n")

    for file_name in data:
        print(file_name)

    return os.listdir(fs_path)
