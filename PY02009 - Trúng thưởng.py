for t in range(int(input())):
    n = int(input())
    a = [0 for i in range(1001)]
    m = 0
    mindex = 0
    for i in range(n):
        tmp = int(input())
        a[tmp] += 1
        if a[tmp] > m:
            m = a[tmp]
            mindex = tmp
        if a[tmp] == m:
            if tmp < mindex:
                m = a[tmp]
                mindex = tmp
    print(mindex)
