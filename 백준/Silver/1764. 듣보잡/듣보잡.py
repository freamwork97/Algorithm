n, m = map(int, input().split())
n_list = set(input() for _ in range(n))
m_list = [input() for _ in range(m)]

chk = 0
new = []
for i in m_list:
    if i in n_list:
        chk += 1
        new.append(i)
print(chk)
new = sorted(new, reverse=False)
for i in new:
    print(i)