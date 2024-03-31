t = int(input())  # 테스트 케이스
q = 25
d = 10
n = 5
p = 1


m = []
for _ in range(t):
    m.append(int(input()))

for i in m:
    for j in [q, d, n, p]:
        print(i // j, end=" ")
        i = i % j
    print()
