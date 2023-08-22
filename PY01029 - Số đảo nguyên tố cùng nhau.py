from math import gcd

test = int(input())
for t in range(test):
    so = int(input())
    if gcd(so, int(str(so)[::-1])) == 1:
        print("YES")
    else:
        print("NO")