import sys
from collections import deque
input = sys.stdin.readline


n = int(input())

graph = [[] for _ in range(n+1)]
parent = [0] * (n+1)


for _ in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs():
    queue = deque([1])

    visited = [False] * (n+1)
    visited[1] = True

    while queue:
        # now = 1
        now = queue.popleft()

        for child in graph[now]:
            if not visited[child]:
                # 1st child / 6, 4
                # 4
                visited[child] = True
                # parent of 6 is 1
                # 4 = 1
                parent[child] = now
                # queue = 6,4
                queue.append(child)
        

bfs()

# parent[] each parent 

for i in range(2, n+1):
    print(parent[i])
