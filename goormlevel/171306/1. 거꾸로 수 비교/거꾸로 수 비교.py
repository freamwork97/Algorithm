a,b = map(str,input().split())

print(int(a)) if int(a[::-1]) > int(b[::-1]) else print(int(b))
