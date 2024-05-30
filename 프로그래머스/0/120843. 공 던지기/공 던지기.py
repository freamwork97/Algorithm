def solution(numbers, k):
    length = len(numbers)
    return numbers[(k * 2) % length - 2]
