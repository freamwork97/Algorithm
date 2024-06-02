def solution(polynomial):
    p = list(map(str, polynomial.split(' + ')))
    s = []
    n = []
    for i in p:
        if 'x' in i:
            s.append(i)
        else:
            n.append(int(i))
    if len(s) == 0 :
        n_n =n.copy()
        n = 0
        for i in n_n:
            n += int(i)
        return str(n)
    n_s = []
    for i in s:
        if i == 'x':
            n_s.append(1)
        else:
            n_s.append(int(i[:-1]))
    str_s = str(sum(n_s))+'x'
    try:
        if str_s == '1x' and len(n) != 0:
            return f'x + {sum(n)}'
        elif str_s == '1x' and len(n) == 0:
            return 'x'
        else:
            if len(n) == 0:
                return f'{str_s}'
            else:
                return f'{str_s} + {sum(n)}'
    
    except:
        return f'{str_s}'