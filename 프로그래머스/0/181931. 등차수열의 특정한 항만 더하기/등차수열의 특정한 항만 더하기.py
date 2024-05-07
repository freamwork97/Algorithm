def solution(a, d, included):
    answer = 0
    for i in range(len(included)):
        num = a + (d * i)
        answer += num if included[i] == True else 0
            
    return answer