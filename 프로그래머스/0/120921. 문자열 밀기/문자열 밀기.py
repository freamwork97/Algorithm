def solution(A, B):
    answer = 0
    if A==B:
        return answer
    else:     
        for i in range(1,len(A)):
            A = A[-1]+A[0:-1]
            if A == B:
                answer = i
                return answer
            
        answer = -1
        return answer