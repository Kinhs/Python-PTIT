test = int(input())
for t in range(test):
    index = list(map(float, input().split()))
    cnt = 0
    while index[0] < index[2]:
        index[0] = index[0]*index[1]/100 + index[0]
        cnt += 1
    print(cnt)