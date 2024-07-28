aeiou = ['a', 'A', 'e', 'E', 'i',
         'I', 'o', 'O', 'u', 'U']
while True:
    s = input()
    chk = 0
    if s == '#':
        break
    for i in s:
        if i in aeiou:
            chk += 1
    print(chk)