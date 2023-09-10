a = list(map(int, input().split()))
while len(a) < 10:
    for i in list(map(int, input().split())):
        a.append(i)
ok = [0 for i in range(42)]
cnt = 0
for i in a:
    tmp = i % 42
    if ok[tmp] == 0:
        ok[tmp] += 1
        cnt += 1
print(cnt)
