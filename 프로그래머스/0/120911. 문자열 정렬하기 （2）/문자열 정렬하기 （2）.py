def solution(my_string):
    answer = ''
    my_string = my_string.lower()
    for i in sorted(my_string):
        answer+=i
    return answer