user_input = int(input())
for i in range(user_input):
	a,b = map(int,input().split())
	if a < b:
		print('Sunflower')
	elif a == b:
		print('Tulip')
	else:
		print('Rose')
