n = int(input())

l = []
for i in range(n):
    x, y = input().split()
    x = int(x)
    l.append([x, y])

l = sorted(l, key=lambda x: x[0])
for i in l:
    print(*i)