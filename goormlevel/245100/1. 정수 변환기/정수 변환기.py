N, K = map(int, input().split())

s = input()
new_s = ''
for i in range(len(s)):
	new_s += str(int(s[i])+K)
print(new_s)
