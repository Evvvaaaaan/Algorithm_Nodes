def solution(s):
    answer = True
    s = s.upper()
    pCount = 0
    yCount = 0
    for i in s:
        if i == 'P':
            pCount += 1
        elif i == 'Y':
            yCount += 1
    if(pCount == yCount):
        answer = True
    else:
        answer = False
    return answer