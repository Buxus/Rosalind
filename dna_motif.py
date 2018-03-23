#!/usr/bin/python3
# http://rosalind.info/problems/subs/

# string1 = "GATATATGCATATACTT"
# string2 = "ATAT"

dna_file = open("/home/steve/Dropbox/Rosalind/rosalind_subs.txt")

string1 = dna_file.readline().strip()
string2 = dna_file.readline().strip()

indexes = []
i = 0
for base in string1:
    # try:
    if string2 == string1[i:i + len(string2)]:
        indexes.append(i + 1)

    i += 1


for i in range(0, len(indexes)):
    print ("%s " % indexes[i], end='')
print("")
