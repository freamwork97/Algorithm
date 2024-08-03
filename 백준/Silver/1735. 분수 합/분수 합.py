def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())

n = a1 * b2 + b1 * a2
d = b1 * b2
g = gcd(n, d)

print(f'{n // g} {d // g}')