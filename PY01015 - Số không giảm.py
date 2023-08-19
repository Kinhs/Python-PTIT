def koGiam(xau):
    xau = [int(i) for i in xau]
    for i in range(len(xau) - 1):
        if xau[i] > xau[i+1]:
            return "NO"
    return "YES"


test = int(input())
for t in range(test):
    xau = input()
    print(koGiam(xau))