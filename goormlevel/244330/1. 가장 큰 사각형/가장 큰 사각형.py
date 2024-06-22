T = int(input())
s = []
for _ in range(T):
	w,h = map(int,input().split())
	s.append(w*h)
	
print(max(s))
