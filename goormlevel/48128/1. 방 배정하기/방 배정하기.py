a,b,c,s = map(int,input().split())

count = 0
for i in range(s//a+1):
    for j in range(s//b+1):
        for k in range(s//c+1):
            if a * i + b * j + c * k == s:
                count = 1
if count > 0:
	print(1)
else:
	print(0)
