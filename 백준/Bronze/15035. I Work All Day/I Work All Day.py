n = int(input())
h = list(map(int,input().split()))
t = int(input())

r = 0
n = []
s = 0
for i in h:
    r = t % i
    n.append(r)

for i in h:
    r = t % i
    if min(n) == r:
        s = i

print(s)