v = "aeiouy"

while True:
    s = input()
    if s == 'quit!':
        break
    if len(s) >= 4 and s[-2:] == 'or':
        if s[-3] not in v:
            print(s[:-1] + 'ur')
        else:
            print(s)
    else:
        print(s)