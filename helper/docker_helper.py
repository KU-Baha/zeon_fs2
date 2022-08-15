import os
import glob
import json

from pathlib import Path

from helper.helper import BASE_FS_PATH


def get_meta(dir_path, *args):
    init_path = os.path.join(dir_path, BASE_FS_PATH)
    objects_path = f'{init_path}/objects'

    if not Path(init_path).exists():
        print("FS not initialized!")
        return False

    list_of_files = glob.glob(f'{objects_path}/*')
    latest_file = max(list_of_files, key=os.path.getctime)
    meta_data = {'name': BASE_FS_PATH, 'file_count': len(list_of_files), 'last_updated_file': latest_file.split('/')[-1]}

    with open(f'{init_path}/meta.txt', 'w') as meta_file:
        json.dump(meta_data, meta_file)

    with open(f'{init_path}/meta.html', 'w') as meta_html:
        meta_html.write(f"""
<html>
    <head>
        <title>Meta</title>
    </head>
    <body>
        <h1>Data</h1>
        <p>Name: {meta_data.get('name')}</p>
        <p>File count: {meta_data.get('file_count')}</p>
        <p>Last updated file: {meta_data.get('last_updated_file')}</p>
    </body>
</html>
""")
    return True