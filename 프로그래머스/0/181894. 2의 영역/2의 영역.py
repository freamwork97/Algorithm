def solution(arr):
    answer = []
    if 2 not in arr:
        answer.append(-1)
    else:
        l=[]
        for i in range(len(arr)):
            if arr[i] == 2:
                l.append(i)
        for i in arr[l[0]:l[-1]+1]:
            answer.append(i)
    return answer