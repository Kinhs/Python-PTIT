n = int(input())
arr = list(map(int, input().split()))
res = []
for i in range(n):
    if len(res) == 0:
        res.append(arr[i])
    elif (res[-1] + arr[i]) % 2 == 0:
        res.pop(-1)
    else:
        res.append(arr[i])
print(len(res))
