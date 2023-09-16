for t in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    dic = {}
    max_val = -1
    max_key = "NO"
    for i in a:
        if i not in dic.keys():
            dic[i] = 1
        else:
            dic[i] += 1
        if dic[i] <= n // 2:
            continue
        if dic[i] > max_val:
            max_key = i
            max_val = dic[i]
        elif i < max_key and dic[i] == max_val:
            max_key = i
    print(max_key)
