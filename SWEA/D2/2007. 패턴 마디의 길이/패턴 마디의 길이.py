T = int(input())
for test_case in range(1, T + 1):
    word = input()
    for i in range(1, 11):
        if word[:i] == word[i:2 * i] and word[:i] == word[2 * i:3 * i]:
            result = len(word[:i])
            break
    print(f'#{test_case} {result}')
