#!/usr/bin/env python3
"""
http://rosalind.info/problems/sseq/
Problem
A subsequence of a string is a collection of symbols contained in order (though not necessarily contiguously) in the string (e.g., ACG is a subsequence of TATGCTAAGATC). The indices of a subsequence are the positions in the string at which the symbols of the subsequence appear; thus, the indices of ACG in TATGCTAAGATC can be represented by (2, 5, 9).

As a substring can have multiple locations, a subsequence can have multiple collections of indices, and the same index can be reused in more than one appearance of the subsequence; for example, ACG is a subsequence of AACCGGTT in 8 different ways.

Given: Two DNA strings s and t (each of length at most 1 kbp) in FASTA format.

Return: One collection of indices of s in which the symbols of t appear as a subsequence of s. If multiple solutions exist, you may return any one.

Sample Dataset
>Rosalind_14
ACGTACGTGACG
>Rosalind_18
GTA
Sample Output
3 8 10
"""


import os
from cons import get_seqs
from time import clock


def spliced_motif(s, t):
    answer = [0]
    for motif_nuc in t:
        for i in range(answer[-1], len(s)):
            if motif_nuc == s[i]:
                answer.append(i + 1)
                break

    return answer[1:]


def main():
    try:
        file_name = os.path.basename(__file__)[:-3]
        data_set_name = f'datasets/rosalind_{file_name}.txt'
        with open(os.path.join(os.pardir, data_set_name), 'r') as file:
            data = file.read()

        seqs = get_seqs(data)
        s, t = seqs[0], seqs[1]
        answer = spliced_motif(s, t)

        answer_name = f'answers/{file_name}.txt'
        with open(os.path.join(os.pardir, answer_name), 'w') as file:
            for i in answer:
                if i != len(answer) - 1:
                    file.write(f'{str(i)} ')
                else:
                    file.write(f'{str(i)}')

    except (FileNotFoundError):
        print('File not found.')


if __name__ == '__main__':
    main()
