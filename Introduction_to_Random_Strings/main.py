#!/usr/bin/python3
# http://rosalind.info/problems/prob/

import math

def main():
    dna_file = open("./rosalind_prob.txt", 'r')
    dna_string = dna_file.readline().strip()
    
    a_array = [num for num in dna_file.readline().split()]

    print(dna_string)
    print(a_array)

    AT = dna_string.count('A') + dna_string.count('T')
    CG = dna_string.count('C') + dna_string.count('G')
    
    b_array = [round(math.log10(((float(a_array[x])/2)**CG)*((.5-(float(a_array[x])/2))**AT)), 3) for x in range(len(a_array))]

    for x in range(len(b_array)):
        print(b_array[x], end = " ")
    print("")
    
if __name__ == "__main__":
    main()
