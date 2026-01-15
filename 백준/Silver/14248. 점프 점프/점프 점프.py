import sys
from collections import deque

num = int(sys.stdin.readline().strip())
stones = list(map(int, sys.stdin.readline().strip().split()))
start = int(sys.stdin.readline())

visited = [False] * num
count = 1

queue = deque()
queue.append(start-1)

while queue:
    current = queue.popleft()
    visited[current] = True

    jump = stones[current]
    for next_pos in [current+jump, current-jump]:
        if 0 <= next_pos < num:
            if not visited[next_pos]:
                visited[next_pos] = True
                count += 1
                queue.append(next_pos)

print(count)