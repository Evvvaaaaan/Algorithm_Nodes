from collections import deque
n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)]  
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    graph[i].sort()
    
visited = [False] * (n+1)
visited_bfs = [False] * (n+1)
def dfs(v):
    visited[v] = True
    print(v, end=' ')
    for next_v in graph[v]:
        if not visited[next_v]:
            dfs(next_v)
def bfs(v):
    queue = deque([v])
    visited_bfs[v] = True
    while queue:
        current = queue.popleft()
        print(current, end=' ')
        for next_v in graph[current]:
            if not visited_bfs[next_v]:
                visited_bfs[next_v] = True
                queue.append(next_v)

dfs(v)
print(end='\n')
bfs(v)




