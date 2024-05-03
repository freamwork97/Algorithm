t = int(input())

for i in range(t):
    p = ""
    r, s = input().split()
    r = int(r)
    for j in s:
        p += j * r
    print(p)
