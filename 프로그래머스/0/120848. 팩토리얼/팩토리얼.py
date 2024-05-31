def solution(n):
    answer = 0
    f = 1
    while f <= n:
        answer += 1
        f *= answer
    return answer-1
