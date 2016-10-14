# Euler44.py
# (c) RIWAZ POUDYAL 2016
# 0.55 secs (14th Oct 2016)

n = 0
pen_set = set()
def generateNextNumbers(i):
    result = []
    global n, pen_list
    for x in range(0,i):
        n += 1
        num  = int((n * (3 * n - 1)) / 2)
        pen_set.add(num)
        result.append(num)
    return result

# initialize a list with the first 5000 pentagonal #s
generateNextNumbers(5000)
check_set = pen_set
n = 0
pen_set = set()


while(n < 2500):
    # check in chunks
    recent = generateNextNumbers(500)
    done = False
    for x in recent:
        for y in pen_set:
            if x + y in check_set:
                if x - y in check_set:
                    done = True
                    print(x-y)
                    break
        if done:
            break

