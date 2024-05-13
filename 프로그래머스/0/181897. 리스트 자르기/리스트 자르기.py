def solution(n, slicer, num_list):
    answer = []
    if n ==1:
        for i in num_list[:slicer[1]+1]:
            answer.append(i)           
    elif n==2:
        for i in num_list[slicer[0]:]:
            answer.append(i)
    elif n==3:
        for i in num_list[slicer[0]:slicer[1]+1]:
            answer.append(i)
    elif n==4:
        for i in num_list[slicer[0]:slicer[1]+1:slicer[2]]:
            answer.append(i)
    return answer