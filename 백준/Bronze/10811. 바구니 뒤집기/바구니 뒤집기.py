n, m = map(int, input().split())
l = list(range(1, n + 1))
for _ in range(m):
    i, j = map(int, input().split())

    l[i - 1 : j] = reversed(l[i - 1 : j])
print(*l)
