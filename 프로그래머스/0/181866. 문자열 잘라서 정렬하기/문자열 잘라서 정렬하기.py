def solution(myString):
    answer=list(map(str,myString.split('x')))
    answer=' '.join(answer).split()
    answer.sort()
    return answer