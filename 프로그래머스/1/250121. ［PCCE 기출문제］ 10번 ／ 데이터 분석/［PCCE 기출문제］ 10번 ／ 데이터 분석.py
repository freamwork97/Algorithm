def solution(data, ext, val_ext, sort_by):
    d = {'code':0,'date':1,'maximum':2,'remain':3}
    e_index = d[ext]
    s_index = d[sort_by]
    result = [i for i in data if i[e_index] < val_ext]
    result = sorted(result, key=lambda i: i[s_index])
    return result