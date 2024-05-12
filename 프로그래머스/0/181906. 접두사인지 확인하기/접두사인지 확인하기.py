def solution(my_string, is_prefix):
    answer = 0
    l = [my_string[:i] for i in range(len(my_string))]
    for i in l:
        answer += 1 if i == is_prefix else 0
    return answer