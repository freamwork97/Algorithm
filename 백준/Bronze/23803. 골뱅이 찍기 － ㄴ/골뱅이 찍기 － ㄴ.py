n = int(input())

# 아래로
for i in range(n * 4):
    print("@" * n)
    if i == n * 4 - 1:
        # 옆으로
        for _ in range(n):
            print("@" * 5 * n)