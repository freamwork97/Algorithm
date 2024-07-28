n = int(input())
l = list(map(int,input().split()))
index_l = [(l, i + 1) for i, l in enumerate(l)]
sorted_l = sorted(index_l, key=lambda x: x[0], reverse=True)[:3]
for i in sorted_l:
	print(i[1], end=' ')