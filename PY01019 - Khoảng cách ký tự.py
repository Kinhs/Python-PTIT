test = int(input())
for t in range(test):
    xau = input()
    xau_dao = xau[::-1]
    res = "YES"
    for i in range(1, len(xau)):
        if abs(ord(xau[i]) - ord(xau[i-1])) != abs(ord(xau_dao[i]) - ord(xau_dao[i-1])):
            res = "NO"
            break
    print(res)