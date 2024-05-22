def solution(arr):
    copy_arr = arr.copy()
    cnt = 0

    while True:
        arr = [i * 2 + 1 if i % 2 == 1 and i < 50 else i / 2 if i % 2 == 0 and i >= 50 else i for i in arr]

        if arr == copy_arr:
            return cnt

        copy_arr = arr.copy()
        cnt += 1
