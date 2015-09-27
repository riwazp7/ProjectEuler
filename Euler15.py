def calc (x, y, count):
	if x == 2 and y == 2:
		return 1 + count
	elif x<2 and y<2:
		return calc(x+1 ,y , count) + calc(x, y+1, count)
	else: return 0

print(calc(0,0,0))
		