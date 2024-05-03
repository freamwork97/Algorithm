n = int(input())
nl = list(map(int, input().split()))
print(sum(nl) / n / max(nl) * 100)