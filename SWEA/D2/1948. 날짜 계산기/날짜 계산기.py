T = int(input())
month_list = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for test_case in range(1, T + 1):
    m1, d1, m2, d2 = map(int, input().split())

    days = 0

    if m1 == m2:
        days = d2 - d1 + 1
    else:
        days += month_list[m1] - d1 + 1

        for m in range(m1 + 1, m2):
            days += month_list[m]

        days += d2

    print(f'#{test_case} {days}')