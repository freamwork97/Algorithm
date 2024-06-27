T = int(input())

for test_case in range(1, T + 1):

    N = int(input())
    result = ''

    for _ in range(N):
        s, l = input().split()
        l = int(l)
        result += s * l

    print(f'#{test_case}')

    while result:
        print(result[:10])
        result = result[10:]