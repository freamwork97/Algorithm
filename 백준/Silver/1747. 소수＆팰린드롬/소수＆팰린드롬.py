N = int(input())

while True:
    if N < 2:
        a = False
    else:
        a = True
        for i in range(2, int(N ** 0.5) + 1):
            if N % i == 0:
                a = False
                break

    if a == True and str(N) == str(N)[::-1]:
        print(N)
        break

    N += 1