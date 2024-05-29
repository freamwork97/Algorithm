def solution(numbers):
    # for i in range(len(numbers)):
        # numbers[i] = abs(numbers[i])
    numbers = sorted(numbers, reverse=True)
    answer = numbers[0]*numbers[1]
    if numbers[-1]*numbers[-2] > answer:
        answer = numbers[-1]*numbers[-2]
    return answer