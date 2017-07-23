# Euler50.py
# 0.05 secs, July 2017
# (c) Riwaz Poudyal

fact_value = [-1] * 101
fact_value[0] = 1
tot = 0

def calculate_factorial(n):
    if fact_value[n] != -1:
        return fact_value[n]
    prod = 1
    for i in range(2, n + 1):
        prod *= i
    fact_value[n] = prod
    return prod


for n in range(0,101):
    print(n)
    for r in range(0, n + 1):
        if calculate_factorial(n) / calculate_factorial(n-r) / calculate_factorial(r) > 1000000:
            tot += 1

print(tot)
