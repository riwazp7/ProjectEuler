#Looking up stored values doesn't make the program go faster. Maybe it will be more efficient
#if we are dealing with a larger space so that the dictionary contains enough values.

d = {}


highest = 0
hnum = 0

#Number below 500000 have a shorter tail because numbers<500000 * 2 is numbers>500000
for x in range(500000,1000000):
	num = x
	count  = 0

	while (x != 1):
		
		if x in d:
			count+=d[x]
			break
		else:
			count+=1
			if x%2 == 0: x = x/2
			else: x = x*3+1

			

	d[x] = count

	if count>highest: 
		highest = count
		hnum = num
		print(hnum, highest)

print(hnum)