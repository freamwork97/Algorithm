x = int(input())
s = 0
for _ in range(int(input())):
    a, b = map(int, input().split())
    s = s + a * b

print("Yes") if s == x else print("No")

# if s == x:
#     print("Yes")
# else:
#     print("No")