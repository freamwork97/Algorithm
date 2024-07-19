import sys

n = int(input())
l = []

for _ in range(n):
    s = sys.stdin.readline().split()

    if s[0] == 'push':
        l.insert(0, s[-1])

    if s[0] == 'top':
        if len(l) == 0:
            print(-1)
        else:
            print(l[0])

    if s[0] == 'pop':
        if len(l) == 0:
            print(-1)
        else:
            p = l.pop(0)
            print(p)

    if s[0] == 'size':
        print(len(l))

    if s[0] == 'empty':
        if len(l) == 0:
            print(1)
        else:
            print(0)