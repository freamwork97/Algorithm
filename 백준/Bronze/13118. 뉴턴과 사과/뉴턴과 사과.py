m = list(map(int, input().split()))  # 사람 좌표 저장

x, y, r = map(int, input().split())

if x in m:
    result = m.index(x) + 1
else:
    result = 0

print(result)

