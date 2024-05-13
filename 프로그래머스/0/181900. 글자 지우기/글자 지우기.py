def solution(my_string, indices):
    
    answer = ''
    s = list(my_string)
    indices.sort()
    indices.reverse()
    
    for i in indices:
        del s[i]
        if i == indices[-1]:
            for j in s:
                answer+=j
    
    return answer