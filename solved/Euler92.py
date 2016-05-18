''' Euler92.py
'   (c) Riwaz Poudyal
'   28 secs
'''

count = 0
arr = [-1] * 10000000

index = 2
arr[89] = 1
arr[1] = 0
arr[0] = 0

def expand(n):
	sum = 0
	while(n):
		s = n % 10
		sum += (s * s)
		n //= 10
	return sum

while(index < 10000000):
	n = index
	l = []
	while(True):
		l.append(n)
		n = expand(n)
		if arr[n] == 1:
			for num in l:
				arr[num] = 1
			break
		elif arr[n] == 0:
			for num in l:
				arr[num] = 0
			break
	while (True):
		index += 1
		if index >= 10000000 or arr[index] == -1:
			break

count = 0
for a in range(1,10000000):
	count += arr[a]

print(count)
