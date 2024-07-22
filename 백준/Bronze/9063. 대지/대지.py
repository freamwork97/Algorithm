n = int(input())
x = []
y = []

for _ in range(n):
    xi, yi = map(int, input().split())
    x.append(xi)
    y.append(yi)

if len(x) < 2:
    print(0)
else:
    print((max(x) - min(x)) * (max(y) - min(y)))