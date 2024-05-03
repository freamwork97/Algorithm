n, m = map(int, input().split())
b = [0] * (n + 1)

for _ in range(m):
    i, j, k = map(int, input().split())

    for n in range(i, j + 1):
        b[n] = k
b.remove(0)

print(*b)
