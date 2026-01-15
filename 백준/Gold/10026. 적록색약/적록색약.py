import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


colors = [list(input().strip()) for _ in range(n)]


def bfs(x,y,visited, current_colors):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = True
    color = current_colors[x][y]

    while queue:
        cx, cy = queue.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and current_colors[nx][ny] == color:
                    queue.append((nx, ny))
                    visited[nx][ny] = True

                

visited_n = [[False] * n for _ in range(n)]
count_n = 0

for i in range(n):
    for j in range(n):
        if not visited_n[i][j]:
            bfs(i, j, visited_n, colors)
            count_n += 1
for i in range(n):
    for j in range(n):
        if colors[i][j] == 'G':
            colors[i][j] = 'R'

visited_d = [[False] * n for _ in range(n)]
count_d = 0

for i in range(n):
    for j in range(n):
        if not visited_d[i][j]:
            bfs(i,j,visited_d,colors)
            count_d += 1


print(count_n, count_d)