x = int(input())
counter = 0
for i in range(1, int(x ** 0.5) + 1):
    for j in range(1, int(x ** 0.5) + 1):
        if i ** 2 + j ** 2 == x:
            counter += 1
print(counter // 2)