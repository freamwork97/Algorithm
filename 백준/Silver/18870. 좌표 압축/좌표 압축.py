n = int(input())
l = list(map(int, input().split()))

sorted_l = sorted(list(set(l)))
dict_l = {sorted_l[i]: i for i in range(len(sorted_l))}
r = [dict_l[i] for i in l]

print(*r)