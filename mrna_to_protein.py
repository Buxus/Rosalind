#! /usr/bin/python3
# http://rosalind.info/problems/mrna/


mrna_file = open("/home/steve/Dropbox/Rosalind/rosalind_mrna.txt")
protein_string = mrna_file.read().strip()

rna_possibilities_dict = {'A': 4, 'R': 6, 'N': 2, 'D': 2, 'C': 2, 'Q': 2, 'E': 2, 'G': 4, 'H': 2,
                          'I': 3, 'L': 6, 'K': 2, 'M': 1, 'F': 2, 'P': 4, 'S': 6, 'T': 4, 'W': 1, 'Y': 2, 'V': 4}


def calculate_odds(protein_string):
    base = 1000000
    score = 3  # three for three possibilities of STOP codon
    for aa in protein_string:
        score *= rna_possibilities_dict[aa]
    return (score % base)


print(calculate_odds(protein_string))
