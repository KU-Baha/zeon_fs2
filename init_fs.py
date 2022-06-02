import os
from pathlib import Path
from config import BASE_DIR


def init_fs(*args) -> bool:
    if len(args) != 0:
        print("Command init doesn't take any arguments!")
        return False

    if Path(BASE_DIR).exists():
        print("Already exists")
        return False

    os.makedirs(BASE_DIR)
    print("Success")

    return True
