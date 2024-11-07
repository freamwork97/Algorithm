n = int(input())
s = input()
chk = 0
for i in range(len(s)):
    if i % 2 == 0 and s[i] != 'I':
        chk += 1
    elif i % 2 == 1 and s[i] != 'O':
        chk += 1
print(chk)