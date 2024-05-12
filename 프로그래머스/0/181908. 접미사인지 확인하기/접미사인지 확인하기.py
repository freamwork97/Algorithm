def solution(my_string, is_suffix):
    answer = 0
    l = [my_string[i:] for i in range(len(my_string))]
    for i in l:
        answer += 1 if i == is_suffix else 0
        
    return answer