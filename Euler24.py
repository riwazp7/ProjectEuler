import itertools

l = [0,1,2,3,4,5,6,7,8,9]
x = list(itertools.permutations(l))

lex = []
for i in x:
    st = ""
    for z in i:
        st += str(z)
    lex.append(st)

print (lex[1000000-1])
