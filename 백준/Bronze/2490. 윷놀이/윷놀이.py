for i in range(3):
    b = 0
    f = 0
    n = map(int, input().split())

    for j in n:
        if j == 0:
            b += 1
        else:
            f += 1

    if b == 0:
        print("E")
    elif b == 1:
        print("A")
    elif b == 2:
        print("B")
    elif b == 3:
        print("C")
    elif b == 4:
        print("D")