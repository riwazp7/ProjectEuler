''' Euler8.py
'   (c) Riwaz Poudyal
'   0.001 s
'   April 29 016
'''

#Notice the pattern:

'''1
3 + 5 + 7 + 9 (+2)
13 + 17 + 21 + 25 (+4)
31 + 37 + 43 + 49 (+6)
'''

last = 1
sum =  1
increase = 2
lev = 1
while (2 * lev + 1 <= 1001):
    for i in range(0,4):
        last += increase
        sum += last
    increase += 2
    lev += 1

print(sum)

