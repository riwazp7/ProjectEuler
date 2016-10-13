# Euler39.py
# (c) RIWAZ POUDYAL 2016
# 0.13 secs (12 Oct 016)
from math import sqrt

count = [0] * 1001

for a in range(1,500):
    for b in range(a,500):
        c = sqrt(a * a + b * b)
        if c - int(c) == 0:
            if a + b + c > 1000: continue
            count[a + b + int(c)] += 1

high = 0
for x in range(0, 1000):
    if count[x] > count[high]:
        high = x

print(high)
