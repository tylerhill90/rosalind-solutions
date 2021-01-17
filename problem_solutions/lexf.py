#!/usr/bin/env python3
"""
http://rosalind.info/problems/lexf/
Problem
Assume that an alphabet A has a predetermined order; that is, we write the alphabet as a permutation A=(a1,a2,…,ak), where a1<a2<⋯<ak. For instance, the English alphabet is organized as (A,B,…,Z).

Given two strings s and t having the same length n, we say that s precedes t in the lexicographic order (and write s<Lext) if the first symbol s[j] that doesn't match t[j] satisfies sj<tj in A.

Given: A collection of at most 10 symbols defining an ordered alphabet, and a positive integer n (n≤10).

Return: All strings of length n that can be formed from the alphabet, ordered lexicographically (use the standard order of symbols in the English alphabet).

Sample Dataset
A C G T
2
Sample Output
AA
AC
AG
AT
CA
CC
CG
CT
GA
GC
GG
GT
TA
TC
TG
TT
"""


import os


def lexf(symbols, n):
    words = symbols
    while n - 1:
        temp = []
        for word in words:
            for char in symbols:
                temp.append(word + char)
        words = temp
        n -= 1

    return words


def main():
    try:
        file_name = os.path.basename(__file__)[:-3]
        data_set_name = f'datasets/rosalind_{file_name}.txt'
        with open(os.path.join(os.pardir, data_set_name), 'r') as file:
            data = file.readlines()

        symbols = data[0].split()
        n = int(data[1])
        answer = lexf(symbols, n)

        answer_name = f'answers/{file_name}.txt'
        with open(os.path.join(os.pardir, answer_name), 'w') as file:
            for i, word in enumerate(answer):
                if i + 1 == len(answer):
                    file.write(f'{word}')
                else:
                    file.write(f'{word}\n')

    except (FileNotFoundError):
        print('File not found.')


if __name__ == '__main__':
    main()

    symbols = ['A', 'C', 'G', 'T']
    n = 2
    expected = '''AA
AC
AG
AT
CA
CC
CG
CT
GA
GC
GG
GT
TA
TC
TG
TT'''.split()

    assert lexf(symbols, n) == expected
