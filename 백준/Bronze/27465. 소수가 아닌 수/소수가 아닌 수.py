n = int(input())

l = []
for i in range(n + 1, 10 ** 6):
    if 10 ** 9 % i == 0:
        l.append(i + 2)
print(l[0])