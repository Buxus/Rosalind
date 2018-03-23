#!/usr/bin/python3
# http://rosalind.info/problems/gc/

from Bio import SeqIO

fasta_sequences = SeqIO.parse(
    open("/home/steve/Dropbox/Rosalind/rosalind_gc.txt"), 'fasta')

fasta_strings = {}
for sequence in fasta_sequences:
    fasta_strings[sequence.id] = str(sequence.seq)

# fasta_strings = {"Rosalind_6404": "CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCCTCCCACTAATAATTCTGAGG",
#                  "Rosalind_5959": "CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCTATATCCATTTGTCAGCAGACACGC",
#                  "Rosalind_0808": "CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT"}

gc_percents = {}

for key in fasta_strings.keys():
    gc_count = 0
    for base in fasta_strings[key]:
        if base == "G" or base == "C":
            gc_count += 1
    gc_percents[key] = (gc_count / len(fasta_strings[key])) * 100

winner = max(gc_percents, key=gc_percents.get)
print(winner)
print(gc_percents[winner])
