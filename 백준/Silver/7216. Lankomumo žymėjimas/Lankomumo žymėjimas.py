n, k = map(int, input().split())
l = list(map(int, input().split()))

a = l[k - 1]
la = l[k - 1]
for i in range(1, n + 1):
    if i == 1:
        la = a
    else:
        la = l[la - 1]

print(l.index(la) + 1)