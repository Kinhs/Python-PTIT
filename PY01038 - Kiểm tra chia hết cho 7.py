def solution(n):
    for i in range(1000):
        if n % 7 == 0:
            return n
        n += int(str(n)[::-1])
    return -1


test = int(input())
for t in range(test):
    n = int(input())
    print(solution(n))
