import sys

n = int(sys.stdin.readline())
user = [list(map(str, sys.stdin.readline().split())) for _ in range(n)]
enter = set()
for i, j in enumerate(user):
    if j[-1] == 'enter':
        enter.add(j[0])
    else:
        enter.remove(j[0])
enter = sorted(enter, reverse=True)
for i in enter:
    print(i)