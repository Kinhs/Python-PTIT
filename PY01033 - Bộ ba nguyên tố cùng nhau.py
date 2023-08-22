from math import gcd

lr = list(map(int, input().split()))
for i in range(lr[0], lr[1]-1):
    for j in range(i+1, lr[1]):
        for k in range(j+1, lr[1]+1):
            if gcd(i,j) == 1 and gcd(i,k) == 1 and gcd(k,j) == 1:
                print(f"({i}, {j}, {k})")
