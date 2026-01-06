def solution(s):
    answer = True
    sLen = len(s)
    
    if sLen not in (4,6):
        answer = False
    else:
        if s.isdigit():
            answer = True
        else: answer = False
    
    return answer