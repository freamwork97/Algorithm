t = int(input())
for _ in range(t):
    s = input()
    chk = 0
    answer = 0
    for i in s:
        if i == 'O':
            answer += 1 + chk
            chk += 1
        else:
            chk = 0
    print(answer)