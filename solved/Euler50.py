''' Euler50.py
'   0.05 on a powerful machine, July 2017
'   (c) Riwaz Poudyal
'''

primes = []
def isPrime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False
    i = 5
    while(i*i <= n):
        if n % i == 0: return False
        if n % (i + 2) == 0: return False
        i += 6
    return True
for i in range(3942): # Requries a bit of tuning to find something that is below 1 million
  if isPrime(i):
    primes.append(i)

cumPrimes = [0] * len(primes)
cumPrimes[0] = primes[0]
for i in range(1, len(primes)):
  cumPrimes[i] = cumPrimes[i-1] + primes[i]

longest = 0
longestPrime = -1

# Can do better by remembering which find we have already looked at
# Still pretty fast
def find(i, j):
  global longest, longestPrime
  if j - i <= longest:
    return
  if (i > len(primes) or j < 0):
    return
  if isPrime((cumPrimes[j] - cumPrimes[i])):
    longest = j - i
    longestPrime = cumPrimes[j] - cumPrimes[i]
  else:
    find(i+1, j)
    find(i, j - 1)

find(0, len(primes)-1)
print(longest)
print(longestPrime)
