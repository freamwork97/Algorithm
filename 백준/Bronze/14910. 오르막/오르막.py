n = list(map(int, input().split()))

print("Good") if n == sorted(n) else print("Bad")