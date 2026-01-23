import sys
input = sys.stdin.readline

n = int(input())
weight = [int(input()) for _ in range(n)]
energy = 0


sorted_weight = sorted(weight)

index_map = {val: i for i, val in enumerate(sorted_weight)}
visited = [False] * n
global_min = min(weight)


for i in range(n):
    if visited[i] or index_map[weight[i]] == i:
        continue  

    cycle_sum = 0
    cycle_min = float('inf')
    j = i
    cycle_len = 0

    while not visited[j]:
        visited[j] = True
        val = weight[j]
        cycle_sum += val
        cycle_min = min(cycle_min, val)
        j = index_map[val]
        cycle_len += 1

    cost1 = cycle_sum + cycle_min * (cycle_len - 2)
    cost2 = cycle_sum + cycle_min + global_min * (cycle_len + 1)
    energy += min(cost1, cost2)

print(energy)
