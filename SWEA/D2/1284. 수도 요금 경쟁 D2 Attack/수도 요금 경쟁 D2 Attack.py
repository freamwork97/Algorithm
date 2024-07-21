t = int(input())

for test_case in range(1, t + 1):
    p, q, r, s, w = map(int, input().split())

    a = p * w
    b = 0
    if r > w:
        b += q
    else:
        l = w - r
        b += q + s * l

    print(f'#{test_case} {b if a > b else a}')