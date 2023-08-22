from math import gcd

arr = list(map(int, input().split()))
cnt = 0
for i in range(10 ** (arr[1]-1), 10 ** arr[1]):
    if gcd(i, arr[0]) == 1:
        cnt += 1
        print(i, end=" ")
        if cnt == 10:
            print()
            cnt = 0