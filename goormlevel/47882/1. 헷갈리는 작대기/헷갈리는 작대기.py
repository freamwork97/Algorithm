n = input()

l = [0,0,0,0]

for i in n:
	if i == '1':
		l[0]+=1
	elif i == 'I':
		l[1]+=1
	elif i == 'l':
		l[2]+=1
	elif i == '|':
		l[3]+=1
for i in l:
	print(i)