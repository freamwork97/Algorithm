import re

def solution(babbling):
    answer = 0
    for i in babbling:
        answer+=1 if re.match(r"(aya|ye|woo|ma)+$", i) else 0
    return answer