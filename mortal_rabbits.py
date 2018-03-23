#!/usr/bin/python3

n = 6
m = 3

rabbits = {1: 1}

month = 1

while month < n:
    month += 1
    
    rabbits[2] = rabbits[1]
    rabbits[1] = 0
    
    


print(rabbits[n])
