import sys

n, m = map(int, sys.stdin.readline().split())
n_dict = {sys.stdin.readline(): i for i in range(1, n + 1)}
n_list = list(n_dict.keys())

for _ in range(m):
    s = sys.stdin.readline()
    try:
        s = int(s)
        print(n_list[s - 1].rstrip())
    except ValueError:
        print(n_dict[s])