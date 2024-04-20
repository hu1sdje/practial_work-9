n = int(input())
counter = 0
for i in range(n + 1):
    for j in range(i, n + 1):
        counter += i + j
print(counter)
