#!/usr/bin/env python3
"""
http://rosalind.info/problems/perm/
Problem
A permutation of length n is an ordering of the positive integers {1,2,…,n}. For example, π=(5,3,2,1,4) is a permutation of length 5.

Given: A positive integer n≤7.

Return: The total number of permutations of length n, followed by a list of all such permutations (in any order).

Sample Dataset
3
Sample Output
6
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1
"""


import os


def perm(nums):
    permutations = [[]]
    for n in nums:
        new_perms = []
        for perm in permutations:
            for i in range(len(perm) + 1):
                new_perms.append(perm[:i] + [n] + perm[i:])
                permutations = new_perms
    return permutations


def format_answer(data):
    answer = str(len(data)) + '\n'
    for perm in data:
        for i in perm:
            answer += f'{i} '
        answer.strip(' ')
        answer += '\n'
    
    return answer[:-1]


def main():
    try:
        file_name = os.path.basename(__file__)[:-3]
        data_set_name = f'datasets/rosalind_{file_name}.txt'
        with open(os.path.join(os.pardir, data_set_name), 'r') as file:
            data = int(file.read())
        
        answer = perm(range(1, data + 1))

        answer_name = f'answers/{file_name}.txt'
        with open(os.path.join(os.pardir, answer_name), 'w') as file:
            file.write(format_answer(answer))

    except (FileNotFoundError):
        print('File not found.')


if __name__ == '__main__':
    main()
    