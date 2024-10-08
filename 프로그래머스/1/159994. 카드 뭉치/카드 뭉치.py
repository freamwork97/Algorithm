def solution(cards1, cards2, goal):
    i, j, k = 0, 0, 0
    while i < len(cards1) and j < len(cards2) and k < len(goal):
        if goal[k] == cards1[i]:
            i += 1
        elif goal[k] == cards2[j]:
            j += 1
        else:
            return "No"
        k += 1
    while i < len(cards1) and k < len(goal):
        if goal[k] == cards1[i]:
            i += 1
        else:
            return "No"
        k += 1
    while j < len(cards2) and k < len(goal):
        if goal[k] == cards2[j]:
            j += 1
        else:
            return "No"
        k += 1
    return "Yes" if k == len(goal) else "No"
