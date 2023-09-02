from math import sqrt


def isprime(n):
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    sqr = int(sqrt(n))
    for i in range(5, sqr+1, 6):
        if n % i == 0 or n % (i+2) == 0:
            return False
    return True


def check(l):
    if not isprime(len(l)):
        return False
    cnt = 0
    for i in l:
        if isprime(i):
            cnt += 1
    if cnt > len(l) - cnt:
        return True
    return False


for t in range(int(input())):
    l = list(int(i) for i in input())
    if check(l):
        print("YES")
    else:
        print("NO")