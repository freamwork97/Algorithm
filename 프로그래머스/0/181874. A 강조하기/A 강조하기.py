def solution(myString):
    answer = ''
    for i in myString:
        i=i.lower()
        if i == 'a':
            i=i.upper()
        answer+=i
    return answer