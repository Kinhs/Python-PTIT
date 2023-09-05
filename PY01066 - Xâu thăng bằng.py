for t in range(int(input())):
    s = input()
    s_dao = s[::-1]
    ok = True
    for i in range(1, len(s)):
        if abs(ord(s[i]) - ord(s[i-1])) != abs(ord(s_dao[i]) - ord(s_dao[i-1])):
            ok = False
    if ok:
        print("YES")
    else:
        print("NO")
