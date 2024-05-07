def solution(box, n):
    answer = 0
    for i in range(len(box)):
        if i == 0:
            answer += int(box[i]/n)
        else:
            answer *= int(box[i]/n)
    return answer