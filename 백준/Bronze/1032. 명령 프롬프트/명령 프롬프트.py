n = int(input())
l = [input() for _ in range(n)]
p = list(l[0])

for i in l:
    for j in range(len(i)):
        if i[j] != p[j]:
            p[j] = '?'

print(''.join(p))