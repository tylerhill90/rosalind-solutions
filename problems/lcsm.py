#!/usr/bin/env python3
"""
http://rosalind.info/problems/lcsm/
Problem
A common substring of a collection of strings is a substring of every member of the collection. We say that a common substring is a longest common substring if there does not exist a longer common substring. For example, "CG" is a common substring of "ACGTACGT" and "AACCGTATA", but it is not as long as possible; in this case, "CGTA" is a longest common substring of "ACGTACGT" and "AACCGTATA".

Note that the longest common substring is not necessarily unique; for a simple example, "AA" and "CC" are both longest common substrings of "AACC" and "CCAA".

Given: A collection of k (k≤100) DNA strings of length at most 1 kbp each in FASTA format.

Return: A longest common substring of the collection. (If multiple solutions exist, you may return any single solution.)

Sample Dataset
>Rosalind_1
GATTACA
>Rosalind_2
TAGACCA
>Rosalind_3
ATACA
Sample Output
AC
"""


import os
import re
from math import inf
from suffix_trees import STree

from cons import get_seqs


def brute_lcsm(seqs):
    # Find the shortest sequence, save it, and remove it from the list
    index = None
    min_len = inf
    for x, seq in enumerate(seqs):
        n = len(seq)
        if n < min_len:
            min_len = n
            index = x
    shortest = seqs[index]
    del seqs[index]

    # Compare decrementing slices of the shortest seq, via a sliding window,
    # to the rest of the sequences and return the slice if it is present in all
    # sequences
    longest_common_substrings = []
    n = len(seqs)
    for i in range(min_len, 0, -1):
        if longest_common_substrings:
            return longest_common_substrings
        for s in range(min_len - i + 1):
            substring = shortest[s:s + i]
            count = 0
            for seq in seqs:
                for x in range(len(seq) - i + 1):
                    if seq[x:x + i] == substring:
                        count += 1
                        break
            if count == n:
                longest_common_substrings.append(substring)


def lcsm(seqs):
    gen_suf_tree = STree.STree(seqs)
    return gen_suf_tree.lcs()


def main():
    try:
        file_name = os.path.basename(__file__)[:-3]
        data_set_name = f'datasets/rosalind_{file_name}.txt'
        with open(os.path.join(os.pardir, data_set_name), 'r') as file:
            data = file.read()

        seqs = get_seqs(data)
        answer = lcsm(seqs)

        answer_name = f'answers/{file_name}.txt'
        with open(os.path.join(os.pardir, answer_name), 'w') as file:
            file.write(answer)

    except (FileNotFoundError):
        print('File not found.')


if __name__ == '__main__':
    main()

    sample = '''Sample Dataset
>Rosalind_1
GATTACA
>Rosalind_2
TAGACCA
>Rosalind_3
ATACA'''


    assert lcsm(get_seqs(sample)) in ['TA', 'AC', 'CA']
