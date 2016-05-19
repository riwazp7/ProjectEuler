''' Euler33.py
'   (c) Riwaz Poudyal 2016
'   0.05 secs (18 may 016)
'''

def check(i,j):
    try:
        if ("0" in i and "0" in j) or (i == j) or (i > j): return -1
        elif i[0:1] == j[0:1]:
            return int(i[1:])/int(j[1:])
        elif i[0:1] == j[1:]:
            return int(i[1:])/int(j[0:1])
        elif i[1:] == j[1:]:
            return int(i[0:1])/int(j[0:1])
        elif i[1:] == j[0:1]:
            return int(i[0:1])/int(j[1:])
        else: return -1
    except ZeroDivisionError:
        return -1

l = []

for i in range(11,99):
    for j in range (12,99):
        x = check(str(i),str(j))
        if x == (i/j):  l.append((i,j))

num = 1
denom = 1

for (i,j) in l:
    num *= i
    denom *= j

if denom % num == 0: denom /= num

print(denom)
