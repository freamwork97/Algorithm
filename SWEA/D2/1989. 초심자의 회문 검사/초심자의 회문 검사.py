T = int(input())

for test_case in range(1, T + 1):
    s = input()
    s_list = []
    revers_s_list = []
    num = 0
    for i in s:
        s_list.append(i)
    for i in s[::-1]:
        revers_s_list.append(i)
    if s_list == revers_s_list:
        num += 1
    print(f"#{test_case} {num}")
