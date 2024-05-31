def solution(bin1, bin2):
    answer = ''
    t=int(bin1, 2)+int(bin2,2)
    answer=bin(t)[2:]
    return answer