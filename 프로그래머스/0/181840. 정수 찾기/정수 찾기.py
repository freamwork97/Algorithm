def solution(num_list, n):
    for i in num_list:
        if str(n) == str(i):
            return 1
    return 0