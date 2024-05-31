def solution(order):
    answer = 0
    for i in str(order):
        i = int(i)
        if i == 3 or i == 6 or i ==9:
            answer+=1
    return answer