def solution(arr):
    row_count = len(arr)
    column_count = len(arr[0])
    if row_count > column_count:
        for i in range(row_count):
            arr[i] += [0] * (row_count - column_count)
    elif column_count > row_count:
        for _ in range(column_count - row_count):
            arr.append([0] * column_count)

    return arr




