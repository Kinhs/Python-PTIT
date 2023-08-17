test = int(input())
for t in range(test):
    xau = input()
    if xau[:2] == xau[-2:]:
        print("YES")
    else:
        print("NO")