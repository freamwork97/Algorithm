from collections import Counter
def solution(array):
    answer = 0 
    cnt = Counter(array).most_common(2)
    if len(array)>1:
        try:
            if cnt[0][1] == cnt[1][1]: 
                answer = -1 
            else: 
                answer = cnt[0][0]
        except IndexError:
            answer = cnt[0][0]
    else:
        answer = cnt[0][0]      
    return answer