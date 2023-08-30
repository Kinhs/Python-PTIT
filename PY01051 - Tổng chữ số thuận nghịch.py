def solution(s):
    if s < 10:
        return "NO"
    xau = str(s)
    for i in range(int(len(xau)/2)+1):
        if xau[i] != xau[len(xau)-i-1]:
            return "NO"
    return "YES"


for t in range(int(input())):
    s = sum([int(i) for i in input()])
    print(solution(s))