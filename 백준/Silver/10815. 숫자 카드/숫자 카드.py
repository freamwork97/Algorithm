import sys

n = int(sys.stdin.readline())
card_list = set(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())
dis_list = list(map(int, sys.stdin.readline().split()))

answer = [1 if i in card_list else 0 for i in dis_list]
print(*answer)