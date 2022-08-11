from commands.info import info_helper
from helper.helper import file_list, init_fs, add_file, del_file

commands_list = {
    'init': init_fs,
    'list': file_list,
    'add': add_file,
    'del': del_file,
    'info': info_helper,
}
