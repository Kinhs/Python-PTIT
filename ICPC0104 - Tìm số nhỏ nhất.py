from re import *
n = int(input())
for i in range(n):
    xau = input()
    so = list(map(int, findall(r'\d+', xau)))
    print(min(so))
