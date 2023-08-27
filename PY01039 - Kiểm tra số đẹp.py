def solution(s):
    if s[0] == s[1]:
        return "NO"
    for i in range(len(s)):
        if i % 2 == 0:
            if s[i] != s[0]:
                return "NO"
        else:
            if s[i] != s[1]:
                return "NO"
    return "YES"


for t in range(int(input())):
    s = input()
    print(solution(s))
