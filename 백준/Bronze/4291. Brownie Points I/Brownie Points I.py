import sys

while True:
    s = 0
    o = 0
    xl = []
    yl = []
    b = int(input())
    if b == 0:
        break
    for _ in range(b):
        x, y = map(int, sys.stdin.readline().split())
        xl.append(x)
        yl.append(y)

    for i, j in zip(xl, yl):
        if i > xl[(len(xl) + 1) // 2 - 1] and j > yl[(len(yl) + 1) // 2 - 1]:  # 1사분면
            s += 1
        elif (
            i < xl[(len(xl) + 1) // 2 - 1] and j > yl[(len(yl) + 1) // 2 - 1]
        ):  # 2사분면
            o += 1
        elif (
            i < xl[(len(xl) + 1) // 2 - 1] and j < yl[(len(yl) + 1) // 2 - 1]
        ):  # 3사분면
            s += 1
        elif (
            i > xl[(len(xl) + 1) // 2 - 1] and j < yl[(len(yl) + 1) // 2 - 1]
        ):  # 4사분면
            o += 1
    print(s, o)