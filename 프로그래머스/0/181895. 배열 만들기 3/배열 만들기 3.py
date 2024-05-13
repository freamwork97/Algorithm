def solution(arr, intervals):
    answer = []
    for (x,y) in intervals:
        for j in arr[x:y+1]:
            answer.append(j)
    return answer