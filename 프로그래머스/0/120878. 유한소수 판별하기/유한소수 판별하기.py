import math

def solution(a, b):
    answer = 0
    gcd = math.gcd(a, b)
    b = b//gcd
    for i in [2, 5]:
        while not b % i:
            b //= i
    answer = 1 if b == 1 else 2
    return answer