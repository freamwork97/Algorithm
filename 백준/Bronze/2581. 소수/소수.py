M = int(input())
N = int(input())

chk = []

for i in range(M, N + 1):
    if i < 2:
        continue
    is_prime = True
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        chk.append(i)

if len(chk) == 0:
    print(-1)
else:
    print(sum(chk))
    print(min(chk))