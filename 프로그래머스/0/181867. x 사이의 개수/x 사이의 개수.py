def solution(myString):
    n=list(map(str,myString.split('x')))
    answer = [len(i) for i in n]
    return answer