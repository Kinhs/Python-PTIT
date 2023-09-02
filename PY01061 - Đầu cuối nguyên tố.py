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


for t in range(int(input())):
    a = input()
    if isprime(int(a[:3])) and isprime(int(a[-3:])):
        print("YES")
    else:
        print("NO")