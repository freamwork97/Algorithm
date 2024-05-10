def solution(n):
    answer = [n]
    while True:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        answer.append(n)
        if n == 1:
            break
    return answer