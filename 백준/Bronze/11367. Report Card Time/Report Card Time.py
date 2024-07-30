t = int(input())

for _ in range(t):
    n, s = input().split()
    s = int(s)
    if s >= 97:
        print(f'{n} A+')
    elif s >= 90:
        print(f'{n} A')
    elif s >= 87:
        print(f'{n} B+')
    elif s >= 80:
        print(f'{n} B')
    elif s >= 77:
        print(f'{n} C+')
    elif s >= 70:
        print(f'{n} C')
    elif s >= 67:
        print(f'{n} D+')
    elif s >= 60:
        print(f'{n} D')
    else:
        print(f'{n} F')