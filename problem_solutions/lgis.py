#!/usr/bin/env python3
"""
http://rosalind.info/problems/lgis/
Problem
A subsequence of a permutation is a collection of elements of the permutation in the order that they appear. For example, (5, 3, 4) is a subsequence of (5, 1, 3, 4, 2).

A subsequence is increasing if the elements of the subsequence increase, and decreasing if the elements decrease. For example, given the permutation (8, 2, 1, 6, 5, 7, 4, 3, 9), an increasing subsequence is (2, 6, 7, 9), and a decreasing subsequence is (8, 6, 5, 4, 3). You may verify that these two subsequences are as long as possible.

Given: A positive integer n≤10000 followed by a permutation π of length n.

Return: A longest increasing subsequence of π, followed by a longest decreasing subsequence of π.

Sample Dataset
5
5 1 4 2 3
Sample Output
1 2 3
5 4 2
"""


import os


def lgis(n, pi):
    "https://www.geeksforgeeks.org/construction-of-longest-increasing-subsequence-using-dynamic-programming/"
    lis = [0] * n
    for i in range(1, n):
        for x in range(0, i):
            if pi[i] > pi[x] and lis[i] < lis[x] + 1:
                lis[i] = lis[x] + 1

    lds = [n - 1] * n
    for i in range(1, n):
        for x in range(0, i):
            if pi[i] < pi[x] and lds[i] > lds[x] - 1:
                lds[i] = lds[x] - 1

    print(lis, lds)


def main():
    try:
        file_name = os.path.basename(__file__)[:-3]
        data_set_name = f'datasets/rosalind_{file_name}.txt'
        with open(os.path.join(os.pardir, data_set_name), 'r') as file:
            data = file.read().split()

        n, pi = int(data[0]), [int(i) for i in data[1:]]

        answer = lgis(n, pi)

        answer_name = f'answers/{file_name}.txt'
        with open(os.path.join(os.pardir, answer_name), 'w') as file:
            file.write(' '.join([str(i) for i in answer[0]]))
            file.write('\n' + ' '.join([str(i) for i in answer[1]]))

    except (FileNotFoundError):
        print('File not found.')


if __name__ == '__main__':
    main()

    sample = '''5
5 1 4 2 3'''.split()
    n, pi = int(sample[0]), [int(i) for i in sample[1:]]

    assert lgis(n, pi) == ([1, 2, 3], [5, 4, 3])
