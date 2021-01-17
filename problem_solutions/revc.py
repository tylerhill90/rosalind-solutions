#!/usr/bin/env python3
"""
http://rosalind.info/problems/revc/
Problem
In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.

The reverse complement of a DNA string s is the string sc formed by reversing the symbols of s, then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").

Given: A DNA string s of length at most 1000 bp.

Return: The reverse complement sc of s.

Sample Dataset
AAAACCCGGT
Sample Output
ACCGGGTTTT
"""

import os
import sys


def reverse_complement(dna):
    rc = ''
    for nuc in dna:
        if nuc == 'A':
            rc += 'T'
        elif nuc == 'T':
            rc += 'A'
        elif nuc == 'G':
            rc += 'C'
        elif nuc == 'C':
            rc += 'G'

    return rc[::-1]


def main():
    try:
        file_name = os.path.basename(__file__)[:-3]
        data_set_name = f'datasets/rosalind_{file_name}.txt'
        with open(os.path.join(os.pardir, data_set_name), 'r') as file:
            data = file.read()
            answer = reverse_complement(data)

        answer_name = f'answers/{file_name}.txt'
        with open(os.path.join(os.pardir, answer_name), 'w') as file:
            file.write(answer)

    except (FileNotFoundError):
        print('File not found.')


if __name__ == '__main__':
    main()

    assert reverse_complement('AAAACCCGGT') == 'ACCGGGTTTT'