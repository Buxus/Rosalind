#!/usr/bin/python3
# http://rosalind.info/problems/cons/

from Bio import SeqIO


data_file = open("/home/steve/Dropbox/Rosalind/rosalind_cons.txt")
fasta_strings = list(SeqIO.parse(data_file, "fasta"))

# initialize dict of base counts
dna_length = len(fasta_strings[0].seq)
base_matrices = {
    base: [0 for i in range(dna_length)]
    for base in ["A", "C", "G", "T"]
}

# build count of bases
for record in fasta_strings:
    index = 0
    for base in record.seq:
        base_matrices[base][index] += 1
        index += 1

consensus = ""
for i in range(dna_length):
    consensus = consensus + \
        max(base_matrices, key=lambda k: base_matrices[k][i])
    # keyfunction taken from
    # https://stackoverflow.com/posts/35256685/revisions

print(consensus)
# for key, value in base_matrices.items():
# print(key + ": ", end='')
# print(value)

