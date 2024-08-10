while True:
    n = int(input())
    if n == -1:
        break
    result = 0
    m, h = [], []
    for _ in range(n):
        mn, hn = map(int, input().split())
        m.append(mn)
        h.append(hn)

    for i in range(n):
        if i == 0:
            result += m[i] * h[i]
        else:
            result += m[i] * (h[i] - h[i - 1])
    print(f'{result} miles')