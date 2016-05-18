''' Euler52.py
'   (c) 2015 Riwaz Poudyal
'   0.33secs
'''
n = 10

def checkOrder(x):
    l = []
    for i in str(x):
        l.append(i)
    count = 2
    
    while(count < 7):
        
        y = x * count
        
        for z in str(y):
            if z not in l: return False
        
        count += 1
    
    return True

while(True):
    if checkOrder(n): 
        print(n)
        break
    n += 1
