u = 0
m = 0
for _ in range(10):
    s, p = input().split()
    s = int(s)
    p = int(p)
    u = u + p - s
    if u > m:
        m = u

print(m)