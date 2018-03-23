#!/usr/bin/python3

n = 35
k = 2

rabbits = {0: 0, 1: 1}

month = 1

while month < n:
    month += 1
    print(rabbits[month - 1])
    rabbits[month] = rabbits[month - 1] + (k * rabbits[month - 2])

print(rabbits[n])
