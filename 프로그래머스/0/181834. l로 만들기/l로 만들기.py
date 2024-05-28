import re
def solution(myString):
    answer = re.sub('[a-k]','l', myString)
    return answer