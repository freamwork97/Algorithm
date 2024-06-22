N = int(input())
schedule = [list(map(int, input().split())) for _ in range(N)]

schedule.sort(key=lambda x: (x[1], x[0]))

last = 0
cnt = 0
for s, e in schedule:
    if s > last:  
        cnt += 1
        last = e

print(cnt)
