def solution(quiz):
    answer = []
    for i in quiz:
        a,b=map(str,(i.split('=')))
        r = eval(a)
        answer.append('O') if r == int(b) else answer.append('X')
    return answer