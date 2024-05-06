def solution(a, b):
    answer = 0
    a = str(a)
    b = str(b)
    c1 = a+b
    c2 = b+a
    if int(c1) > int(c2):
        answer = int(c1)
    else:
        answer = int(c2)
    return answer