T = int(input())

for test_case in range(1, T + 1):
    h1, m1, h2, m2 = map(int, input().split())
    m = m1 + m2
    h = h1 + h2

    # Adjust the hours and minutes if necessary
    if m >= 60:
        h += 1
        m %= 60

    if h > 12:
        h %= 12

    # It seems like we need to ensure the hour is not 0, if it is then we should set it to 12.
    if h == 0:
        h = 12

    print(f'#{test_case} {h} {m}')
