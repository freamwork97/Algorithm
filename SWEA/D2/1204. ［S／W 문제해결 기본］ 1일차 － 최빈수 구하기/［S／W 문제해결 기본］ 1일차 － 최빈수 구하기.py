from collections import Counter

t = int(input())

for i in range(1, t + 1):
    test_num = int(input())
    n_list = list(map(int, input().split()))
    cnt = Counter(n_list)
    print(f'#{i} {cnt.most_common(1)[0][0]}')