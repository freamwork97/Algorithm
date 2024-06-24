N = int(input())

s = list(map(str, input().split()))
start = s[0][0]
chk = 1
for i in s:
    if i == i[::-1] and i[0] == start:
        pass
    else:
        chk = 0
        break
print(chk)