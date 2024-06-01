def solution(chicken):
    coupon = 10
    answer = 0

    while chicken >= coupon:
        answer += chicken // coupon  
        chicken = (chicken % coupon) + (chicken // coupon)  

    return answer
