''' Euler17.py
'   (c) 2016 Riwaz Poudyal
'   0 secs, 15 may 016
'''

dic_1 = {'0': 0, '1': 3, '2': 3, '3': 5, '4': 4, '5': 4, '6': 3, '7': 5, '8': 5, '9': 4}
dic_2 = {'0': 0,  '2': 6, '3': 6, '4': 5, '5': 5, '6': 5, '7': 7, '8': 6, '9': 6}
dic_w = {'10': 3, '11': 6, '12': 6, '13': 8, '14':8, '15':7, '16':7, '17':9, '18': 8, '19': 8}

sum_letters = 0

#Processes all < 2 digit #s
def find_sum(n):
    if n < 10:
        return dic_1[str(n)]
    
    elif n < 20:
        return dic_w[str(n)]
    
    else:
        sum = 0
        sum += dic_1[str (n % 10)]
        n //= 10
    
        sum += dic_2[str (n % 10)]
        return sum

#Process 1,2,3 digit number. Uses find_sum for 1,2 digits
def tot(i):
    if i < 100:
        return find_sum(i)
    else: #Three digits
        sum = 0
        # Hundred place digit
        sum += dic_1[ str(i//100) ]
        #Last two digits
        k = int(str(i)[1:])
        sum += find_sum(k)
        if k != 0: 
            # Add 'and' if last two digit not 0s
            sum += 3
        return sum + 7 # 7 for 'Hundred'

for i in range(1, 1000):
    sum_letters += tot(i)

# Add 'one thousand' and print
print (sum_letters + 3 + 8)

