T = int(input())

for test_case in range(1, T + 1):
    s = input()
    s_list = [i for i in s]
    revers_s_list = [i for i in s[::-1]]
    num = 1 if s_list == revers_s_list else 0
    print(f"#{test_case} {num}")
