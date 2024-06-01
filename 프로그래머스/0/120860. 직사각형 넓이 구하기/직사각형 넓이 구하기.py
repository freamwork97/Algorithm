def solution(dots):
    answer = 0
    dots.sort()
    d1,d2,d3,d4 = dots[0],dots[1],dots[2],dots[3]
    x = abs(d1[0] - d3[0])
    y = abs(d1[1] - d4[1])
    if y == 0:
        y = x
    
    answer = x*y
    return answer