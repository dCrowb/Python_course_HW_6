import sys
import os
import re

FILES_FORMAT = {'images': ('JPEG', 'PNG', 'JPG', 'SVG', 'BMP'),
                'files': ('AVI', 'MP4', 'MOV', 'MKV'),
                'documents': ('DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX'),
                'music': ('MP3', 'OGG', 'WAV', 'AMR'),
                'archives': ('ZIP', 'GZ', 'TAR', 'RAR')
                }

CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"

TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

DICTIONARY_FOR_TRANSLITERATION = {}
if __name__ == '__main__':
    for cyr, tran in zip(CYRILLIC_SYMBOLS, TRANSLATION):
        DICTIONARY_FOR_TRANSLITERATION[ord(cyr)] = tran
        DICTIONARY_FOR_TRANSLITERATION[ord(cyr.upper())] = tran.upper()


def translate_file_name(name):
    file_name, file_extention = os.path.splitext(name)
    translated_name = ''
    pattern = r'[a-zA-Z0-9]'
    for symbol in file_name:
        if re.search(pattern, symbol) != None:
            translated_name += symbol
        elif ord(symbol) in DICTIONARY_FOR_TRANSLITERATION:
            translated_name += DICTIONARY_FOR_TRANSLITERATION[ord(symbol)]
        else:
            translated_name += '_'
    return translated_name + file_extention


def file_format_sorting(file):
    normalized_file_name = translate_file_name(file)
    for key, value in FILES_FORMAT.items():
        if normalized_file_name.upper().endswith(value):
            sorted_files[key].append(normalized_file_name)
            return
    sorted_files['unknown_extensions'].append(normalized_file_name)
    return


def tree_directory(path):
    for file in os.scandir(path):
        if file.is_dir():
            tree_directory(file.path)
        else:
            file_format_sorting(file.name)
    return


def get_path():
    if len(sys.argv) == 2:
        file, path = sys.argv
        return path
    else:
        flag_error = '****ERROR****\nThe program work with only parameter path.\nFor example: main.py /path/to/directiry\nTry run again'
        print(flag_error)


if __name__ == '__main__':
    sorted_files = {'images': [],
                    'files': [],
                    'documents': [],
                    'music': [],
                    'archives': [],
                    'unknown_extensions': []
                    }
    PATH = get_path()

    if PATH != None:
        tree_directory(PATH)
        for el, value in sorted_files.items():
            print(el)
            print(value)
    # print(DICTIONARY_FOR_TRANSLITERATION)
