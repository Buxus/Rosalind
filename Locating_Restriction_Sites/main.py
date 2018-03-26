#!/usr/bin/env python3
# http://rosalind.info/problems/revp/

from Bio import SeqIO

def main():
    data_file = open("./rosalind_revp.txt", 'r')
    dna_fasta = list(SeqIO.parse(data_file, "fasta"))

    dna_string = dna_fasta[0].seq
    print(dna_string)
    
    palindromes = []

    for i in range(len(dna_string)):
        for j in range(4,13):
            slice = dna_string[i:i+j]
            if j == len(slice) and isReversePalindrome(slice):
                palindromes.append("%s %s" % (i + 1, j))

            
    for item in palindromes:
        print(item)


def isReversePalindrome(string):
    return string == revComplement(string)[::-1]

def revComplement(dna_string):
    complements_dict = {
        "A" : "T",
        "T" : "A",
        "C" : "G",
        "G" : "C"
    }
    
    complement = ""
    for base in dna_string:
        complement += complements_dict[base]

    return complement


if __name__ == '__main__':
    main()
