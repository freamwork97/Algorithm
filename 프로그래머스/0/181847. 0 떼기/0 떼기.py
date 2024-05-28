def solution(n_str):
    answer = ''
    for i in n_str:
        answer+=i
    print(answer[0])
    if answer[0] == '0':
        while answer[0]=='0':
            answer = answer[1:]
    return answer