#!/usr/bin/env python3
"""
http://rosalind.info/problems/grph/
Problem
A graph whose nodes have all been labeled can be represented by an adjacency list, in which each row of the list contains the two node labels corresponding to a unique edge.

A directed graph (or digraph) is a graph containing directed edges, each of which has an orientation. That is, a directed edge is represented by an arrow instead of a line segment; the starting and ending nodes of an edge form its tail and head, respectively. The directed edge with tail v and head w is represented by (v,w) (but not by (w,v)). A directed loop is a directed edge of the form (v,v).

For a collection of strings and a positive integer k, the overlap graph for the strings is a directed graph Ok in which each string is represented by a node, and string s is connected to string t with a directed edge when there is a length k suffix of s that matches a length k prefix of t, as long as s≠t; we demand s≠t to prevent directed loops in the overlap graph (although directed cycles may be present).

Given: A collection of DNA strings in FASTA format having total length at most 10 kbp.

Return: The adjacency list corresponding to O3. You may return edges in any order.

Sample Dataset
>Rosalind_0498
AAATAAA
>Rosalind_2391
AAATTTT
>Rosalind_2323
TTTTCCC
>Rosalind_0442
AAATCCC
>Rosalind_5013
GGGTGGG
Sample Output
Rosalind_0498 Rosalind_2391
Rosalind_0498 Rosalind_0442
Rosalind_2391 Rosalind_2323
"""

import os
import re


def adjacency_list(data, k=3):
    O = []
    for x, (ref_s, s) in enumerate(data.items()):
        suffix = s[-k:]
        for ref_t, t in data.items():
            if s != t:
                prefix = t[:k]
                if suffix == prefix:
                    O.append((ref_s, ref_t))

    return O


def data_format(string):
    refs = re.findall('Rosalind_\d+', string)
    seqs = re.findall('\n[ACGT\n]*', string)
    seqs = [seq.replace('\n', '') for seq in seqs]
    
    return {ref: seq for ref, seq in zip(refs, seqs)}


def answer_format(answer):
    formatted_answer = ''
    for nodes in answer:
        formatted_answer += (f'{nodes[0]} {nodes[1]}\n')
    return formatted_answer[:-1]


def main():
    try:
        file_name = os.path.basename(__file__)[:-3]
        data_set_name = f'datasets/rosalind_{file_name}.txt'
        with open(os.path.join(os.pardir, data_set_name), 'r') as file:
            data = file.read()

        data = data_format(data)
        answer = adjacency_list(data)

        answer_name = f'answers/{file_name}.txt'
        with open(os.path.join(os.pardir, answer_name), 'w') as file:
            file.write(answer_format(answer))

        # Make a .gv file to construct a graph with graphviz
        with open(os.path.join(os.pardir, 'graphs/grph.gv'), 'w') as file:
            file.write('digraph grph {\n')
            for nodes in answer:
                file.write(f'\t{nodes[0]} -> {nodes[1]};\n')
            file.write('}')

    except (FileNotFoundError):
        print('File not found.')

    os.system(
        f'dot -Tjpg {os.pardir}/graphs/grph.gv -o {os.pardir}/graphs/grph.jpg'
    )


if __name__ == '__main__':
    main()

    sample = """>Rosalind_0498
AAATAAA
>Rosalind_2391
AAATTTT
>Rosalind_2323
TTTTCCC
>Rosalind_0442
AAATCCC
>Rosalind_5013
GGGTGGG"""
    sample = data_format(sample)
    answer = """Rosalind_0498 Rosalind_2391
Rosalind_0498 Rosalind_0442
Rosalind_2391 Rosalind_2323"""

    assert answer_format(adjacency_list(sample)) == answer
