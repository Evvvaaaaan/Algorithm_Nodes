num = int(input())
net = int(input())

graph = [[]for _ in range(num+1)]

for i in range(net):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (num+1)

def dfs(v):
    visited[v] = True
    for next_v in graph[v]:
        if not visited[next_v]:
            dfs(next_v)

dfs(1)
print(visited.count(True)-1)