while True:
    n1, n2 = map(int, input().split())

    if n1 == n2 == 0:
        break

    if n1 % n2 == 0:
        print("multiple")
    elif n2 % n1 == 0:
        print('factor')
    else:
        print("neither")
