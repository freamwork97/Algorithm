n, k = map(int,input().split())
l = list(map(int,input().split()))
r = 0
for i in l:
	if i % k != 0:
		r+=i
		
print(r)
