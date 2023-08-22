def chanle(arr):
    tong = 0
    for i in range(len(arr)-1):
        if abs(arr[i]-arr[i+1]) != 2:
            return "NO"
        tong += arr[i]
    if (tong + arr[-1]) % 10 == 0:
        return "YES"
    return "NO"


test = int(input())
for t in range(test):
    arr = list(int(i) for i in input())
    print(chanle(arr))