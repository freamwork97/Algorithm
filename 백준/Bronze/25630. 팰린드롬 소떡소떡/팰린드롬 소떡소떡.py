n = int(input())
p = input()
r_p = p[::-1]

chk = 0
for i in range(len(p)):
    if p[i] != r_p[i]:
        chk += 1
print(chk // 2)