def solution(dots):
    answer = 0
    dot1,dot2,dot3,dot4 = dots
    if abs(dot1[1] - dot2[1])/abs(dot1[0] - dot2[0]) == abs(dot3[1] - dot4[1])/abs(dot3[0] - dot4[0]):
        answer=1
    if abs(dot2[1] - dot3[1])/abs(dot2[0] - dot3[0]) == abs(dot1[1] - dot4[1])/abs(dot1[0] - dot4[0]):
        answer=1
    if abs(dot1[1] - dot3[1])/abs(dot1[0] - dot3[0]) == abs(dot2[1] - dot4[1])/abs(dot2[0] - dot4[0]):
        answer=1
    if abs(dot1[1] - dot4[1])/abs(dot1[0] - dot4[0]) == abs(dot2[1] - dot3[1])/abs(dot2[0] - dot3[0]):
        answer=1
    return answer