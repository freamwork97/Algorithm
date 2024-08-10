import sys
from collections import deque

n = int(sys.stdin.readline())
q = deque()
for _ in range(n):
    s = sys.stdin.readline().split()

    if s[0] == '1':
        q.appendleft(s[1])
    elif s[0] == '2':
        q.append(s[1])
    elif s[0] == '3':
        if len(q) > 0:
            print(q.popleft())
        else:
            print(-1)
    elif s[0] == '4':
        if len(q) > 0:
            print(q.pop())
        else:
            print(-1)
    elif s[0] == '5':
        print(len(q))
    elif s[0] == '6':
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif s[0] == '7':
        if len(q) > 0:
            print(q[0])
        else:
            print(-1)
    else:
        if len(q) > 0:
            print(q[-1])
        else:
            print(-1)