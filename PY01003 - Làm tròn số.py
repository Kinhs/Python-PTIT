n = int(input())
for i in range(n):
    num = input()
    if len(num) == 1:
        print(num)
    else:
        j = len(num) - 2
        res = list(num)
        while j >= 0:
            if int(res[j+1]) >= 5:
                res[j] = str(int(res[j]) + 1)
            res[j+1] = '0'
            j -= 1
        print("".join(res))
        