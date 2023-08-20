test = int(input())
for t in range(test):
    danhSach = list(i for i in input())
    res = ""
    while len(danhSach) > 0:
        res = res + danhSach[0]*int(danhSach[1])
        danhSach.pop(0)
        danhSach.pop(0)
    print(res)