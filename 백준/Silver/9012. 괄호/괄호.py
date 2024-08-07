n = int(input())

for _ in range(n):
    l = input()
    for i in range(len(l)):
        l = l.replace("()", "")

    if len(l) == 0:
        print('YES')
    else:
        print('NO')