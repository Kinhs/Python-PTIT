index = list(map(int, input().split()))
du = index[1] - index[0] % index[1]
if index[0] + du > index[2]:
    print(-1)
else:
    adder = 0
    while du + adder + index[0] <= index[2]:
        print(du + adder, end=' ')
        adder += index[1]