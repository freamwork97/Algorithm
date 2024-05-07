def solution(array, n):
    answer = 0
    for i in array:
        answer += 1 if n == i else 0
    return answer