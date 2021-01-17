#!/usr/bin/env python3
"""
http://rosalind.info/problems/subs/
Problem
Given two strings s and t, t is a substring of s if t is contained as a contiguous collection of symbols in s (as a result, t must be no longer than s).

The position of a symbol in a string is the total number of symbols found to its left, including itself (e.g., the positions of all occurrences of 'U' in "AUGCUUCAGAAAGGUCUUACG" are 2, 5, 6, 15, 17, and 18). The symbol at position i of s is denoted by s[i].

A substring of s can be represented as s[j:k], where j and k represent the starting and ending positions of the substring in s; for example, if s = "AUGCUUCAGAAAGGUCUUACG", then s[2:5] = "UGCU".

The location of a substring s[j:k] is its beginning position j; note that t will have multiple locations in s if it occurs more than once as a substring of s (see the Sample below).

Given: Two DNA strings s and t (each of length at most 1 kbp).

Return: All locations of t as a substring of s.

Sample Dataset
GATATATGCATATACTT
ATAT
Sample Output
2 4 10
"""

import os


def subs(string, substring):
    answer = []
    for i in range(0, len(string) - len(substring)):
        if string[i:i+len(substring)] == substring:
            answer.append(i + 1)

    return answer


def main(argv):
    try:
        with open(argv[0], 'r') as file:
            string = file.readline().strip('\n')
            substring = file.readline().strip('\n')

        answer = subs(string, substring)
        print(answer)

        with open('answers/subs.txt', 'w') as file:
            file.write(answer)

    except (FileNotFoundError, IndexError):
        print('Please provide a valid file.')


def main():
    try:
        file_name = os.path.basename(__file__)[:-3]
        data_set_name = f'datasets/rosalind_{file_name}.txt'
        with open(os.path.join(os.pardir, data_set_name), 'r') as file:
            string = file.readline().strip('\n')
            substring = file.readline().strip('\n')
            answer = subs(string, substring)

        answer_name = f'answers/{file_name}.txt'
        with open(os.path.join(os.pardir, answer_name), 'w') as file:
            file.write(' '.join([str(x) for x in answer]))

    except (FileNotFoundError):
        print('File not found.')


if __name__ == '__main__':
    main()

    string = 'GATATATGCATATACTT'
    substring = 'ATAT'
    assert subs(string, substring) == [2, 4, 10]
