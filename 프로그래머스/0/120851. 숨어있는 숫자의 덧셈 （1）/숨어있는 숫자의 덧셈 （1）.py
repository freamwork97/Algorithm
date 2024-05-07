import re
def solution(my_string):
    answer = 0
    new=re.sub(r'[a-zA-Z]','',my_string)
    for i in new:
        answer += int(i)
    return answer