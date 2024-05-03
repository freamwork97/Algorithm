l = []
l2 = []
for _ in range(10):
    l.append(int(input()))

for i in l:
    l2.append(i % 42)

l2 = set(l2)
l2 = list(l2)
print(len(l2))
