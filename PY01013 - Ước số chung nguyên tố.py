from math import gcd, sqrt


def is_prime(n):
    res = sum(i for i in list(map(int, str(n))))
    if res <= 1:
        return False
    for i in range(2, int(sqrt(res))+1):
        if res % i == 0:
            return False
    return True


test = int(input())
for t in range(test):
    index = list(map(int, input().split()))
    if is_prime(gcd(index[0], index[1])):
        print("YES")
    else:
        print("NO")