#!/usr/bin/env python3
"""
http://rosalind.info/problems/pmch/
Problem
A matching in a graph G is a collection of edges of G for which no node belongs to more than one edge in the collection. See Figure 2 for examples of matchings. If G contains an even number of nodes (say 2n), then a matching on G is perfect if it contains n edges, which is clearly the maximum possible. An example of a graph containing a perfect matching is shown in Figure 3.

First, let Kn denote the complete graph on 2n labeled nodes, in which every node is connected to every other node with an edge, and let pn denote the total number of perfect matchings in Kn. For a given node x, there are 2n−1 ways to join x to the other nodes in the graph, after which point we must form a perfect matching on the remaining 2n−2 nodes. This reasoning provides us with the recurrence relation pn=(2n−1)⋅pn−1; using the fact that p1 is 1, this recurrence relation implies the closed equation pn=(2n−1)(2n−3)(2n−5)⋯(3)(1).

Given an RNA string s=s1…sn, a bonding graph for s is formed as follows. First, assign each symbol of s to a node, and arrange these nodes in order around a circle, connecting them with edges called adjacency edges. Second, form all possible edges {A, U} and {C, G}, called basepair edges; we will represent basepair edges with dashed edges, as illustrated by the bonding graph in Figure 4.

Note that a matching contained in the basepair edges will represent one possibility for base pairing interactions in s, as shown in Figure 5. For such a matching to exist, s must have the same number of occurrences of 'A' as 'U' and the same number of occurrences of 'C' as 'G'.

Given: An RNA string s of length at most 80 bp having the same number of occurrences of 'A' as 'U' and the same number of occurrences of 'C' as 'G'.

Return: The total possible number of perfect matchings of basepair edges in the bonding graph of s.

Sample Dataset
>Rosalind_23
AGCUAGUCAU
Sample Output
12
"""


import os
import re

from math import factorial


def get_seq(data):
    match = re.search(r'\n[ACGU\n]+', data)
    return match.group().replace('\n', '')


def pmch(seq):
    bond_graph = build_bonding_graph(seq)

    AU = 0
    CG = 0
    for nuc in seq:
        if nuc in ['A', 'U']:
            AU += 1
        else:
            CG += 1

    return factorial(AU/2) * factorial(CG/2)


def build_bonding_graph(seq):
    bond_graph = dict()
    for i, nuc in enumerate(seq):
        bond_graph[(i, nuc)] = set()

    for i, (key, value) in enumerate(bond_graph.items()):
        if key[1] in ['A', 'U']:
            look_for = ['A', 'U']
            look_for.remove(key[1])
        else:
            look_for = ['C', 'G']
            look_for.remove(key[1])

        for x in range(i+1, len(seq)):
            nuc = seq[x]
            if nuc in look_for:
                value.add(x)
                bond_graph[(x, look_for[0])].add(i)

    return bond_graph


def main():
    try:
        file_name = os.path.basename(__file__)[:-3]
        data_set_name = f'datasets/rosalind_{file_name}.txt'
        with open(os.path.join(os.pardir, data_set_name), 'r') as file:
            data = file.read()

        seq = get_seq(data)
        answer = pmch(seq)

        answer_name = f'answers/{file_name}.txt'
        with open(os.path.join(os.pardir, answer_name), 'w') as file:
            file.write(str(answer))

    except (FileNotFoundError):
        print('File not found.')


if __name__ == '__main__':
    main()

    sample = '''>Rosalind_23
AGCUAGUCAU'''

    assert pmch(get_seq(sample)) == 12
