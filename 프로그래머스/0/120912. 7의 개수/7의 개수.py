def solution(array):
    answer = 0
    
    for i in array:
        if '7' in str(i):
            for j in range(len(str(i))):
                if '7' == str(i)[j]:
                    answer+=1
    return answer