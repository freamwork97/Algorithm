t = int(input())

for test_case in range(1, t + 1):

    l = list(map(int, input().split()))[1:]
    chk = 0
    for i in range(len(l)):
        j = i
        while j > 0 and l[j - 1] > l[j]:
            l[j - 1], l[j] = l[j], l[j - 1]
            chk += 1
            j -= 1
    print(f'{test_case} {chk}')