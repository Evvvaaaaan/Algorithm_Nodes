import sys
from collections import deque

limit_a, limit_b, limit_c = map(int, sys.stdin.readline().split())

queue = deque()
queue.append((0, 0))

visited = [[False] * (limit_b + 1) for _ in range(limit_a + 1)]
visited[0][0] = True

ans = []

# 물을 부었을 때, 두가지 경우로 나누기 
def pour(x, y , y_limit):
    # 남은 공간 계산
    space = y_limit - y
    # 만약 x가 남은 공간보다 많다면
    if x > space:
        return x - space, y_limit
    else:
        return 0, y + x
    

while queue:
    curr_a, curr_b = queue.popleft()
    curr_c = limit_c - curr_a - curr_b

    if curr_a == 0:
        ans.append(curr_c)

    water = [curr_a, curr_b, curr_c]
    moves = [(0,1,limit_b),(0,2,limit_c),(1,0,limit_a),(1,2,limit_c),(2,0,limit_a),(2,1,limit_b)]

    for start, end, limit in moves:
        next_start, next_end = pour(water[start], water[end], limit)

        next_water = list(water)
        next_water[start] = next_start
        next_water[end] = next_end

        next_a = next_water[0]
        next_b = next_water[1]

        if not visited[next_a][next_b]:
            visited[next_a][next_b] = True
            queue.append((next_a, next_b))


ans.sort()
print(*ans)