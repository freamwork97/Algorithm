t = int(input())

for _ in range(t):
    x, y = map(int, input().split())

    dis = y - x
    cnt = 0
    k = 1
    while dis > 0:
        dis -= k
        cnt += 1
        if cnt % 2 == 0:
            k += 1
    print(cnt)