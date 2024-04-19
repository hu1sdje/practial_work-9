def stairs(n, m):
    if n == 0: return 1
    counter = 0
    if n <= 100:
        for i in range(min(n, m), -1, -1):
            counter += stairs(n - i, i - 1)
    return counter


n = int(input())
print(stairs(n, n))
