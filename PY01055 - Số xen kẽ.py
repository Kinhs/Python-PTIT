def solve(s):
    if s[0] == s[1] or len(s) % 2 == 0:
        return "NO"
    for i in range(0, len(s)-1, 2):
        if s[i] != s[0]:
            return "NO"
    return "YES"


for t in range(int(input())):
    s = input()
    print(solve(s))