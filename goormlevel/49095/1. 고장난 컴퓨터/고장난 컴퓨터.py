n, c = map(int, input().split())

t_list = list(map(int, input().split()))
chk = 1
for i in range(len(t_list) - 1):
    if t_list[i + 1] - t_list[i] > c:
        chk = 1
    else:
        chk += 1
print(chk)
