#!/usr/bin/python3
# http://rosalind.info/problems/iprb/

# Should replace this with straight calculation i.e. this solution found on Rosalind:
# k = 2039 m = 1923 n = 2167
# print((4*k**2+8*k*m+8*k*n-4*k+3*m**2+4*m*n-3*m)/(4*(k+m+n-1)*(k+m+n)))

import itertools

k = 124320
m = 154355
n = 2655

population_size = k + m + n

weights = {('AA', 'AA'): 1,
           ('AA', 'Aa'): 1,
           ('AA', 'aa'): 1,
           ('Aa', 'AA'): 1,
           ('Aa', 'Aa'): .75,
           ('Aa', 'aa'): .5,
           ('aa', 'AA'): 1,
           ('aa', 'Aa'): .5,
           ('aa', 'aa'): 0}

population = []

while k > 0:
    population.append("AA")
    k -= 1

while m > 0:
    population.append("Aa")
    m -= 1

while n > 0:
    population.append("aa")
    n -= 1

matches = 0
score = 0
for match in itertools.permutations(population, 2):
    matches += 1
    score += weights[match]

print(score/matches)
