from math import sqrt


def isPrime(i):
    if i < 2:
        return False
    if i < 4:
        return True
    if i % 2 == 0 or i % 3 == 0:
        return False
    sqr = int(sqrt(i))
    for j in range(5, sqr+1, 6):
        if i % j == 0 or i % (j+2) == 0:
            return False
    return True


n = int(input())
a = [int(i) for i in input().split()]
m = {}
for i in a:
    if i not in m:
        if isPrime(i):
            m[i] = 1
    else:
        m[i] += 1
for i in a:
    if i in m and m[i] > 0:
        print(i, m[i])
        m[i] = 0