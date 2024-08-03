n, m = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))
lst = []
for i in a:
    if i not in b:
        lst.append(i)
for i in b:
    if i not in a:
        lst.append(i)
print(len(lst))