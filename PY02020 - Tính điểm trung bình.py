n = int(input())
a = [float(i) for i in input().split()]
a.sort()
sum = 0
for i in a:
    if i == a[0] or i == a[-1]:
        n -= 1
        continue
    sum += i
print("{:.2f}".format(round(sum/n, 2)))