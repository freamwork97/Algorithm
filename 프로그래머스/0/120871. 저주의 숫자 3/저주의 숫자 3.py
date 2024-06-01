def solution(n):
    answer = 0
    cnt = 0
    while cnt < n:    
        if ('3' in str(answer)) or (answer % 3 == 0):
            answer += 1
        else:
            cnt += 1
            answer += 1
    answer -=1
    return answer 