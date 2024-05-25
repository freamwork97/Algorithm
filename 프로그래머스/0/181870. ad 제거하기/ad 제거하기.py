def solution(strArr):
    try:
        strArr = [i for i in strArr if 'ad' not in i]
        print(strArr)  
        return strArr
    except:
        return strArr