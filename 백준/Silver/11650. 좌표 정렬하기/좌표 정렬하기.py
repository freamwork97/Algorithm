n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]
l.sort()

for i in l:
    print(*i)