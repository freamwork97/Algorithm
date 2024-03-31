import sys
from collections import deque

n = int(sys.stdin.readline())

l = deque(range(1, n + 1))
for i in range(n):
    if i == n - 1:
        break
    else:
        l.popleft()
        l.append(l[0])
    l.popleft()
print(l[0])