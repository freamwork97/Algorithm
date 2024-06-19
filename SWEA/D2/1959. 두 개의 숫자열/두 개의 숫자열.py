T = int(input())

for t in range(1, T + 1):

    N, M = map(int, input().split())
    Ai = list(map(int, input().split()))
    Bj = list(map(int, input().split()))

    if N < M:
        Ai, Bj = Bj, Ai
        N, M = M, N

    max_value = float('-inf')

    for i in range(N - M + 1):
        value = sum(a * b for a, b in zip(Ai[i:i + M], Bj))
        max_value = max(max_value, value)

    print(f'#{t} {max_value}')
