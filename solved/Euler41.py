# Euler41.py
# (c) 2016 RIWAZ POUDYAL
# 0.28 secs ( ~2 sec if 9 included but answer is not in that length)

def isPrime(i):
    if i <= 1:
        return False
    k = 2
    while (k*k <= i):
        if i % k == 0:
            return False
        k += 1
    return True

def generate(l):
    result = []
    if len(l) == 1:
        result.append(str(l[0]))
        return result
    for x in l:
        new_l = l[:]
        new_l.remove(x)
        s = generate(new_l)
        for a in s:
            result.append(str(x) + a)
    return result

def getPandigitals(n):
    l = []
    for i in range(1, n + 1):
        l.append(i)
    return generate(l)


def find():
    for i in range(8, 3, -1):
        pandigitals = getPandigitals(i)
        sorted_pan = sorted(pandigitals, reverse=True)
        for num in sorted_pan:
            if isPrime(int(num)):
                print(num)
                return

find()
        
