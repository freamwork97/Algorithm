n = int(input())

for _ in range(n):
    p = input()
    if p == "P=NP":
        print("skipped")
    else:
        n1, n2 = p.split("+")
        n1 = int(n1)
        n2 = int(n2)
        print(n1 + n2)
