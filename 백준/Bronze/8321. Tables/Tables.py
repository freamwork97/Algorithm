n, k, s = map(int, input().split())
ks = k * s
# print(ks)
a = list(map(int, input().split()))
a = sorted(a, reverse=True)
# print(a)
for i in range(len(a)):
    ks = ks - a[i]
    if ks <= 0:
        print(len(a[: i + 1]))
        break