n, w, h = map(int, input().split())
p = w * w + h * h
for _ in range(n):
    i = int(input())
    if i * i > p:
        print('NO')
    else:
        print('YES')