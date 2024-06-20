t = int(input())

for _ in range(t):
    s, n = input().split()
    n = int(n)
    new_s = s[-n:] + s[:-n]
    print(f'Shifting {s} by {n} positions gives us: {new_s}')