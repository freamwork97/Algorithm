n = int(input())
m = list(input())
c = sum(1 for i in m if i == "L")
print(n) if c == 0 else print(n - int((c / 2 - 1)))
