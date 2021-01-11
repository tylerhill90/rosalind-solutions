#!/usr/bin/env python3
"""
http://rosalind.info/problems/mprt/
Problem
To allow for the presence of its varying forms, a protein motif is represented by a shorthand as follows: [XY] means "either X or Y" and {X} means "any amino acid except X." For example, the N-glycosylation motif is written as N{P}[ST]{P}.

You can see the complete description and features of a particular protein by its access ID "uniprot_id" in the UniProt database, by inserting the ID number into

http://www.uniprot.org/uniprot/uniprot_id
Alternatively, you can obtain a protein sequence in FASTA format by following

http://www.uniprot.org/uniprot/uniprot_id.fasta
For example, the data for protein B5ZC00 can be found at http://www.uniprot.org/uniprot/B5ZC00.

Given: At most 15 UniProt Protein Database access IDs.

Return: For each protein possessing the N-glycosylation motif, output its given access ID followed by a list of locations in the protein string where the motif can be found.

Sample Dataset
A2Z669
B5ZC00
P07204_TRBM_HUMAN
P20840_SAG1_YEAST
Sample Output
B5ZC00
85 118 142 306 395
P07204_TRBM_HUMAN
47 115 116 382 409
P20840_SAG1_YEAST
79 109 135 248 306 348 364 402 485 501 614
"""

import os
import requests
import re


def find_motif_locals(uniprot_id, motif, k):
    url = f'https://www.uniprot.org/uniprot/{uniprot_id}.fasta'
    r = requests.get(url)
    prot_seq = ''.join(r.text.split('\n')[1:])

    # Handle overlapping patterns
    locations = []
    for i in range(len(prot_seq) - k):
        if re.fullmatch(motif, prot_seq[i:i+k]):
            locations.append(i+1)

    return locations


def format_output(data):
    answer = ''
    for key, value in data.items():
        answer += f'{key}\n'
        answer += ' '.join([str(x) for x in value]) + '\n'

    return answer.strip('\n')


def main():
    try:
        file_name = os.path.basename(__file__).strip(".py")
        data_set_name = f'datasets/rosalind_{file_name}.txt'
        with open(os.path.join(os.pardir, data_set_name), 'r') as file:
            data = file.read().split('\n')

        # N-glycosylation motif
        n_glycosylation = re.compile('N[^P][ST][^P]')
        answer = dict()
        for uniprot_id in data:
            locations = find_motif_locals(uniprot_id, n_glycosylation, 4)
            if locations:
                answer[uniprot_id] = locations

        answer_name = f'answers/{file_name}.txt'
        with open(os.path.join(os.pardir, answer_name), 'w') as file:
            file.write(format_output(answer))

    except (FileNotFoundError):
        print('File not found.')


if __name__ == '__main__':
    main()

    sample = """A2Z669
B5ZC00
P07204_TRBM_HUMAN
P20840_SAG1_YEAST"""

    expected_output = {
        'B5ZC00': [int(x) for x in '85 118 142 306 395'.split()],
        'P07204_TRBM_HUMAN': [int(x) for x in '47 115 116 382 409'.split()],
        'P20840_SAG1_YEAST': [int(x) for x in
                              '79 109 135 248 306 348 364 402 485 501 614'.split()]
    }

    data = sample.split()
    n_glycosylation = re.compile('N[^P][ST][^P]')
    answer = dict()
    for uniprot_id in data:
        locations = find_motif_locals(uniprot_id, n_glycosylation, 4)
        if locations:
            answer[uniprot_id] = locations

    assert answer == expected_output
