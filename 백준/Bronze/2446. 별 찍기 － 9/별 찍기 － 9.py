n = int(input())

a = [(" " * (n - i) + "*" * (2 * i - 1)) for i in range(n, 0, -1)]

a += [(" " * (n - i) + "*" * (2 * i - 1)) for i in range(2, n + 1)]
for i in a:
    print(i)