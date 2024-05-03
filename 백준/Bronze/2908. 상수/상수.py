a, b = map(str, input().split())

ra = a[::-1]
rb = b[::-1]
ra = int(ra)
rb = int(rb)

if ra > rb:
    print(ra)
else:
    print(rb)
