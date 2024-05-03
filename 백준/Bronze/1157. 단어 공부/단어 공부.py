s = input().upper()
s2 = list(set(s))

c = []

for i in s2:
    c.append(s.count(i))

if c.count(max(c)) > 1:
    print("?")
else:
    print(s2[c.index(max(c))])
