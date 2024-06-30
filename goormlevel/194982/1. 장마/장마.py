n, m = map(int, input().split())

k = list(map(int, input().split()))
r = set()

for i in range(1, m + 1):

    s, e = map(int, input().split())

    for j in range(s, e + 1):
        k[j - 1] += 1
        r.add(j)

    if i % 3 == 0:
        for l in r:
            k[l - 1] -= 1
        r.clear()

for i in k:
    print(i, end=' ')
