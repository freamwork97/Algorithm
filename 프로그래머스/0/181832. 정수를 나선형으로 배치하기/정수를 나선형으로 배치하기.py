def solution(n):
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]  
    x, y, c = 0, -1, 1
    answer = [[0] * n for _ in range(n)]
    for k in range(2 * n - 1):
        for _ in range((2 * n - k) // 2):
            x += dx[k % 4]
            y += dy[k % 4]
            answer[x][y] = c
            c += 1
    return answer
