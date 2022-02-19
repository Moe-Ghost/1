# import errno
# import os


# def path_maker(string):   
#     p = string[0]
#     if len(p) == 2 and ':' in p: 
#         for x in string[1:]:
#             p += f'\\{x}'
#             try:
#                 os.mkdir(p)
#             except OSError as err:
#                 if err.errno != errno.EEXIST:
#                     return False
#                 continue
#         return True
#     return False


# if __name__ == "__main__":
#     string = input('Enter the path: ')
#     print(path_maker(string))


import os


def path_maker():
    path = input('Enter path: ')
    dir_names = path.split('\\')
    new_path = ''
    for name in dir_names:
        result = 1
        new_path += f'{name}\\'
        try:
            os.mkdir(new_path)
        except FileExistsError:
            result = -1
            continue
        except FileNotFoundError:
            return print(0)
        except PermissionError:
            continue
    return print(result)
        



if __name__ == '__main__':
    result = path_maker()
    if result == 1:
        print('ok')
    elif result == 0:
        print('There is already file with the same name as the folder name')
    else:
        print('incorrect tome name')
    