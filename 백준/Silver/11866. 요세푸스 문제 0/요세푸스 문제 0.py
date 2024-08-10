n, k = map(int, input().split())

l = [i for i in range(1, n + 1)]
answer = []
idx = 0

while l:
    idx = (idx + (k - 1)) % len(l)
    answer.append(str(l.pop(idx)))
print('<'+', '.join(answer)+'>')