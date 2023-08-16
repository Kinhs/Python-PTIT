from math import gcd, sqrt


def is_prime(k):
    if k <= 1:
        return False
    for i in range(2, int(sqrt(k))+1):
        if k % i == 0:
            return False
    return True


t = int(input())
for i in range(t):
    n = int(input())
    cnt = 0
    for k in range(1, n):
        if gcd(n, k) == 1:
            cnt += 1
    if is_prime(cnt):
        print("YES")
    else:
        print("NO")