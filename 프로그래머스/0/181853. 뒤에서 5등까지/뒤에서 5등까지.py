def solution(num_list):
    answer = []
    num_list=sorted(num_list)
    for i in num_list[:5]:
        answer.append(i)
    return answer