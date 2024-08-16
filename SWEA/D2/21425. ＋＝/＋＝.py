t = int(input())

for _ in range(t):
    x, y, n = map(int, input().split())
    count = 0

    while x <= n and y <= n:
        if x < y:
            x += y
        else:
            y += x
        count += 1

    print(count)