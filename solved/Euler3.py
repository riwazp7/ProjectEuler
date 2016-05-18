

def nextPrime():
	global current
	while (True):
		current +=1
		if isPrime(current): return current

def isPrime(n):

	for x in range(2,int(n/2)+1):
		if n%x == 0: return False

	return True

current = 1
num = 600851475143

while(True):
	n = nextPrime()
	
	if n>=num: break
	
	elif num%n == 0: 
		num = num/n
	
print (num)