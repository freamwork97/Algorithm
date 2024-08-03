s = input()
len_s = len(s)
total = set(s[i:j + 1] for i in range(len_s) for j in range(i, len_s + 1))

print(len(total))