''' Euler19.py
'   ~0.0 (016 May 19)
'   (c) Riwaz Poudyal 2016 
'''

# Thanks Wikipedia for the 'algorithm'
def isLeapYear(n):
    if not n % 4 == 0: return False
    elif not n % 100 == 0: return True
    elif not n % 400 == 0: return False
    else: return True

no_days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6:30, 7:31, 8:31, 9:30, 10:31, 11: 30, 12: 31}


year = 1900
month = 1
day = 2 #Sunday is 1
count = 0

while(year < 2001):
    day = day + no_days[month]
    
    # Add 1 to Feb if leap year
    if month == 2 and isLeapYear(year):
        day += 1
    day = day % 7
    
    # Sunday, 1st of the month
    if (day == 1 and year >= 1901): 
        count += 1
    
    #Better than mod by 12
    month += 1
    if month == 13:
        month = 1
        year += 1
