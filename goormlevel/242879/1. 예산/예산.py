N,M = map(int,input().split())

for _ in range(N):
	c,v = map(int,input().split())
	M -= c*v
	
if M >=0:
	print(M)
else:
	print('No')
