def solution(keyinput, board):
    answer = [0]*2
    for i in keyinput:
        if i == 'left':
            answer[0] -=1
        if i == 'right':
            answer[0] +=1
        if i == 'up':
            answer[1] +=1
        if i == 'down':
            answer[1] -=1
        if answer[0] >board[0] // 2:
            answer[0] = board[0] // 2
        if answer[0] < -(board[0] // 2):
            answer[0] = -(board[0] // 2)
        if answer[1] > board[1] // 2:
            answer[1] = board[1] // 2
        if answer[1] < -(board[1] // 2):
            answer[1] = -(board[1] // 2)
    
    return answer