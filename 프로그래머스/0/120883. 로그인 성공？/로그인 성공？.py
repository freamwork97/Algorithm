def solution(id_pw, db):
    answer = ''
    # if id_pw in db:
    #     answer+='login'
    for i in db:
        if id_pw[0] == i[0]:
            if id_pw[1] == i[1]:
                answer+='login'
                return answer
            elif id_pw[1] != i[1]:
                answer+='wrong pw'
                return answer
    if answer == '':
        answer+='fail'
    return answer