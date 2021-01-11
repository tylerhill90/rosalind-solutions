#!/usr/bin/env python3
"""
http://rosalind.info/problems//

"""


import os


def main():
    try:
        file_name = os.path.basename(__file__)[:-3]
        data_set_name = f'datasets/rosalind_{file_name}.txt'
        with open(os.path.join(os.pardir, data_set_name), 'r') as file:
            data = file.read()

        answer_name = f'answers/{file_name}.txt'
        with open(os.path.join(os.pardir, answer_name), 'w') as file:
            file.write()

    except (FileNotFoundError):
        print('File not found.')


if __name__ == '__main__':
    main()
