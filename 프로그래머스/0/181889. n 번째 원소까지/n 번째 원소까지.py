def solution(num_list, n):
    answer = []
    for i in range(len(num_list)):
        if n > i:
            answer.append(num_list[i])
    return answer