from collections import deque
import sys
input = sys.stdin.readline

graph = [list(input().split()) for _ in range(5)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]

result = set()

def dfs(x,y,depth, number_string):
    if depth == 6:
        result.add(number_string)
        return 
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if 0 <= nx < 5 and 0 <= ny < 5:
            dfs(nx,ny, depth + 1, number_string + graph[nx][ny])


for i in range(5):
    for j in range(5):
        dfs(i,j,1,graph[i][j])

print(len(result))