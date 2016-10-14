# Euler43.py
# (c) 2016 RIWAZ POUDYAL
# 2.1secs (14 Oct 016)

from itertools import permutations

filtered = [x for x in permutations('0123456789') if (x[0] != '0' and int(x[3]) % 2 == 0and (x[5] == '0' or x[5] == '5'))]
filtered = [x for x in filtered if int(x[5] + x[6] + x[7]) % 11 == 0 and int(x[6] + x[7] + x[8]) % 13 == 0 and int(x[7] + x[8] + x[9]) % 17 == 0]
filtered = [x for x in filtered if (int(x[2]) + int(x[3]) + int(x[4])) % 3 == 0 and int(x[4] + x[5] + x[6]) % 7 == 0]

nums = [''.join(x) for x in filtered]
print(sum(int(x) for x in nums))
                    
                    





