t = int(input())
for _ in range(t):
    h, w, n = map(int, input().split())

    y = n % h if n % h else h
    x = n // h if n % h else n // h - 1
    print(y * 100 + x + 1)