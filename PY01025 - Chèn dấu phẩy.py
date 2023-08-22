xau = input()[::-1]
cnt = 0
res = ""
for i in range(len(xau)):
    cnt += 1;
    res = xau[i] + res
    if cnt == 3 and i != len(xau) - 1:
        res = "," + res
        cnt = 0
print(res)
