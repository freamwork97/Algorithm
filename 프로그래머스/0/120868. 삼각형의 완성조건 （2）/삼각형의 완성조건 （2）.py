def solution(sides):
    chk = 0
    for _ in range(max(sides)-min(sides)+1,max(sides)+1):
        chk+=1
    chk+=sum(sides)-max(sides)-1
    return chk