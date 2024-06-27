def solution(players, callings):
    p = {player: i for i, player in enumerate(players)}
    
    for i in callings:
        idx = p[i]
        players[idx], players[idx - 1] = players[idx - 1], players[idx]
        p[players[idx]] = idx
        p[players[idx-1]] = idx-1
        
    return players

