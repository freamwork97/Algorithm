n, m = map(int, input().split())
n_l = list(map(int, input().split()))
m_l = list(map(int, input().split()))

for i in range(n):
    temp = []
    for j in range(m):
        if n_l[i] == m_l[j]:
            n_l[i] = 0
            temp.append(n_l[i])
        else:
            n_l[i] = 1
            temp.append(n_l[i])
    m_l = temp
print(m_l[-1])