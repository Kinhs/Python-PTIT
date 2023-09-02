from math import sqrt


def isprime(n):
    if n < 2:
        return "NO"
    if n < 4:
        return "YES"
    if n % 2 == 0 or n % 3 == 0:
        return "NO"
    sqr = int(sqrt(n))
    for i in range(5, sqr+1, 6):
        if n % i == 0 or n % (i+2) == 0:
            return "NO"
    return "YES"


for t in range(int(input())):
    print(isprime(int(input()[-4:])))