n = input()
l = [int(i) for i in n]
l = sorted(l, reverse=True)
for i in l:
    print(i, end='')