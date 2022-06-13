# import os
# from pathlib import Path
#
# from helper.helper import get_data_by_key
# from treelib import Node, Tree
#
data = [
    "62893484c3df2321c57ec12d50c3ab1695c1cb97,197,/command/test.py",
    "da39a3ee5e6b4b0d3255bfef95601890afd80709,0,/glob/test.py",
    "da39a3ee5e6b4b0d3255bfef95601890afd8s709,50,/glob/gg/ff/tess.py",
    "da39a3ee5e6b4b0d3255bfef95601890afd807109,0,/glob/gng/test.py",
]


def create_tree(path, fs):
    root = fs
    if root in fs:
        root[path] = fs
    root = {}
    return root


fs = {}
 
print(create_tree(data, fs))
# result = {
#     '/': {'parent': None},
#     'home': {'parent': '/'},
#     'baha': {'parent': 'home'},
#     'test.py': {'parent': 'baha'},
#     'command': {'parent': '/'},
#     'my.txt': {'parent': 'command'}
# }
#
#
# # def list_files(startpath):
# #     for i in os.walk(startpath):
# #         print(i)
# # for root, dirs, files in os.walk(startpath):
# #     level = root.replace(startpath, '').count(os.sep)
# #     indent = ' ' * 4 * (level)
# #     print('{}{}/'.format(indent, os.path.basename(root)))
# #     subindent = ' ' * 4 * (level + 1)
# #     for f in files:
# #         print('{}{}'.format(subindent, f))
#
# # for i in data:
# #     file_info = get_data_by_key(i.split(',')[0], data)
#
# # list_files('commands/')
#
# # my_tree = {}
# #
# # def get_parent(path, size):
# #     parent = Path(path).parent
# #     level = " " * 2 * path.count('/')
# #     if path != '/':
# #         get_parent(str(parent), size)
# #         print(f" {level} ./{Path(path).name}")
# #         return 0
#
# # for i in data:
# #     file_info = get_data_by_key(i.split(',')[0], data)
# #     get_parent(file_info.get('file_name'), file_info.get('file_size'))
# def some_function(paths):
#     my_path = []
#     for path in paths:
#         # file_path = path.get('file_name').split('/')[1:]
#         file_path = path.get('file_name')
#         file_size = path.get('file_size')
#         print(file_path, file_size)
#         p = Path(file_path)
#         while len(str(p.parent.absolute())) > 1:
#             my_path.append([str(p, file_size)])
#             p = p.parent.absolute()
#         # for directory in file_path[:-1]:
#         #     print(directory)
#         # if my_path.get(directories[0]):
#         #     my_data = [my_path.get(directories[0])[0], my_path.get(directories[0])[1], (directories[-1])]
#         #     my_path.update({directories[0]: my_data})
#         #     continue
#         # if len(directories) <= 1:
#         #     my_path.update({'/': directories})
#         #     continue
#         # my_path.update({directories[0]: [directories[1:-1], directories[-1]]})
# #
# #     return my_path
# #
# #
# directories = []
# #
# for i in data:
#     file_info = get_data_by_key(i.split(',')[0], data)
#     directories.append(file_info)
#
# print(some_function(directories))
#
# # print(my_tree)
#
# # tree = Tree()
# # for i in result:
# #     tree.create_node(f'/{i}', i, parent=result[i]['parent'])  # root node
# # tree.create_node(None, None, parent=None)
# # tree.create_node("Baha", "baha", parent=None)
# # tree.create_node("DJ", "dj", parent='baha')
# # tree.create_node('Home', 'home', parent=None)  # root node
# # tree.create_node("Baha", "baha", parent="home")
# # tree.create_node("Bill", "bill", parent="harry")
# # tree.create_node("Diane", "diane", parent="jane")
# # tree.create_node("Mary", "mary", parent="diane")
# # tree.create_node("Mark", "mark", parent="jane")
# # tree.show()
