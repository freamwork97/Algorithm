def solution(money):
    return [money // (sum(list(range(1,101)))+450), money % (sum(list(range(1,101)))+450)]