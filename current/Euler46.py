# Euler46.py
# (c) 2016 RIWAZ POUDYAL 
#

l = [false] * 1000
primes = set()
squares = []

for num in range(1,1000):
    squares.append(num * num)

for prime in primes:
    for square in squares:
        l[prime + 2 * square = True]
