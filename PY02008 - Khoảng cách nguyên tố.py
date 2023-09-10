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
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


a, b = list(int(i) for i in input().split())
print(b, end=" ")
cnt = 0
c = 2
while cnt < a:
    while not isprime(c):
        c += 1
    b += c
    cnt += 1
    c += 1
    print(b, end=" ")
