#!/usr/bin/python3
# http://rosalind.info/problems/pper/

import math


def main():
    data = open("./rosalind_pper.txt", 'r').readline().split()
    
    n = int(data[0])
    k = int(data[1])

    print(n)
    print(k)

    print(p(n, k) % 1000000)


def p(n, k):
    result = math.factorial(n) // math.factorial(n - k)
    return result

if __name__ == '__main__':
    main()
