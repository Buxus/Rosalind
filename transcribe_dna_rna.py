#!/usr/bin/python3
# http://rosalind.info/problems/rna/

dna_file = open("/home/steve/Dropbox/Rosalind/rosalind_rna.txt")
dna_string = dna_file.readline().strip()

base_key = {"A": "A", "G": "G", "C": "C", "T": "U"}

rna_string = ""
for base in dna_string:
    rna_string += base_key[base]

print(rna_string)
