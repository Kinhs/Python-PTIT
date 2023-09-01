for i in range(int(input())):
    res = 1
    for i in input():
        if int(i) == 0:
            continue
        res *= int(i)
    print(res)