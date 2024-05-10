def solution(a, b, c, d):
    answer = 0
    l = [a, b, c, d]
    l2 = list(set(l))
    if len(l2) == 1:
        answer = 1111 * l2[0]
    elif len(l2) == 2:
        for i in l:
            if l.count(i) == 3:
                p = i
                q = [x for x in l2 if x != p][0]
                answer= (10*p+q)**2
            elif l.count(i) == 2:
                p = i
                q = [x for x in l2 if x != p][0]
                answer= (p + q)*(abs(p-q))
    elif len(l2) == 3:
        for i in l:
            if l.count(i) == 2:
                l3 = [x for x in l2 if x != i]
                answer = l3[0]*l3[1]
    else:  
        answer = min(l)
    return answer