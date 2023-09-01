for t in range(int(input())):
    s = 0
    for i in input():
        s += int(i)
    if s % 3 == 0:
        print("YES")
    else:
        print("NO")