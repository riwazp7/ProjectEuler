# Euler62.py
# (c) Riwaz Poudyal
# 0.1 sec, Sept 3 2017
cubes = []
for i in range(1, 10000):
    cubes.append((sorted(str(i*i*i)), i*i*i))
cubes.sort(key = lambda tup: tup[0])
pointer = 0
cube = []
while (pointer + 4 < len(cubes)):
    start = pointer
    found = True
    for i in range(1, 5):
        if cubes[start + 1][0] != cubes[start][0]:
            found = False
            break
        start += 1
    if (found):
        cube = cubes[pointer]
        break
    pointer += 1

print(cube[1])
