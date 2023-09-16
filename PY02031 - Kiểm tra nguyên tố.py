from math import sqrt


def isPrime(i):
    if i < 2:
        return 0
    if i < 4:
        return 1
    if i % 2 == 0 or i % 3 == 0:
        return 0
    sqr = int(sqrt(i))
    for j in range(5, sqr+1, 6):
        if i % j == 0 or i % (j+2) == 0:
            return 0
    return 1


a, b = [int(i) for i in input().split()]
for i in range(a):
    l = [int(i) for i in input().split()]
    for j in l:
        print(isPrime(j), end=' ')
    print()