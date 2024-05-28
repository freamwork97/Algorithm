def solution(rank, attendance):
    answer = 0
    a_rank = []
    for i in range(len(rank)):
        if attendance[i]:
            a_rank.append([rank[i],i])
    a_rank = sorted(a_rank)
    answer = 10000 * a_rank[0][1] + 100 * a_rank[1][1] + a_rank[2][1]
    return answer