user_input = int(input())
N = 0
for _ in range(user_input):
	c,v = map(str,input().split())
	if c == 'in':
		N+=int(v)
	else:
		N-=int(v)
	if N <0:
		break
if N >=0:
	print('success')
else:
	print('fail')
