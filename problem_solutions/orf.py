#!/usr/bin/env python3
"""
http://rosalind.info/problems/orf/
Problem
Either strand of a DNA double helix can serve as the coding strand for RNA transcription. Hence, a given DNA string implies six total reading frames, or ways in which the same region of DNA can be translated into amino acids: three reading frames result from reading the string itself, whereas three more result from reading its reverse complement.

An open reading frame (ORF) is one which starts from the start codon and ends by stop codon, without any other stop codons in between. Thus, a candidate protein string is derived by translating an open reading frame into amino acids until a stop codon is reached.

Given: A DNA string s of length at most 1 kbp in FASTA format.

Return: Every distinct candidate protein string that can be translated from ORFs of s. Strings can be returned in any order.

Sample Dataset
>Rosalind_99
AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG
Sample Output
MLLGSFRLIPKETLIQVAGSSPCNLS
M
MGMTPRLGLESLLE
MTPRLGLESLLE
"""


import os
import re

from revc import reverse_complement as revc
from rna import transcribe
from prot import lookup


def get_seq(data):
    match = re.search(r'\n[ACGT\n]+', data)
    return match.group().replace('\n', '')


def find_orfs(seq):
    rc_seq = revc(seq)
    seq, rc_seq = transcribe(seq), transcribe(rc_seq)

    orfs = []
    for rna in [seq, rc_seq]:
        for i in range(3):
            orf_found = False
            prot_seq = ''
            sub_orfs = []  # Keep track of overlapping ORFs
            for x in range(i, len(rna[i:]) - len(rna[i:]) % 3, 3):
                codon = rna[x:x+3]
                aa = lookup(codon)
                if codon == 'AUG':
                    if not orf_found:
                        orf_found = True
                    else:
                        sub_orfs.append(len(prot_seq))
                if orf_found and aa != 'Stop':
                    prot_seq += aa
                elif aa == 'Stop' and orf_found:
                    orfs.append(prot_seq)
                    # Append any sub ORFs
                    if sub_orfs:
                        [orfs.append(prot_seq[z:]) for z in sub_orfs]
                    orf_found = False
                    prot_seq = ''
                    sub_orfs = []

    return set(orfs)


def main():
    try:
        file_name = os.path.basename(__file__)[:-3]
        data_set_name = f'datasets/rosalind_{file_name}.txt'
        with open(os.path.join(os.pardir, data_set_name), 'r') as file:
            data = file.read()

        seq = get_seq(data)
        answer = find_orfs(seq)

        answer_name = f'answers/{file_name}.txt'
        with open(os.path.join(os.pardir, answer_name), 'w') as file:
            for x, prot in enumerate(answer):
                if x != len(answer) - 1:
                    file.write(f'{prot}\n')
                else:
                    file.write(prot)

    except (FileNotFoundError):
        print('File not found.')


if __name__ == '__main__':
    main()

    sample = '''>Rosalind_99
AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG'''

    expected_output = '''MLLGSFRLIPKETLIQVAGSSPCNLS
M
MGMTPRLGLESLLE
MTPRLGLESLLE'''

    assert find_orfs(get_seq(sample)) == set(expected_output.split())
