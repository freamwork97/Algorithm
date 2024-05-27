import math


def solution(arr):
    length = len(arr)
    next_pow_of_2 = 2 ** math.ceil(math.log2(length))

    return arr + [0] * (next_pow_of_2 - length)
