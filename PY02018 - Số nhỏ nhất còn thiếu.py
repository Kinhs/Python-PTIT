n = int(input())
a = [int(i) for i in input().split()]
a.sort()
res = 1
for i in a:
    if i > res:
        break
    elif i == res:
        res += 1
print(res)
