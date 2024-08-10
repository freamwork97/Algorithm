n, m = map(int, input().split())
if n >= m:
    if m == 1 or m == 2:
        print('NEWBIE!')
    else:
        print('OLDBIE!')
else:
    print('TLE!')