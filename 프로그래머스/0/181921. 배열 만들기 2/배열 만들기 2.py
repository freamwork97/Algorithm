import re

def solution(l, r):
    pattern = r'^[^12346789]+$'
    answer = [-1] if not any(re.match(pattern, str(i)) for i in range(l, r+1)) else [i for i in range(l, r+1) if re.match(pattern, str(i))]

    return answer

