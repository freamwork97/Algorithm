import sys

m = int(input())
s = set()
for _ in range(m):
    op = sys.stdin.readline().strip().split()
    if op[0] == 'add':
        s.add(int(op[1]))
    elif op[0] == 'remove':
        s.discard(int(op[1]))
    elif op[0] == 'check':
        print(1 if int(op[1]) in s else 0)
    elif op[0] == 'toggle':
        if int(op[1]) in s:
            s.discard(int(op[1]))
        else:
            s.add(int(op[1]))
    elif op[0] == 'all':
        s = set([i for i in range(1, 21)])
    else:
        s = set()