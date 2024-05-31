import math
def solution(n):
    factors=[]
    i=2
    while i<=n:
        if n%i==0:
            factors.append(i)
            n=n/i
        else:
            i=i+1
    factors = list(set(factors))
    factors = sorted(factors)
    return factors