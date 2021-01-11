#!/usr/bin/env python3
"""
http://rosalind.info/problems/hamm/
Problem

Figure 2. The Hamming distance between these two strings is 7. Mismatched symbols are colored red.
Given two strings s and t of equal length, the Hamming distance between s and t, denoted dH(s,t), is the number of corresponding symbols that differ in s and t. See Figure 2.

Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).

Return: The Hamming distance dH(s,t).

Sample Dataset
GAGCCTACTAACGGGAT
CATCGTAATGACGGCCT
Sample Output
7
"""


import os
import sys


def hamm(seq1, seq2):
    return sum([1 for x in range(len(seq1)) if seq1[x] != seq2[x]])


def main():
    try:
        file_name = os.path.basename(__file__)[:-3]
        data_set_name = f'datasets/rosalind_{file_name}.txt'
        with open(os.path.join(os.pardir, data_set_name), 'r') as file:
            data = file.read().split()

        answer = hamm(data[0], data[1])
        print(answer)

        answer_name = f'answers/{file_name}.txt'
        with open(os.path.join(os.pardir, answer_name), 'w') as file:
            file.write(str(answer))

    except (FileNotFoundError):
        print('File not found.')


if __name__ == '__main__':
    main()

    sample = """GAGCCTACTAACGGGAT
CATCGTAATGACGGCCT"""
    data = sample.split()

    assert hamm(data[0], data[1]) == 7
