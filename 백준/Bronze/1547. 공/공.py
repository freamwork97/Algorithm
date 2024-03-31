m = int(input())
r = 1
for i in range(m):
    x, y = input().split()
    x = int(x)
    y = int(y)
    if x == r:
        r = y
    elif y == r:
        r = x
print(r)
