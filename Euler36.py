sum = 0

def findBinary(n):
    s = ""
    while( n != 0):
        s = str (n % 2) + s
        n = int( n / 2 ) 
    return s


for i in range(1, 1000001):
    x = str(i)
    if x == x[::-1]:
        y = findBinary(i)
        if y == y[::-1]:
            sum += i

print(sum)
