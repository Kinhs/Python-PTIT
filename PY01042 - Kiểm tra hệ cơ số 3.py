def solution(s):
    for i in s:
        if i != '2' and i != '0' and i != '1':
            return "NO"
    return "YES"


for t in range(int(input())):
    print(solution(input()))