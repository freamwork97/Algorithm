def solution(q, r, code):
    answer = ''
    for i in range(len(code)):
        new_r = i % q
        if new_r == r:
            answer+=code[i]
    return answer