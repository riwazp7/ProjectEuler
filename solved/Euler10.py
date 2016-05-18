l = [True] * 2000001

for x in range(2,2000000):
	
	count = 0

	while (True):
		
		a = x**2 + count*x
		
		if not (a <= 2000000): break
		l[a] = False
		
		count+=1
		
# 1 and 0
l[1] = False
l[0] = False

sum = 0
count = 0
for x in l:
	if x: sum+=count
	count+=1

print(sum)


	
