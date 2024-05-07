def solution(arr, queries):
    answer = []
    for i,j,k in queries:
        t = []
        for a in arr[i:j+1]:
            if a > k:
                t.append(a)
        try:
            answer.append(min(t))
        except:
            answer.append(-1)
    return answer