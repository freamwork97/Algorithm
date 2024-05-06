def solution(ineq, eq, n, m):
    answer = 0
    if ineq == ">":
        answer = 1 if (n >= m if eq == "=" else n > m) else 0
    else:
        answer = 1 if (n <= m if eq == "=" else n < m) else 0
    return answer