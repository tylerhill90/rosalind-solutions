#!/usr/bin/env python3
"""
http://rosalind.info/problems/revp/
Problem

Figure 2. Palindromic recognition site
A DNA string is a reverse palindrome if it is equal to its reverse complement. For instance, GCATGC is a reverse palindrome because its reverse complement is GCATGC. See Figure 2.

Given: A DNA string of length at most 1 kbp in FASTA format.

Return: The position and length of every reverse palindrome in the string having length between 4 and 12. You may return these pairs in any order.

Sample Dataset
>Rosalind_24
TCAATGCATGCGGGTCTATATGCAT
Sample Output
4 6
5 4
6 6
7 4
17 4
18 4
20 6
21 4
"""


import os
import re

from revc import reverse_complement as revc


def extract_seq(data):
    return re.search(r'\n[ACGT\n]*', data).group().replace('\n', '')


def find_rev_pals(seq, n=4, m=12):
    answer = []
    for i in range(len(seq) - n + 1):
        for x in range(n, m + 1):
            if x + i <= len(seq):
                substring = seq[i:i+x]
                if substring in revc(substring):
                    answer.append(
                        (i+1, x)
                    )

    return answer


def format_answer(data):
    answer = ''
    for x in data:
        answer += f'{x[0]} {x[1]}\n'

    return answer[:-1]


def main():
    try:
        file_name = os.path.basename(__file__)[:-3]
        data_set_name = f'datasets/rosalind_{file_name}.txt'
        with open(os.path.join(os.pardir, data_set_name), 'r') as file:
            data = file.read()

        seq = extract_seq(data)
        answer = find_rev_pals(seq)

        answer_name = f'answers/{file_name}.txt'
        with open(os.path.join(os.pardir, answer_name), 'w') as file:
            file.write(format_answer(answer))

    except (FileNotFoundError):
        print('File not found.')


if __name__ == '__main__':
    main()

    sample = '''>Rosalind_24
TCAATGCATGCGGGTCTATATGCAT'''

    expected_output = '''4 6
5 4
6 6
7 4
17 4
18 4
20 6
21 4'''

    assert format_answer(find_rev_pals(extract_seq(sample))) == expected_output
