def solution(hp):
    b = 5
    m = 3
    s = 1
    return (hp // b) + ((hp % b) // m) + (((hp % b) % m) // s)