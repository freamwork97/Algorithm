n = int(input())
k = int(input())

total = 0
for _ in range(k + 1):
    total += n
    n *= 10
print(total)