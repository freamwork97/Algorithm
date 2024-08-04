import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())

    while True:
        chk = True
        if n < 2:
            chk = False
            print(2)
            break
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                chk = False
                break
        if chk:
            print(n)
            break
        n += 1