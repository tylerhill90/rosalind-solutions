#!/usr/bin/env python3
"""
http://rosalind.info/problems//
Problem
A matrix is a rectangular table of values divided into rows and columns. An m×n matrix has m rows and n columns. Given a matrix A, we write Ai,j to indicate the value found at the intersection of row i and column j.

Say that we have a collection of DNA strings, all having the same length n. Their profile matrix is a 4×n matrix P in which P1,j represents the number of times that 'A' occurs in the jth position of one of the strings, P2,j represents the number of times that C occurs in the jth position, and so on (see below).

A consensus string c is a string of length n formed from our collection by taking the most common symbol at each position; the jth symbol of c therefore corresponds to the symbol having the maximum value in the j-th column of the profile matrix. Of course, there may be more than one most common symbol, leading to multiple possible consensus strings.

DNA Strings	
A T C C A G C T
G G G C A A C T
A T G G A T C T
A A G C A A C C
T T G G A A C T
A T G C C A T T
A T G G C A C T

Profile	
A   5 1 0 0 5 5 0 0
C   0 0 1 4 2 0 6 1
G   1 1 6 3 0 1 0 0
T   1 5 0 0 0 1 1 6

Consensus
A T G C A A C T

Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.

Return: A consensus string and profile matrix for the collection. (If several possible consensus strings exist, then you may return any one of them.)

Sample Dataset
>Rosalind_1
ATCCAGCT
>Rosalind_2
GGGCAACT
>Rosalind_3
ATGGATCT
>Rosalind_4
AAGCAACC
>Rosalind_5
TTGGAACT
>Rosalind_6
ATGCCATT
>Rosalind_7
ATGGCACT
Sample Output
ATGCAACT
A: 5 1 0 0 5 5 0 0
C: 0 0 1 4 2 0 6 1
G: 1 1 6 3 0 1 0 0
T: 1 5 0 0 0 1 1 6
"""


import os
import re


def get_seqs(data):
    matches = re.findall(r'\n[ACGT\n]+', data)
    return [m.replace('\n', '') for m in matches]


def build_profile(seqs):
    # Check to see if seqs are all of the same length
    n = len(seqs[0])
    if not sum([1 for x in seqs if len(x) == n]) == len(seqs):
        return None

    profile = {
        'A': [0 for x in range(n)],
        'C': [0 for x in range(n)],
        'G': [0 for x in range(n)],
        'T': [0 for x in range(n)]
    }

    for seq in seqs:
        for i, nuc in enumerate(seq):
            if nuc == 'A':
                profile['A'][i] += 1
            elif nuc == 'C':
                profile['C'][i] += 1
            elif nuc == 'G':
                profile['G'][i] += 1
            elif nuc == 'T':
                profile['T'][i] += 1

    return profile


def get_consensus(profile):
    n = len(profile['A'])
    consensus = ''
    for i in range(n):
        max = 0
        nuc = ''
        for key, value in profile.items():
            if value[i] > max:
                max = value[i]
                nuc = key
        consensus += nuc

    return consensus


def format_answer(consensus, profile):
    answer = consensus + '\n'
    for key, value in profile.items():
        nums = ''
        for num in value:
            nums += f'{num} '
        answer += f'{key}: {nums[:-1]}'
        answer += '\n'

    return answer[:-1]


def main():
    try:
        file_name = os.path.basename(__file__)[:-3]
        data_set_name = f'datasets/rosalind_{file_name}.txt'
        with open(os.path.join(os.pardir, data_set_name), 'r') as file:
            data = file.read()

            seqs = get_seqs(data)
            profile = build_profile(seqs)
            consensus = get_consensus(profile)
            answer = format_answer(consensus, profile)

        answer_name = f'answers/{file_name}.txt'
        with open(os.path.join(os.pardir, answer_name), 'w') as file:
            file.write(answer)

    except (FileNotFoundError):
        print('File not found.')


if __name__ == '__main__':
    main()

    sample = '''>Rosalind_1
ATCCAGCT
>Rosalind_2
GGGCAACT
>Rosalind_3
ATGGATCT
>Rosalind_4
AAGCAACC
>Rosalind_5
TTGGAACT
>Rosalind_6
ATGCCATT
>Rosalind_7
ATGGCACT'''

    expected_output = '''ATGCAACT
A: 5 1 0 0 5 5 0 0
C: 0 0 1 4 2 0 6 1
G: 1 1 6 3 0 1 0 0
T: 1 5 0 0 0 1 1 6'''

    seqs = get_seqs(sample)
    profile = build_profile(seqs)
    consensus = get_consensus(profile)
    answer = format_answer(consensus, profile)

    assert answer == expected_output
