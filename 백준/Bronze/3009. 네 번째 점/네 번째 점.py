l = list(list(map(int, input().split())) for _ in range(3))

x = l[0][0] ^ l[1][0] ^ l[2][0]
y = l[0][1] ^ l[1][1] ^ l[2][1]

print(x, y)