test = int(input())
for t in range(test):
    danhSach = list(i for i in input())
    res = ""
    i = 0
    while i < len(danhSach):
        cnt = 1
        while i + 1 < len(danhSach) and danhSach[i+1] == danhSach[i]:
            cnt += 1
            i += 1
        res = res + str(cnt) + danhSach[i]
        i += 1
    print(res)