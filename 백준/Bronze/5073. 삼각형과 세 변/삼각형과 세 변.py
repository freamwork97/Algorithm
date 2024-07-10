while True:
    n1, n2, n3 = map(int, input().split())
    if n1 == n2 == n3 == 0:
        break

    if n1 == n2 and n1 == n3 and n2 == n3:
        print('Equilateral')
    elif n1 == n2 != n3 or n3 == n1 != n2 or n3 == n2 != n1:
        if max(n1, n2, n3) >= n1 + n2 + n3 - max(n1, n2, n3):
            print('Invalid')
        else:
            print('Isosceles')
    else:
        if max(n1, n2, n3) >= n1 + n2 + n3 - max(n1, n2, n3):
            print('Invalid')
        else:
            print('Scalene')