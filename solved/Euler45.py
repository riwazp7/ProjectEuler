# Euler45.py
# (c) 2016 RIWAZ POUDYAL
# 0.14 secs
# for each Triangular number from n=1, see if it is already in pentagonal, hexagonal lists. Extend pent and hex list if needed.

tri_n = 0

pent = set()
pent_n = 0
pent_last = 0

hex = set()
hex_n = 0
hex_last = 0

def generateTri(i):
    result = []
    global tri, tri_n
    for x in range(0,i):
        tri_n += 1
        num = int(tri_n * (tri_n+1) / 2)
        result.append(num)
    return result

def generatePent(i):
    result = []
    global pent, pent_n
    for x in range(0,i):
        pent_n += 1
        num = int(pent_n * (3 * pent_n - 1) / 2)
        pent.add(num)
        result.append(num)
    return result

def generateHex(i):
    result = []
    global hex, hex_n
    for x in range(0,i):
        hex_n += 1
        num = hex_n * (2 * hex_n - 1)
        hex.add(num)
        result.append(num)
    return result

for i in range(0,100000):
    triangles = generateTri(100)
    done = False
    for num in triangles:
        while(pent_last < num):
            pent_last = generatePent(100)[99]
        if num in pent:
            while(hex_last < num):
                hex_last = generateHex(100)[99]
            if num in hex and num != 1 and num != 40755:
                print(num)
                done = True
                break
    if done:
        break
