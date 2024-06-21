import sys

A, B, C = map(int, sys.stdin.readline().split())
for _ in range(C % 2):
    A ^= B
print(A)