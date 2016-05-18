tri = [-1]*1000000000
pen = [-1]*1000000000
hex = [-1]*1000000000

print("Initialized all arrays")

x = 40755
n = 144
while( x < 10000000000 ):
   x = n * (2 * n - 1)
   hex[x] = 1
   n += 1

print("1st array populated")

x = 40755
n = 144
while( x < 10000000000 ):
    x = n * (3 * n - 1) / 2
    pen[x] = 1
    n += 1

print("2nd array populated")

x = 40755
n = 144
while( x < 10000000000 ):
    x = n * ( n + 1) / 2
    tri[x] = 1  
    n += 1

print("All three done. Finding the number now")

for i in range(40756,90000000000):
    if hex[i] == 1 and pen[i] == 1 and tri[i] == 1:
        print (i)
        break
