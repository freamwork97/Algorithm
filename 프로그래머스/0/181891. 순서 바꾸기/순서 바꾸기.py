def solution(num_list, n):
    answer = []
    l = []
    n=n-1
    for i in range(len(num_list)):
        if i <=n:
            l.append(num_list[i])
    for i in range(len(num_list)):
        if i >n:
            answer.append(num_list[i])
    answer.extend(l)
    return answer