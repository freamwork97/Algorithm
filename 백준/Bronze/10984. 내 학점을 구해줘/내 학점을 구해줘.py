T = int(input())

for _ in range(T):
    N = int(input())
    c = 0
    g = 0.0
    for i in range(N):
        x, y = map(float, input().split())
        c += int(x)
        g += y * int(x)
    print(f'{c} {g / c:.1f}')