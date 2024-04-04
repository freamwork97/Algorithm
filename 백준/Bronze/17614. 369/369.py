c = 0
n = int(input())

for i in range(1, n + 1):
    c += str(i).count("3") + str(i).count("6") + str(i).count("9")

print(c)