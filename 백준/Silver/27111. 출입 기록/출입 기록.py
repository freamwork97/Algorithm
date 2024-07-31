import sys

N = int(sys.stdin.readline())
l = [0] * 200001
answer = 0
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    if y == 0:
        if l[x] == 1:
            l[x] = 0
        else:
            answer += 1
    else:
        if l[x] == 1:
            answer += 1
        else:
            l[x] = 1

for i in range(len(l)):
    if l[i] != 0:
        answer += 1

print(answer)