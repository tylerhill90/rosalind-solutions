#!/usr/bin/env python3
"""
http://rosalind.info/problems/fibd/
Problem

Figure 4. A figure illustrating the propagation of Fibonacci's rabbits if they die after three months.
Recall the definition of the Fibonacci numbers from “Rabbits and Recurrence Relations”, which followed the recurrence relation Fn=Fn−1+Fn−2 and assumed that each pair of rabbits reaches maturity in one month and produces a single pair of offspring (one male, one female) each subsequent month.

Our aim is to somehow modify this recurrence relation to achieve a dynamic programming solution in the case that all rabbits die out after a fixed number of months. See Figure 4 for a depiction of a rabbit tree in which rabbits live for three months (meaning that they reproduce only twice before dying).

Given: Positive integers n≤100 and m≤20.

Return: The total number of pairs of rabbits that will remain after the n-th month if all rabbits live for m months.

Sample Dataset
6 3
Sample Output
4
"""

import os


def fibd(n, m):
    if n in [1, 2]:
        return 1

    pop = [0 if x > 0 else 1 for x in range(m)]
    for month in range(n - 1):
        next_gen = [0 for x in range(m)]
        next_gen[0] = sum(pop[1:])
        for age in range(1, m):
            next_gen[age] = pop[age - 1]
        pop = next_gen

    return sum(pop)


def main():
    try:
        file_name = os.path.basename(__file__)[:-3]
        data_set_name = f'datasets/rosalind_{file_name}.txt'
        with open(os.path.join(os.pardir, data_set_name), 'r') as file:
            data = file.read().split()

        answer = fibd(int(data[0]), int(data[1]))
        print(answer)

        answer_name = f'answers/{file_name}.txt'
        with open(os.path.join(os.pardir, answer_name), 'w') as file:
            file.write(str(answer))

    except (FileNotFoundError):
        print('File not found.')


if __name__ == '__main__':
    main()

    assert fibd(6, 3) == 4