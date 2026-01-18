def solution(n, lost, reserve):
    lost_set = set(lost)
    reserve_set = set(reserve)
    
    common = lost_set & reserve_set
    lost_set -= common 
    reserve_set -= common

    
    for i in sorted(lost_set):
        if i - 1 in reserve_set:
            reserve_set.remove(i - 1)
        elif i + 1 in reserve_set:
            reserve_set.remove(i + 1)
        else:
            n -= 1
    return n