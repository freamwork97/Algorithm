n = int(input())

s = []
for _ in range(n):
    s.append(input())

s = list(set(s))

s.sort()
s.sort(key=lambda i: len(i))
for i in s:
    print(i)