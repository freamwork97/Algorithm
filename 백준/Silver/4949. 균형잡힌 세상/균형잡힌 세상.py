while True:
    s = input()
    chk = ''
    if s == '.':
        break
    else:
        for i in s:
            if i == '(' or i == ')' or i == '[' or i == ']':
                chk += i
    if len(chk) != 0:
        for _ in range(len(chk)):
            chk = chk.replace('[]', '')
            chk = chk.replace('()', '')
    if len(chk) == 0:
        print('yes')
    else:
        print('no')