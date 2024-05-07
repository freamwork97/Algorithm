def solution(sides):
    answer = 2 if max(sides) >= sum(sides)-max(sides) else 1
    return answer