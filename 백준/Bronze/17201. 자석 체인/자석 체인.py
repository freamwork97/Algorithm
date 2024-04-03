n = int(input())  # 한쌍의 자석 수

chain = input()
print("Yes" if chain == chain[:2] * n else "No")