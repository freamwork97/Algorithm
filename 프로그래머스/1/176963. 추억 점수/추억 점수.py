def solution(name, yearning, photo):
    answer = []
    
    for i in photo:
        r = 0
        for j in i:
            for k in range(len(name)):
                if j == name[k]:
                    r+=yearning[k]
        answer.append(r)
    return answer