import os
import shutil
from pathlib import Path
from hashlib import sha1

BASE_FS_PATH = '.zeon_fs2'
BASE_FS_CHILDREN_DIR = f'{BASE_FS_PATH}/objects'
DATABASE_PATH = f'{BASE_FS_PATH}/index'


def check_file(file_path: str, dir_path: str = '') -> bool:
    if not Path(os.path.join(dir_path, file_path)).exists():
        return False

    return True


def check_init(dir_path: str) -> bool:
    while len(str(dir_path)) != 1:
        path = Path(dir_path)
        if Path(os.path.join(dir_path, BASE_FS_PATH)).exists():
            print(f"Directory initialized in {dir_path}")
            return True
        dir_path = path.parent.absolute()
    print("Directory not initialized")
    return False


def add_file(dir_path, *args) -> bool:
    if not len(args) == 1:
        print("Command 'add' take 1 argument - file path!")
        return False

    file_path = args[0]

    init_path = os.path.join(dir_path, BASE_FS_PATH)
    base_dir_path = os.path.join(dir_path, BASE_FS_CHILDREN_DIR)

    if not check_file(init_path):
        print("FS not initialized!")
        return False

    if not check_file(file_path, dir_path):
        print("File not found!")
        return False

    file_name = Path(file_path).name
    file_hash = hash_file(file_path)

    if check_file(file_name, base_dir_path):
        print('File already exists!')
        return False

    database = database_list()

    if not add_to_database(file_hash, file_name, database):
        print("File already exists in database!")
        return False

    shutil.copyfile(file_path, f"{base_dir_path}/{file_hash}")

    print("Success added")
    return True


def del_file(dir_path, *args) -> bool:
    if len(args) != 1:
        print("Command 'del' take 1 argument - file path!")
        return False

    init_path = os.path.join(dir_path, BASE_FS_PATH)
    file_path = args[0]
    database = database_list()

    data = get_data_by_key(file_path, database)

    if not data:
        print("File not found!")
        return False

    file_name = data.get('file_name')
    file_hash = data.get('file_hash')

    if not check_file(init_path):
        print("FS not initialized!")
        return False

    base_dir_path = f"{dir_path}/{BASE_FS_CHILDREN_DIR}/{file_hash}"

    if not check_file(base_dir_path):
        print("File not found!")
        return False

    if not delete_from_database(file_hash, file_name, database):
        print("File not found in database!")
        return False

    os.remove(base_dir_path)
    print("The file has been deleted")
    return True


def init_fs(dir_path, *args) -> bool:
    if len(args) != 0:
        print("Command 'init' doesn't take arguments!")
        return False

    init_path = os.path.join(dir_path, BASE_FS_PATH)
    fs_path = os.path.join(dir_path, BASE_FS_CHILDREN_DIR)

    if check_file(init_path):
        print("FS already initialized!")
        return False

    os.makedirs(fs_path, exist_ok=True)
    print("FS success initialized!")

    open(DATABASE_PATH, 'wb').close()
    print("Database success created!")

    return True


def file_list(dir_path, *args) -> list:
    if len(args) != 0:
        print("Command 'list' doesn't take arguments!")
        return []

    init_path = os.path.join(dir_path, BASE_FS_PATH)
    base_dir_path = os.path.join(dir_path, BASE_FS_CHILDREN_DIR)

    if not Path(init_path).exists():
        print("FS not initialized!")
        return []

    database = database_list()
    data = os.listdir(base_dir_path)

    print(f"Files: {len(data)}\n")

    for file_hash in data:
        data = get_data_by_key(file_hash, database)
        if data:
            print(data.get('file_name'))

    return data


def database_list() -> list:
    if not check_file(DATABASE_PATH):
        return []

    with open(DATABASE_PATH, "r") as file:
        return file.read().split('\n')


def check_in_database(new_file_hash: str, new_file_name: str, database: list) -> bool:
    for line in database:

        if new_file_hash in line or new_file_name in line:
            return True

    return False


def add_to_database(new_file_hash: str, new_file_name: str, database: list) -> bool:
    if check_in_database(new_file_hash, new_file_name, database):
        return False

    with open(DATABASE_PATH, 'w') as file:
        file.write('\n'.join(database))
        file.write(f"{new_file_hash}, {new_file_name}\n")

    return True


def delete_from_database(file_hash: str, file_name: str, database: list) -> bool:
    if not check_in_database(file_hash, file_name, database):
        return False

    for i in range(len(database)):
        if file_hash not in database[i] or file_name not in database[i]:
            continue

        del database[i]

        with open(DATABASE_PATH, 'w') as file:
            file.write('\n'.join(database))

        return True

    return False


def hash_file(file_path: str) -> str:
    if not check_file(file_path):
        return ''

    with open(file_path, "r") as file:
        return sha1(file.read()).hexdigest()


def get_data_by_key(key: str, database: list) -> dict:
    for line in database:
        if key not in line:
            continue

        data = line.split(',')

        return {'file_hash': data[0], 'file_name': data[1]}
    return {}
