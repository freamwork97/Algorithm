p = [1, 1, 2, 2, 2, 8]
n = list(map(int, input().split()))

for i in range(len(n)):
    if n[i] == p[i]:
        n[i] = 0
    elif n[i] > p[i]:
        n[i] = p[i] - n[i]
    elif n[i] < p[i]:
        n[i] = p[i] - n[i]
print(*n)
