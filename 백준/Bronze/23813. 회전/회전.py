n = int(input())
str_n = str(n)
r = [n]

for i in range(len(str_n) - 1):
    str_n = str_n[-1] + str_n[:-1]

    r.append(int(str_n))

print(sum(r))
