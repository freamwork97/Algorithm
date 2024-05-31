def solution(n):
    answer = 0
    for i in range(n+1):
        check = 0
        for j in range(1,i+1):
            check +=1 if i % j == 0 else 0
        if check >=3:
            answer +=1
    return answer