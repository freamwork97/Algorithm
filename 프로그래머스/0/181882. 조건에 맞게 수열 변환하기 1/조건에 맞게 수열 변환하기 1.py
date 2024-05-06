def solution(arr):
    answer = []
    for i in arr:
      (answer.append(i//2) if i % 2 ==0 else answer.append(i)) if i >= 50 else (answer.append(i*2) if i % 2 ==1 else answer.append(i))
            
    return answer