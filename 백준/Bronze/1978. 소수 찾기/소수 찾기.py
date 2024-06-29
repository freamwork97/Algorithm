N = int(input())
l = list(map(int, input().split()))
chk = 0

for i in l:
    if i < 2:
        continue
    is_prime = True

    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        chk += 1

print(chk)