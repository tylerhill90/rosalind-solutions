#!/usr/bin/env python3
"""
http://rosalind.info/problems/tran/
Problem
For DNA strings s1 and s2 having the same length, their transition/transversion ratio R(s1,s2) is the ratio of the total number of transitions to the total number of transversions, where symbol substitutions are inferred from mismatched corresponding symbols as when calculating Hamming distance (see “Counting Point Mutations”).

Given: Two DNA strings s1 and s2 of equal length (at most 1 kbp).

Return: The transition/transversion ratio R(s1,s2).

Sample Dataset
>Rosalind_0209
GCAACGCACAACGAAAACCCTTAGGGACTGGATTATTTCGTGATCGTTGTAGTTATTGGA
AGTACGGGCATCAACCCAGTT
>Rosalind_2200
TTATCTGACAAAGAAAGCCGTCAACGGCTGGATAATTTCGCGATCGTGCTGGTTACTGGC
GGTACGAGTGTTCCTTTGGGT
Sample Output
1.21428571429
"""


import os

from cons import get_seqs


def tran_ratio(s1, s2):
    transitions = [['A', 'G'], ['C', 'T']]
    transversions = [['A', 'C'], ['A', 'T'], ['C', 'G'], ['G', 'T']]
    n_transitions = 0.0
    n_transversions = 0.0

    for nuc_s1, nuc_s2 in zip(s1, s2):
        compare = [nuc_s1, nuc_s2]
        if sorted(compare) in transversions:
            n_transversions += 1
        elif sorted(compare) in transitions:
            n_transitions += 1
        else:
            pass

    return round(n_transitions / n_transversions, 11)


def main():
    try:
        file_name = os.path.basename(__file__)[:-3]
        data_set_name = f'datasets/rosalind_{file_name}.txt'
        with open(os.path.join(os.pardir, data_set_name), 'r') as file:
            data = file.read()

        (s1, s2) = get_seqs(data)
        answer = tran_ratio(s1, s2)

        answer_name = f'answers/{file_name}.txt'
        with open(os.path.join(os.pardir, answer_name), 'w') as file:
            file.write(str(answer))

    except (FileNotFoundError):
        print('File not found.')


if __name__ == '__main__':
    main()

    sample = '''>Rosalind_0209
GCAACGCACAACGAAAACCCTTAGGGACTGGATTATTTCGTGATCGTTGTAGTTATTGGA
AGTACGGGCATCAACCCAGTT
>Rosalind_2200
TTATCTGACAAAGAAAGCCGTCAACGGCTGGATAATTTCGCGATCGTGCTGGTTACTGGC
GGTACGAGTGTTCCTTTGGGT'''

    (s1, s2) = get_seqs(sample)

    assert tran_ratio(s1, s2) == 1.21428571429
