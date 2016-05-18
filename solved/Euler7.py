#10001th prime

l = [True] * 1000000

for x in range(2,999999):
	
	count = 0
	
	while (True):
		a = x**2 + count*x
		
		if not (a < 1000000): break
		
		l[a] = False
		count+=1
		
# 1 and 0
l[1] = False
l[0] = False

count = 0
num = 0

for x in l:
	if x: count+=1
	if count == 10001: 
		print (num)
		break
	num+=1










