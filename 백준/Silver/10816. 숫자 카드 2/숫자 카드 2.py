import sys
from collections import Counter

n = int(sys.stdin.readline())
n_list = Counter(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())
m_list = list(map(int, sys.stdin.readline().split()))
for num in m_list:
    print(n_list[num], end=' ')