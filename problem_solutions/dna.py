#!/usr/bin/env python3
"""
http://rosalind.info/problems/dna/
Problem
A string is simply an ordered collection of symbols selected from some alphabet and formed into a word; the length of a string is the number of symbols that it contains.

An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."

Given: A DNA string s of length at most 1000 nt.

Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.

Sample Dataset
AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC
Sample Output
20 12 17 21
"""

import os

def count_nucs(string):
    a, c, g, t = 0, 0, 0, 0
    if len(string) <= 1000:
        for nuc in string:
            if nuc == 'A':
                a += 1
            elif nuc == 'C':
                c += 1
            elif nuc == 'G':
                g += 1
            elif nuc == 'T':
                t += 1
    
    return [a, c, g, t]

def main():
    try:
        file_name = os.path.basename(__file__)[:-3]
        data_set_name = f'datasets/rosalind_{file_name}.txt'
        with open(os.path.join(os.pardir, data_set_name), 'r') as file:
            data = file.read()
            answer = count_nucs(data)

        answer_name = f'answers/{file_name}.txt'
        with open(os.path.join(os.pardir, answer_name), 'w') as file:
            formatted_answer = ' '.join([str(count) for count in answer])
            file.write(formatted_answer)

    except (FileNotFoundError):
        print('File not found.')

if __name__ == '__main__':
    main()