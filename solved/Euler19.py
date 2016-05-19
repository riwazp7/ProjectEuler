def isLeapYear(n):
    if not n % 4 == 0: return False
    elif not n % 100 == 0: return True
    elif not n % 400 == 0: return False
    else: return True

no_days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6:30, 7:31, 8:31, 9:30, 10:31, 11: 30, 12: 31}

year = 1900
month = 1
day = 2
count = 0
#Uggh this sucks

while(year < 2001):
    day = day + no_days[month]
    if month == 2 and isLeapYear(year):
        day += 1
    day = day % 7

    if (day == 1 and year >= 1901): 
        count += 1
        print(count)
        
    month += 1
    if month == 13:
        month = 1
        year += 1
