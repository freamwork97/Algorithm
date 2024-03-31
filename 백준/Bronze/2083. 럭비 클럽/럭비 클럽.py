while True:
    m, a, w = input().split()
    a = int(a)
    w = int(w)
    if m == "#" and a == 0 and w == 0:
        break
    if a > 17 or w >= 80:
        print(f"{m} Senior")
    else:
        print(f"{m} Junior")