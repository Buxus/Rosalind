#!/usr/bin/python3
# http://rosalind.info/problems/hamm/

dna_file = open("/home/steve/Dropbox/Rosalind/rosalind_hamm.txt")
string1 = dna_file.readline().strip()
string2 = dna_file.readline().strip()

# string1 = "GAGCCTACTAACGGGAT"
# string2 = "CATCGTAATGACGGCCT"

mutations = 0

index = 0
for base in string1:
    if base != string2[index]:
        mutations += 1
    index += 1

print(mutations)
