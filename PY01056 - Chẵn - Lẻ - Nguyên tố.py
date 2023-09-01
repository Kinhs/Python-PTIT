from math import sqrt


def isprime(a):
    if a <= 2:
        return False
    for i in range(2, int(sqrt(a)) + 1):
        if a % i == 0:
            return False
    return True


def solve(l):
    sum = 0
    for i in range(len(l)):
        if l[i] % 2 == 0 and i % 2 == 1:
            return "NO"
        if l[i] % 2 == 1 and i % 2 == 0:
            return "NO"
        sum += l[i]
    if isprime(sum):
        return "YES"
    return "NO"


for t in range(int(input())):
    l = list(int(i) for i in input())
    print(solve(l))
