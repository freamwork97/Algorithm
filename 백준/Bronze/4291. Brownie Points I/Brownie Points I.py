while True:
    s = 0
    o = 0
    xl = []
    yl = []
    b = int(input())
    if b == 0:
        break
    for _ in range(b):
        x, y = map(int, input().split())
        xl.append(x)
        yl.append(y)

    for i, j in zip(xl, yl):
        if (
            i > xl[(len(xl) + 1) // 2 - 1] and j > yl[(len(yl) + 1) // 2 - 1]
        ):  # x,y: 양수
            s += 1
        elif (
            i < xl[(len(xl) + 1) // 2 - 1] and j > yl[(len(yl) + 1) // 2 - 1]
        ):  # x:음수, y:양수
            o += 1
        elif (
            i < xl[(len(xl) + 1) // 2 - 1] and j < yl[(len(yl) + 1) // 2 - 1]
        ):  # x,y: 음수
            s += 1
        elif i > xl[(len(xl) + 1) // 2 - 1] and j < yl[(len(yl) + 1) // 2 - 1]:
            o += 1
    print(s, o)