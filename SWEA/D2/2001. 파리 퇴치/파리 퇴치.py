T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    flies = [list(map(int, input().split())) for _ in range(N)]
    max_flies = 0
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            curr_flies = sum(flies[i + x][j + y] for x in range(M) for y in range(M))
            max_flies = max(max_flies, curr_flies)
    print(f'#{t} {max_flies}')
