def isPalin(str):
	l = len(str)
	if len(str)<=1: return True
	
	elif str[0:1] == str[l-1]: return isPalin(str[1:l-1])
	else: return False

largest=0
for i in range (1,999):
	for j in range(1, 999):
		n = i*j
		if isPalin(str(n)) and n > largest:
			largest = n

print (largest)
