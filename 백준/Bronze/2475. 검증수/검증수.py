l = list(map(int, input().split()))

result = (l[0] ** 2 + l[1] ** 2 + l[2] ** 2 + l[3] ** 2 + l[4] ** 2) % 10
print(result)