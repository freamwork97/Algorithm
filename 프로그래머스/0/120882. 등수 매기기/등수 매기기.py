def solution(score):
    for i in range(len(score)):
        score[i] = sum(score[i])
    sorted_score = sorted(score, reverse = True)
    answer = [sorted_score.index(s) + 1 for s in score] 
    return answer