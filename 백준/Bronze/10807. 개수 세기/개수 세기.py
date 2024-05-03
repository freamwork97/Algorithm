n = int(input())

l = list(map(int, input().split()))
c = 0
v = int(input())
for i in l:
    if i == v:
        c += 1

print(c)
