def solution(numbers):
    answer = 0
    num_list = [i for i in range(10)]
    
    for i in num_list:
        if i not in numbers:
            answer+=i
    return answer