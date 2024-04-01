import sys

input = sys.stdin.readline

r = [0 for _ in range(10001)]

for i in range(int(input())):
    r[int(input())] += 1

for i in range(len(r)):
    if r[i] != 0:
        for _ in range(r[i]):
            print(i)