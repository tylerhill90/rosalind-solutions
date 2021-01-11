#!/usr/bin/env python3
"""
http://rosalind.info/problems/tree/
Problem
An undirected graph is connected if there is a path connecting any two nodes. A tree is a connected (undirected) graph containing no cycles; this definition forces the tree to have a branching structure organized around a central core of nodes, just like its living counterpart. See Figure 2.

We have already grown familiar with trees in “Mendel's First Law”, where we introduced the probability tree diagram to visualize the outcomes of a random variable.

In the creation of a phylogeny, taxa are encoded by the tree's leaves, or nodes having degree 1. A node of a tree having degree larger than 1 is called an internal node.

Given: A positive integer n (n≤1000) and an adjacency list corresponding to a graph on n nodes that contains no cycles.

Return: The minimum number of edges that can be added to the graph to produce a tree.

Sample Dataset
10
1 2
2 8
4 10
5 9
6 10
7 9
Sample Output
3
"""


import os


def tree(n, adj_list):
    sub_graphs = dict()
    for num in range(1, n+1):
        sub_graphs[num] = set()

    for pair in adj_list:
        sub_graphs[pair[0]].add(pair[1])
        sub_graphs[pair[1]].add(pair[0])

    print(sub_graphs)

    trees = [{1}]
    for key, value in sub_graphs.items():
        pointer = None
        for i, t in enumerate(trees):
            for x in {key}.union(value):
                if x in t:
                    pointer = i
                    break
        if type(pointer) == int:
            [trees[pointer].add(x) for x in value]
        else:
            trees.append({key}.union(value))

    return len(trees) - 1


def format_data(data):
    data = data.split()
    n = int(data.pop(0))
    adj_list = []
    for x in range(0, len(data), 2):
        adj_list.append((int(data[x]), int(data[x+1])))

    return n, adj_list


def main():
    try:
        file_name = os.path.basename(__file__)[:-3]
        data_set_name = f'datasets/rosalind_{file_name}.txt'
        with open(os.path.join(os.pardir, data_set_name), 'r') as file:
            data = file.read()

        n, adj_list = format_data(data)
        answer = tree(n, adj_list)

        answer_name = f'answers/{file_name}.txt'
        with open(os.path.join(os.pardir, answer_name), 'w') as file:
            file.write(str(answer))

    except (FileNotFoundError):
        print('File not found.')


if __name__ == '__main__':
    main()

    sample = '''10
1 2
2 8
4 10
5 9
6 10
7 9'''

    n, adj_list = format_data(sample)

    assert tree(n, adj_list) == 3
