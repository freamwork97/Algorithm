import math
def solution(numer1, denom1, numer2, denom2):
    return (numer1*denom2 + numer2*denom1)/math.gcd(numer1*denom2 + numer2*denom1,denom1*denom2),denom1*denom2/math.gcd(numer1*denom2 + numer2*denom1,denom1*denom2)