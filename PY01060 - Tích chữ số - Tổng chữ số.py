for t in range(int(input())):
    l = list(int(i) for i in input())
    tong = 0
    tich = 1
    for i in range(len(l)):
        if i % 2 == 0:
            if l[i] == 0:
                continue
            else:
                tich *= l[i]
        else:
            tong += l[i]
    print(f"{tich} {tong}")