# Euler31.py
# (c) 2016 RIWAZ POUDYAL
# 0.045 secs (Oct 12 016)

no_of_ways = [0] * 201
no_of_ways[0] = 1

l = [1, 2, 5, 10, 20, 50, 100, 200]

def totalWays(n):
    # pre generate the dp table kind of
    for coin in l:
        for num in range(coin, n + 1): # Start from the num you can make with a coin as big
            no_of_ways[num] += no_of_ways[num-coin]
    return no_of_ways[n]

print(totalWays(200))
