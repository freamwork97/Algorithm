def solution(array):
    answer = []
    for i in range(len(array)):
        if max(array) == array[i]:
            answer.append(max(array))
            answer.append(i)
    return answer