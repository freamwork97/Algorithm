from collections import Counter

s = ''
while True:
    try:
        s += input().rstrip()
    except EOFError:
        break

l = [i for i in s if i.isalpha()]

count = Counter(l)

max_value = max(count.values())
most_common = [k for k, v in count.items() if v == max_value]
most_common.sort()
for i in most_common:
    print(i, end='')