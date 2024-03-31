k = int(input())  # 반 수

for i in range(k):
    print(f"Class {i+1}")
    n = list(map(int, input().split()))  # 수학 점수
    n1 = n[:1]
    n2 = n[1:]
    n2 = sorted(n2, reverse=False)
    s = 0
    for j in range(len(n2)):
        if n2[j] - n2[j - 1] > s:
            s = n2[j] - n2[j - 1]
    print(f"Max {max(n2)}, Min {min(n2)}, Largest gap {s}")