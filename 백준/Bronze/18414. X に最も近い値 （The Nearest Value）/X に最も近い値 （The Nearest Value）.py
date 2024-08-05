x, l, r = map(int, input().split())
lst = [abs(i - x) for i in range(l, r + 1)]
lr = [i for i in range(l, r + 1)]
print(lr[lst.index(min(lst))])
