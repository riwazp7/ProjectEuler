# Euler99.py
# (c) Riwaz Poudyal
# 0.04 secs, Sept 3, 2017

from math import log

def getVal(number):
    pair = number.split(',')
    return int(pair[1]) * log(int(pair[0]))

lines = [line.rstrip('\n') for line in open('base_exp.txt')]
max = getVal(lines[0])
index = 0
for i in range(1, len(lines)):
    if getVal(lines[i]) > max:
        max = getVal(lines[i])
        index = i
# Line no
print(index + 1)
