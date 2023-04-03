import sys
import os


def tree_directory(path):
    print(os.listdir(path))


def get_path():
    if len(sys.argv) == 2:
        file, path = sys.argv
        return path
    else:
        flag_error = 'The program work with only parameter path.\nFor example: main.py /path/to/directiry\nTry run again'
        return print(flag_error)


if __name__ == '__main__':
    PATH = get_path()
    tree_directory(PATH)
