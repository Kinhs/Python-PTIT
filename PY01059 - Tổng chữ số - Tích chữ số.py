for t in range(int(input())):
    l = list(int(i) for i in input())
    tong = 0
    tich = 0
    for i in range(len(l)):
        if i % 2 == 0:
            tong += l[i]
        else:
            if l[i] == 0:
                continue
            elif tich == 0:
                tich = l[i]
            else:
                tich *= l[i]
    print(f"{tong} {tich}")