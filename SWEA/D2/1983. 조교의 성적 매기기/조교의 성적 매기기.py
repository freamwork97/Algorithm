T = int(input())

grades = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    students = []
    for n in range(N):
        mid, final, hw = map(int, input().split())
        total = mid * 0.35 + final * 0.45 + hw * 0.2
        students.append([total, n + 1])
    students.sort(reverse=True)
    for i in range(N):
        if students[i][1] == K:
            print('#{} {}'.format(test_case, grades[i // (N // 10)]))
            break
