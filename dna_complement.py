#!/usr/bin/python3
# http://rosalind.info/problems/rna/

# dna_file = open("/home/steve/Dropbox/Rosalind/rosalind_rna.txt")
# dna_string = dna_file.readline().strip()

dna_string = "AAAACCCGGT"

base_key = {"A": "T", "G": "C", "C": "G", "T": "A"}

dna_complement = ""
for base in dna_string:
    dna_complement += base_key[base]

print(dna_complement[::-1])
