import sys
from collections import deque

sys.setrecursionlimit(10**6)

dx = [1, -1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, 1, -1, 1, -1, 1, -1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    graph[x][y] = 0

    while queue:
        cx,cy = queue.popleft()

        for i in range(8):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < h and 0 <= ny < w:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    queue.append((nx, ny))



while True:
    w, h = map(int, sys.stdin.readline().split())

    if w == 0 and h == 0:
        break

    graph = []
    for _ in range(h):
        graph.append(list(map(int, sys.stdin.readline().split())))


    island_count = 0

    for i in range(h):
        for z in range(w):
            if graph[i][z] == 1:
                island_count += 1
                bfs(i,z)

    print(island_count)