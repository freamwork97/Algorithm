n = int(input())

s = input()
b = 0
r = 0
for i in range(1, len(s) + 1):
    if s[i - 1] == 'X':
        b = 0
    else:
        r += i + b
        b += 1
print(r)