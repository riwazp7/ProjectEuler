''' Euler22.py
'   (c) 2015 Riwaz Poudyal
'   0.056 secs
'''

#Open file, save names into a string, close file
f = open('p022_names.txt', 'r')
s = ""
for line in f:
    s += line
f.close()

#Split names into list and remove surrounding ""
names = s.split(",")
for i in range(0, len(names)):
    names[i] = names[i][1:len(names[i])-1]

#Sort
names.sort()

#Calculate alphabetical weight
sum = 0
for i in range(0, len(names)):
    s = 0
    for j in names[i]:
        s += (ord(j) - 64)
    sum += ((i+1)*s)

print(sum)
