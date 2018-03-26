#!/usr/bin/python3

import itertools

n = 7
permutations = list(itertools.permutations(range(1, n + 1)))

print(len(permutations))
for permutation in permutations:
    for num in permutation:
        print(str(num) + " ", end = '')
    print('')
