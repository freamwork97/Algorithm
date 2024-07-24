n = int(input())

for i in range(n):
    for j in range(n):
        if i in [0, n - 1] and j in [0, n - 1]:
            print('|', end='')
        elif i in [0, n - 1]:
            print('-', end='')
        elif j in [0, n - 1]:
            print('|', end='')
        elif i == j or i + j == n - 1:
            print('*', end='')
        else:
            print(' ', end='')
    print()