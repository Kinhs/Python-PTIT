def so_may_man(xau):
    index = list(xau)
    for i in index:
        if i != '4' and i != '7':
            return "NO"
    return "YES"


test = int(input())
for i in range(test):
    xau = input()
    print(so_may_man(xau))
