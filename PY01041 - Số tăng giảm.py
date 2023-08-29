def solution(s):
    i = 1
    while i < len(s) and int(s[i]) > int(s[i-1]):
        i += 1
    if i == 1:
        return "NO"
    if i == len(s):
        return "YES"
    while i < len(s):
        if s[i] >= s[i-1]:
            return "NO"
        i += 1
    return "YES"


for t in range(int(input())):
    s = input()
    print(solution(s))