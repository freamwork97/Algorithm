while True:
    a, b, c = map(int, input().split())
    if a == b == c == 0:
        break
    i = a - b - c
    n = a // 2 + 1 - b
    if n <= 0:
        print(0)
    elif n <= i:
        print(n)
    else:
        print(-1)