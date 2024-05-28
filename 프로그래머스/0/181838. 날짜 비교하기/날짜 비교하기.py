def solution(date1, date2):
    answer = 0
    n_date1 = ''
    n_date2 = ''
    
    for i in date1:
        n_date1+=str(i)
    for i in date2:
        n_date2+=str(i)
    n_date1 = int(n_date1)
    n_date2 = int(n_date2)
    if n_date1 < n_date2:
        answer = 1
    return answer