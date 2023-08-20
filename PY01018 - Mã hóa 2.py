P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
pList = list(i for i in P)
while True:
    userInput = list(input().split())
    if userInput[0] == "0":
        break
    res = ""
    for char in userInput[1]:
        res = res + pList[(pList.index(char) + int(userInput[0])) % 28]
    print(res[::-1])