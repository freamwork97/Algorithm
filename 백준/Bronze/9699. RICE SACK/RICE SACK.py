n = int(input())

for i in range(1, n + 1):
    r = list(map(int, input().split()))
    print(f"Case #{i}: {max(r)}")
