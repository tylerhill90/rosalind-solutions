#!/usr/bin/env python3
"""
http://rosalind.info/problems/mrna/
Problem
For positive integers a and n, a modulo n (written amodn in shorthand) is the remainder when a is divided by n. For example, 29mod11=7 because 29=11×2+7.

Modular arithmetic is the study of addition, subtraction, multiplication, and division with respect to the modulo operation. We say that a and b are congruent modulo n if amodn=bmodn; in this case, we use the notation a≡bmodn.

Two useful facts in modular arithmetic are that if a≡bmodn and c≡dmodn, then a+c≡b+dmodn and a×c≡b×dmodn. To check your understanding of these rules, you may wish to verify these relationships for a=29, b=73, c=10, d=32, and n=11.

As you will see in this exercise, some Rosalind problems will ask for a (very large) integer solution modulo a smaller number to avoid the computational pitfalls that arise with storing such large numbers.

Given: A protein string of length at most 1000 aa.

Return: The total number of different RNA strings from which the protein could have been translated, modulo 1,000,000. (Don't neglect the importance of the stop codon in protein translation.)

Sample Dataset
MA
Sample Output
12
"""

import os


codon_table = {
    "UUU": "F",    "CUU": "L",    "AUU": "I",    "GUU": "V",
    "UUC": "F",    "CUC": "L",    "AUC": "I",    "GUC": "V",
    "UUA": "L",    "CUA": "L",    "AUA": "I",    "GUA": "V",
    "UUG": "L",    "CUG": "L",    "AUG": "M",    "GUG": "V",
    "UCU": "S",    "CCU": "P",    "ACU": "T",    "GCU": "A",
    "UCC": "S",    "CCC": "P",    "ACC": "T",    "GCC": "A",
    "UCA": "S",    "CCA": "P",    "ACA": "T",    "GCA": "A",
    "UCG": "S",    "CCG": "P",    "ACG": "T",    "GCG": "A",
    "UAU": "Y",    "CAU": "H",    "AAU": "N",    "GAU": "D",
    "UAC": "Y",    "CAC": "H",    "AAC": "N",    "GAC": "D",
    "UAA": "Stop", "CAA": "Q",    "AAA": "K",    "GAA": "E",
    "UAG": "Stop", "CAG": "Q",    "AAG": "K",    "GAG": "E",
    "UGU": "C",    "CGU": "R",    "AGU": "S",    "GGU": "G",
    "UGC": "C",    "CGC": "R",    "AGC": "S",    "GGC": "G",
    "UGA": "Stop", "CGA": "R",    "AGA": "R",    "GGA": "G",
    "UGG": "W",    "CGG": "R",    "AGG": "R",    "GGG": "G"
}

# Restructure the codon lookup table to be an amino acid lookup table of codons
aa_table = dict()
for key, val in codon_table.items():
    if val in aa_table:
        aa_table[val].append(key)
    else:
        aa_table[val] = [key]


def calc_n_rna_strings(prot_seq):
    prot_seq = [aa for aa in prot_seq] + ['Stop']
    codon_possibilities = [len(aa_table[aa]) for aa in prot_seq]
    n_seqs = 1
    for n in codon_possibilities:
        n_seqs *= n
    return n_seqs % 10**6


def main():
    try:
        file_name = os.path.basename(__file__)[:-3]
        data_set_name = f'datasets/rosalind_{file_name}.txt'
        with open(os.path.join(os.pardir, data_set_name), 'r') as file:
            prot_seq = file.readline().strip('\n')

        answer = calc_n_rna_strings(prot_seq)
        print(answer)

        answer_name = f'answers/{file_name}.txt'
        with open(os.path.join(os.pardir, answer_name), 'w') as file:
            file.write(str(answer))

    except (FileNotFoundError):
        print('File not found.')


if __name__ == '__main__':
    main()

    assert calc_n_rna_strings('MA') == 12
