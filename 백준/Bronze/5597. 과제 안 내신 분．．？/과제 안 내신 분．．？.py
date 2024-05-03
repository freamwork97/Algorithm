l = list(range(1, 31))

for _ in range(28):
    i = int(input())
    l.remove(i)

for i in l:
    print(i)
