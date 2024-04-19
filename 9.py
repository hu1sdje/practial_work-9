n = int(input())
counter = 0
def domino(n):
    return n * (n + 1) * (n + 2) // 2

print(domino(n))