#!/usr/bin/env python3
"""
http://rosalind.info/problems/iprb/
Problem

Figure 2. The probability of any outcome (leaf) in a probability tree diagram is given by the product of probabilities from the start of the tree to the outcome. For example, the probability that X is blue and Y is blue is equal to (2/5)(1/4), or 1/10.
Probability is the mathematical study of randomly occurring phenomena. We will model such a phenomenon with a random variable, which is simply a variable that can take a number of different distinct outcomes depending on the result of an underlying random process.

For example, say that we have a bag containing 3 red balls and 2 blue balls. If we let X represent the random variable corresponding to the color of a drawn ball, then the probability of each of the two outcomes is given by Pr(X=red)=35 and Pr(X=blue)=25.

Random variables can be combined to yield new random variables. Returning to the ball example, let Y model the color of a second ball drawn from the bag (without replacing the first ball). The probability of Y being red depends on whether the first ball was red or blue. To represent all outcomes of X and Y, we therefore use a probability tree diagram. This branching diagram represents all possible individual probabilities for X and Y, with outcomes at the endpoints ("leaves") of the tree. The probability of any outcome is given by the product of probabilities along the path from the beginning of the tree; see Figure 2 for an illustrative example.

An event is simply a collection of outcomes. Because outcomes are distinct, the probability of an event can be written as the sum of the probabilities of its constituent outcomes. For our colored ball example, let A be the event "Y is blue." Pr(A) is equal to the sum of the probabilities of two different outcomes: Pr(X=blue and Y=blue)+Pr(X=red and Y=blue), or 310+110=25 (see Figure 2 above).

Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms: k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.

Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.

Sample Dataset
2 2 2
Sample Output
0.78333
"""

import os


def calc_prob(k, m, n):
    pop = [k, m, n]
    total = sum(pop)
    final_prob = 0
    for x, first_draw in enumerate(pop):
        exp_1 = first_draw / total
        for i, second_draw in enumerate(pop):
            if x == i:
                exp_2 = (second_draw - 1) / (total - 1)
            else:
                exp_2 = second_draw / (total - 1)
            if x == 0:
                prob = 1
            elif x == 1:
                if i == 0:
                    prob = 1
                elif i == 1:
                    prob = 0.75
                else:
                    prob = 0.5
            else:
                if i == 0:
                    prob = 1
                elif i == 1:
                    prob = 0.5
                else:
                    prob = 0
            final_prob += exp_1 * exp_2 * prob

    return final_prob


def main():
    try:
        file_name = os.path.basename(__file__)[:-3]
        data_set_name = f'datasets/rosalind_{file_name}.txt'
        with open(os.path.join(os.pardir, data_set_name), 'r') as file:
            data = file.read().split()
            k, m, n = int(data[0]), int(data[1]), int(data[2])
            answer = calc_prob(k, m, n)
        
        answer_name = f'answers/{file_name}.txt'
        with open(os.path.join(os.pardir, answer_name), 'w') as file:
            file.write(str(answer))

    except (FileNotFoundError):
        print('File not found.')


if __name__ == '__main__':
    main()

    assert round(calc_prob(2, 2, 2), 5) == 0.78333