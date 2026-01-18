import sys
input = sys.stdin.readline

n, k = map(int,input().split())
cnt = 0
values = []
for _ in range(n):
    values.append(int(input()))

values.sort(reverse=True)

for i in values:
    if i <= k:
        cnt += k // i
        k %= i

print(cnt)