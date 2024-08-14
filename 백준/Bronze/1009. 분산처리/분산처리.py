t = int(input())

for _ in range(t):
    a, b = map(int, input().split())

    a %= 10
    if a == 1 or a == 5 or a == 6:
        print(a)
    elif a == 0:
        print(10)
    else:
        b = b % 4
        if b == 0:
            b = 4
        print((a ** b) % 10)