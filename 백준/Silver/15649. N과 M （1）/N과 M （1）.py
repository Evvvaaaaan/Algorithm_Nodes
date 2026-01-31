import sys
input  = sys.stdin.readline

N, M = map(int, input().split())

s = []
visited = [False] * (N + 1)

def dfs():
    if len(s) == M:
        print(' '.join(map(str, s)))
        return
    
    for i in range(1, N + 1):
        if not visited[i]:
            visited[i] = True
            s.append(i)

            dfs()

            s.pop()
            visited[i] = False

dfs()