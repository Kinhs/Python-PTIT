while True:
    a = [int(i) for i in input().split()]
    if a == [0, 0, 0, 0]:
        break
    cnt = 0
    while not (a[0] == a[1] == a[2] == a[3]):
        cnt += 1
        tmp = a[0]
        for i in range(3):
            a[i] = abs(a[i]-a[i+1])
        a[3] = abs(a[3]-tmp)
    print(cnt)