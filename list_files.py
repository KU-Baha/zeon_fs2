import os
from pathlib import Path

from config import BASE_DIR


def file_list(*args) -> list:
    if len(args) != 0:
        print("Command list doesn't take any arguments!")
        return []

    if not Path(BASE_DIR).exists():
        print("File doesn't initialized!")
        return []

    files = os.listdir(path=BASE_DIR)
    print(f"Files: {len(files)}\n")

    for file in files:
        print(file)

    return files
