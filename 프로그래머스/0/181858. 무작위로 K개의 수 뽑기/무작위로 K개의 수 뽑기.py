def solution(arr, k):
    answer = []
    new_arr = []
    for i in arr:
        if i not in new_arr:
            new_arr.append(i)
            
    for i in range(k):
        try:
            answer.append(new_arr[i])
        except:
            answer.append(-1)
    return answer