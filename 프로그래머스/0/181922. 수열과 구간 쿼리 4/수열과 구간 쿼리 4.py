def solution(arr, queries):
    for i in queries:
        for j in range(i[0], i[1]+1):
            arr[j] += 1 if j % i[2] == 0 else 0
    return arr