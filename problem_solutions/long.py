#!/usr/bin/env python3
"""
http://rosalind.info/problems/long/
Problem
For a collection of strings, a larger string containing every one of the smaller strings as a substring is called a superstring.

By the assumption of parsimony, a shortest possible superstring over a collection of reads serves as a candidate chromosome.

Given: At most 50 DNA strings of approximately equal length, not exceeding 1 kbp, in FASTA format (which represent reads deriving from the same strand of a single linear chromosome).

The dataset is guaranteed to satisfy the following condition: there exists a unique way to reconstruct the entire chromosome from these reads by gluing together pairs of reads that overlap by more than half their length.

Return: A shortest superstring containing all the given strings (thus corresponding to a reconstructed chromosome).

Sample Dataset
>Rosalind_56
ATTAGACCTG
>Rosalind_57
CCTGCCGGAA
>Rosalind_58
AGACCTGCCG
>Rosalind_59
GCCGGAATAC
Sample Output
ATTAGACCTGCCGGAATAC
"""


import os
from grph import adjacency_list, data_format


def shortest_super(data):
    min_len = min([len(x) for x in data.values()])

    # Build a dictionary of pairs that overlap for keys and their overlap
    # length as keys
    to_assemble = dict()
    pairs_set = set()
    for k in range(min_len, min_len // 2, -1):
        adj_lst = adjacency_list(data, k)
        if adj_lst:
            for pair in adj_lst:
                to_assemble[pair] = k
                pairs_set.add(pair)

    # Build a list of pairs that link together
    linked_list = [list(pairs_set)[0]]
    look_forward = True
    while look_forward:
        pointer = linked_list[-1][1]
        for i, pair in enumerate(pairs_set):
            if pair[0] in pointer:
                linked_list.append(pair)
                pairs_set.remove(pair)
                break
            if i + 1 == len(pairs_set):
                look_forward = False

    # Look backward
    while len(linked_list) != len(data) - 1:
        pointer = linked_list[0][0]
        for pair in pairs_set:
            if pair[1] in pointer:
                linked_list.insert(0, pair)
                pairs_set.remove(pair)
                break

    answer = ''
    for i, pair in enumerate(linked_list):
        if i:
            answer += data[pair[1]][to_assemble[pair]:]
        else:
            answer += data[pair[0]] + data[pair[1]][to_assemble[pair]:]

    return answer


def main():
    try:
        file_name = os.path.basename(__file__)[:-3]
        data_set_name = f'datasets/rosalind_{file_name}.txt'
        with open(os.path.join(os.pardir, data_set_name), 'r') as file:
            data = file.read()

        data = data_format(data)
        answer = shortest_super(data)

        answer_name = f'answers/{file_name}.txt'
        with open(os.path.join(os.pardir, answer_name), 'w') as file:
            file.write(answer)

    except (FileNotFoundError):
        print('File not found.')


if __name__ == '__main__':
    main()

    sample = '''>Rosalind_56
ATTAGACCTG
>Rosalind_57
CCTGCCGGAA
>Rosalind_58
AGACCTGCCG
>Rosalind_59
GCCGGAATAC'''

    data = data_format(sample)

    assert shortest_super(data) == 'ATTAGACCTGCCGGAATAC'
