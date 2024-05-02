h, m = map(int, input().split())

if m - 45 < 0:
    if h == 0:
        h = 24
    m = m + 60 - 45
    h -= 1
else:
    m = m - 45

print(h, m)