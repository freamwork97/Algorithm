n = int(input())
r = 0
for _ in range(n):
    s = list(map(int, input().split()))
    run = sorted(s[:2], reverse=True)
    t = sorted(s[2:], reverse=True)
    r = max(r, run[0] + sum(t[:2]))

print(r)