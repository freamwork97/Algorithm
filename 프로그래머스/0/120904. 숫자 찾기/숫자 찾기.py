def solution(num, k):
    answer = 0
    s_num = str(num)
    for i in range(len(s_num)):
        if s_num[i] == str(k):
            answer = i+1
            break
        else:
            answer =-1
    return answer