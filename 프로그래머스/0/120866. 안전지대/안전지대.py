def check(mine_field, x, y, n):
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            nx, ny = x + dx, y + dy
            if nx >= 0 and ny >= 0 and nx < n and ny < n:
                if mine_field[nx][ny] != 1:
                    mine_field[nx][ny] = -1

def solution(board):
    n = len(board)
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                check(board, i, j, n)
    return sum(x.count(0) for x in board)
