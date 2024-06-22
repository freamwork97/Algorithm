N = int(input())

p = list(map(int,input().split()))
p1,p2,p3,p4,p5 = [],[],[],[],[]
answer=0
for _ in range(N):
	l, t = map(int,input().split())
	if l == 1:
		p1.append(t)
	elif l == 2:
		p2.append(t)
	elif l == 3:
		p3.append(t)
	elif l ==4:
		p4.append(t)
	else:
		p5.append(t)
p1 = sorted(p1)
p2 = sorted(p2)
p3 = sorted(p3)
p4 = sorted(p4)
p5 = sorted(p5)
p1 = p1[:p[0]]
p2 = p2[:p[1]]
p3 = p3[:p[2]]
p4 = p4[:p[3]]
p5 = p5[:p[4]]
answer = sum(p1) +sum(p2)+sum(p3)+sum(p4)+sum(p5)

for _ in range(len(p)-1):
	answer+=60
	
for i in range(len(p1)):
	try: 
		if p1[i] != p1[i+1]:
			answer+=abs(p1[i]-p1[i+1])
	except:
		pass
for i in range(len(p2)):
	try: 
		if p2[i] != p2[i+1]:
			answer+=abs(p2[i]-p2[i+1])
	except:
		pass
for i in range(len(p3)):
	try: 
		if p3[i] != p3[i+1]:
			answer+=abs(p3[i]-p3[i+1])
	except:
		pass
for i in range(len(p4)):
	try: 
		if p4[i] != p4[i+1]:
			answer+=abs(p4[i]-p4[i+1])
	except:
		pass
for i in range(len(p5)):
	try: 
		if p5[i] != p5[i+1]:
			answer+=abs(p5[i]-p5[i+1])
	except:
		pass
print(answer)
