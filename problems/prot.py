#!/usr/bin/env python3
"""
http://rosalind.info/problems/prot/
Problem
The 20 commonly occurring amino acids are abbreviated by using 20 letters from the English alphabet (all letters except for B, J, O, U, X, and Z). Protein strings are constructed from these 20 symbols. Henceforth, the term genetic string will incorporate protein strings along with DNA strings and RNA strings.

The RNA codon table dictates the details regarding the encoding of specific codons into the amino acid alphabet.

Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).

Return: The protein string encoded by s.

Sample Dataset
AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA
Sample Output
MAMAPRTEINSTRING
"""

import os


def lookup(query):
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

    return codon_table[query]


def translate(rna):
    prot = ''
    for i in range(0, len(rna), 3):
        codon = rna[i:i+3]
        aa = lookup(codon)
        if aa != 'Stop':
            prot += aa
        else:
            return prot

    return prot


def main():
    try:
        file_name = os.path.basename(__file__)[:-3]
        data_set_name = f'datasets/rosalind_{file_name}.txt'
        with open(os.path.join(os.pardir, data_set_name), 'r') as file:
            rna = file.read().strip('\n')

        answer = translate(rna)

        answer_name = f'answers/{file_name}.txt'
        with open(os.path.join(os.pardir, answer_name), 'w') as file:
            file.write(answer)

    except (FileNotFoundError):
        print('File not found.')


if __name__ == '__main__':
    main()

    sample = 'AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA'

    assert translate(sample) == 'MAMAPRTEINSTRING'
