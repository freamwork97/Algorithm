def solution(code):
    answer = ''
    mode = 0
    for i in range(len(code)):
        if code[i] == '1':
            if mode == 0:
                mode = 1
                continue
            else:
                mode = 0
                continue
        if mode == 0:
            if i % 2 ==0:
                answer += code[i]
        else:
            if i % 2 ==1:
                answer += code[i]
    if answer == '':
        answer = "EMPTY"
    return answer