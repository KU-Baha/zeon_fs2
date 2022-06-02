import os
from pathlib import Path


def del_file(*args) -> bool:
    if len(args) != 1:
        print("Write 1 argument!")
        return False

    file_path = args[0]

    if not Path(file_path).exists():
        print("File does not exists!")
        return False

    if Path(file_path).is_dir():
        print("You can't delete directory!")
        return False

    os.remove(file_path)
    print("Success")
    return True
