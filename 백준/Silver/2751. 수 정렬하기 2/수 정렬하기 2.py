import sys

n = int(sys.stdin.readline())
l = [int(sys.stdin.readline()) for _ in range(n)]
l.sort()
for i in l:
    print(i)