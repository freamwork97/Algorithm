from collections import deque

N, M = map(int, input().split())
A = deque(map(int, input().split()))

for _ in range(M):
    d = A[0]
    A.rotate(-d)

print(A[0])


