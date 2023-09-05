def check(s):
    if len(s) < 3:
        return 'no'
    if s[-3:].lower() != ".py":
        return 'no'
    for i in s.lower():
        if i != '.' and i != '_' and (ord(i) > ord('z') or ord(i) < ord('a')):
            return 'no'
    return 'yes'


print(check(input()))