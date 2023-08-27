from math import sqrt


def solution(s):
    if len(s) < 2:
        return "NO"
    for i in range(2, int(sqrt(len(s))) + 1):
        if len(s) % i == 0:
            return "NO"
    cnt = 0
    for i in s:
        if i == '2' or i == '3' or i == '5' or i == '7':
            cnt += 1
    if cnt <= len(s)/2:
        return "NO"
    return "YES"


for t in range(int(input())):
    s = input()
    print(solution(s))