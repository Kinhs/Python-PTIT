test = int(input())
for t in range(test):
    n = int(input())
    print(1, end=" ")
    i = 2
    while i <= n:
        cnt = 0
        while n % i == 0:
            cnt += 1
            n /= i
        if cnt > 0:
            print(f"* {i}^{cnt} ", end="")
        i += 1
    print()