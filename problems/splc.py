#!/usr/bin/env python3
"""
http://rosalind.info/problems/splc/
Problem
After identifying the exons and introns of an RNA string, we only need to delete the introns and concatenate the exons to form a new string ready for translation.

Given: A DNA string s (of length at most 1 kbp) and a collection of substrings of s acting as introns. All strings are given in FASTA format.

Return: A protein string resulting from transcribing and translating the exons of s. (Note: Only one solution will exist for the dataset provided.)

Sample Dataset
>Rosalind_10
ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG
>Rosalind_12
ATCGGTCGAA
>Rosalind_15
ATCGGTCGAGCGTGT
Sample Output
MVYIADKQHVASREAYGHMFKVCA
"""


import os
import re

from cons import get_seqs
from rna import transcribe
from prot import translate


def splice(seqs):
    s = seqs[0]
    introns = seqs[1:]
    for i in introns:
        matches = re.finditer(i, s)
        offset = 0
        for m in matches:
            s = s[:m.start() + offset] + s[m.end() + offset:]
            offset += m.end() - m.start()
    
    return translate(transcribe(s))


def main():
    try:
        file_name = os.path.basename(__file__)[:-3]
        data_set_name = f'datasets/rosalind_{file_name}.txt'
        with open(os.path.join(os.pardir, data_set_name), 'r') as file:
            data = file.read()
        
        seqs = get_seqs(data)
        answer = splice(seqs)

        answer_name = f'answers/{file_name}.txt'
        with open(os.path.join(os.pardir, answer_name), 'w') as file:
            file.write(answer)

    except (FileNotFoundError):
        print('File not found.')


if __name__ == '__main__':
    main()

    sample = '''>Rosalind_10
ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG
>Rosalind_12
ATCGGTCGAA
>Rosalind_15
ATCGGTCGAGCGTGT'''

    expected_output = 'MVYIADKQHVASREAYGHMFKVCA'

    assert splice(get_seqs(sample)) == expected_output
