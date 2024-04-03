n = int(input())

for _ in range(n):
    c, p = map(int, input().split())
    print(c, p)
    if c > 1:
        print(p * c - (c - 1) * 2)
    else:
        print(p)