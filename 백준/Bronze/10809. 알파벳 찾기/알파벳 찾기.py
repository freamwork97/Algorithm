from string import ascii_lowercase

l = list(ascii_lowercase)

s = input()

nl = [-1 for _ in range(len(l))]

for i in range(len(l)):
    for j in range(len(s)):
        if nl[i] == -1:
            if s[j] == l[i]:
                nl[i] = j

print(*nl)