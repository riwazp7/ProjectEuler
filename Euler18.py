#Pipe the output to "sort -n" to find the greatest sum
# python3 Euler18.py | sort -n

a = []
a.append([75])
a.append([95, 64])
a.append([17 ,47 ,82])
a.append([18, 35, 87, 10])
a.append([20, 4, 82, 47, 65])
a.append([19, 1, 23, 75 ,3, 34])
a.append([88, 2, 77, 73, 7, 63, 67])
a.append([99, 65, 4, 28, 6, 16, 70, 92])
a.append([41, 41, 26, 56, 83, 40, 80, 70, 33])
a.append([41, 48, 72, 33, 47, 32, 37, 16, 94, 29])
a.append([53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14])
a.append([70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57])
a.append([91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48])
a.append([63, 66, 4 ,68 ,89 ,53 ,67 ,30, 73, 16, 69, 87, 40, 31])
a.append([4, 62, 98, 27, 23, 9, 70, 98, 73 ,93 ,38, 53, 60, 4, 23])




def findsum(row, col, sum):
    if row>14: print(sum)
    else:
        findsum(row+1,col+1, sum + a[row][col])
        findsum(row+1, col, sum + a[row][col])

findsum(0,0,0)
