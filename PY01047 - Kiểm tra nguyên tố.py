from math import sqrt


def solution(n):
    if n < 2:
        return "NO"
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return "NO"
    return "YES"


for t in range(int(input())):
    n = int(input()[-4:])
    print(solution(n))