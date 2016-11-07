# Euler55.py
# (c) 2016 RIWAZ POUDYAL 
# 0.02 secs

l_count = 0

def reverse(n):
    o = 0
    while n != 0:
        o = o * 10 + n % 10
        n //= 10
    return o

def reverseAndAdd(n):
    return n + reverse(n)

def isPalindrome(n):
    s = str(n)
    for i in range(0, int(len(s)/2)):
        if s[i] != s[len(s) - i -1]:
            return False
    return True

for i in range(1, 10000):
    n = i
    for x in range(0, 50):
        n = reverseAndAdd(n)
        if isPalindrome(n):
            break
    else:
        l_count += 1
print(l_count)
