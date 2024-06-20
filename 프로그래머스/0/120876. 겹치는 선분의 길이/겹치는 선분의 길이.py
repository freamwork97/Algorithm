def solution(lines):
    endpoints = sorted([point for line in lines for point in line])
    overlaps = 0

    for i in range(len(endpoints) - 1):
        starts = sum(line[0] <= endpoints[i] < line[1] for line in lines)
        ends = sum(line[0] < endpoints[i + 1] <= line[1] for line in lines)
        if starts > 1 or ends > 1:
            overlaps += endpoints[i + 1] - endpoints[i]

    return overlaps
