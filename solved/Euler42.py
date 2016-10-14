# Euler42.py
# (c) 2016 RIWAZ POUDYAL
# 0.05 secs (13 Oct 016) 
import string

isTriangular = [False] * 500
count = 0

# Initialize the list of Triangular numbers < 500
i = 1
while(True):
    num = int((i * (i + 1)) / 2)
    if (num >= 500): 
        break
    isTriangular[num] = True
    i += 1

# get words in lowercase from the file
f = open('p042_words.txt','r')
words = f.read()
word_list = [x[1:-1].lower() for x in words.split(',')]

def getWordValue(word):
    val = 0
    for letter in word:
        val += (ord(letter) - 96)
    return val

for word in word_list:
    if isTriangular[getWordValue(word)]:
        count += 1

print(count)
