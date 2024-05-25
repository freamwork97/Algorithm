def solution(myString, pat):
    trans = str.maketrans('AB', 'BA')
    new_string = myString.translate(trans)
    if pat in new_string:
        return 1
    else:
        return 0
