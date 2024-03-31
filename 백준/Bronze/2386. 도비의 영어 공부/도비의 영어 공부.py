while True:
    w = input()
    if w == "#":
        break
    s = w[0]
    c = w[2:].lower()
    print(s, c.count(s))