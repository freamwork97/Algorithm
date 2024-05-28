def solution(picture, k):
    answer = []
    for row in picture:
        answer_r = ''.join([ch * k for ch in row])
        for _ in range(k):
            answer.append(answer_r)
    return answer