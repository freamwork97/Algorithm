n, m = map(int, input().split())
s = {input() for _ in range(n)}

chk = 0
for _ in range(m):
    if input() in s:
        chk += 1

print(chk)