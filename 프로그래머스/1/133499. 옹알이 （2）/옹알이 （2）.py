def solution(babbling):
    answer = 0
    w = ['aya','ye','woo','ma']
    for i in babbling:
        l_w = ''
        while len(i) > 0:
            for j in w:
                if i.startswith(j) and l_w != j:
                    i = i[len(j):]
                    l_w = j
                    break
            else:
                break  
        else:
            answer += 1 
    return answer

