def solution(n):
    answer = []
    for i in range(n):
        arr = []
        for j in range(n):
            arr.append(1) if i == j else arr.append(0)
        answer.append(arr)
    return answer