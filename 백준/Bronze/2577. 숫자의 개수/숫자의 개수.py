a = int(input())
b = int(input())
c = int(input())

n = a * b * c
n_l = [0] * 10
for i in str(n):
    for j in range(len(n_l)):
        if i == str(j):
            n_l[j] += 1
for i in n_l:
    print(i)