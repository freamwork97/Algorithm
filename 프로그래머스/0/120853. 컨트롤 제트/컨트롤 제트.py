def solution(s):
    answer = 0
    s = list(s.split())
    for i in range(len(s)):
        try:
            answer += int(s[i])
        except:
            answer -= int(s[i-1])
    return answer