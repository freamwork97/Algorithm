l = [int(input()) for _ in range(5)]
l.sort()
print(sum(l) // len(l))
print(l[2])