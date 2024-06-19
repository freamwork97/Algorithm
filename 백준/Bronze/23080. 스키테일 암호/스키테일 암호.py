n = int(input())
s = input()

answer = ''
for i in range(len(s)):
    if i % n == 0:
        answer += s[i]
print(answer)