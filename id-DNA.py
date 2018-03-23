#! /usr/bin/python3
# id-DNA.py
# http://rosalind.info/problems/dna/

dna_file = open('/home/steve/Dropbox/Rosalind/rosalind_dna.txt', 'r')
dna_string = str(dna_file.readlines())

base_count = {"A": 0, "G": 0, "C": 0, "T": 0}
for base in dna_string:
    base_count[base] += 1

print(base_count)
