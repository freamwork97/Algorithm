def solution(my_string, s, e):
    answer = my_string[:s]
    for i in reversed(my_string[s:e+1]):
        answer+=i
    answer+=my_string[e+1:]
    return answer