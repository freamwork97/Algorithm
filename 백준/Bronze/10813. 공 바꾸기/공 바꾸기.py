n, m = map(int, input().split())
l = list(range(1, n + 1))

for _ in range(m):
    i, j = map(int, input().split())
    t = l[i - 1]
    l[i - 1] = l[j - 1]
    l[j - 1] = t

print(*l)
