N = int(input())

S = input()
r = 0
l = 0

for i in range(len(S)):
	if S[i] == 'O':
		r+=1+l
		try:
			if S[i] == S[i+1]:
				l+=1
		except:
			pass
	else:
		l=0
print(r)
