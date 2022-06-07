# import pickle
from helper.helper import database_list, DATABASE_PATH
#
#
# for line in database_list():
#     data = line.split(', ')
#     if len(data) != 2:
#         break
#     file_hash, file_name = data
#     if file_hash == '1234':
#         print("Don't do it")'

with open(DATABASE_PATH, 'r') as file:
    print(file.read())

with open(DATABASE_PATH, 'a') as file:
    hashs = '214'
    name = 'text.txt'
    file.write(hashs)
