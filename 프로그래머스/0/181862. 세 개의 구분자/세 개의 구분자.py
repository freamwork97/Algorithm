def solution(myStr):
    myStr=myStr.replace('b','a').replace('c','a')
    answer = myStr.split('a')
    answer = [i for i in answer if i]
    if len(answer) == 0:
        answer.append('EMPTY')
    return answer