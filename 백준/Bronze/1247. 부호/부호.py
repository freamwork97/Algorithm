import sys

input = sys.stdin.readline

result = []
for _ in range(3):
    n = int(input())
    s = [int(input()) for _ in range(n)]
    if sum(s) == 0:
        result.append(0)
    elif sum(s) > 0:
        result.append("+")
    else:
        result.append("-")

for i in result:
    print(i)