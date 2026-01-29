import sys
input = sys.stdin.readline

num = int(input())

first = []
last = []
cnt = 0

for _ in range(num):
    first.append(input().strip())

for _ in range(num):
    last.append(input().strip())

for i in range(num - 1):
    for j in range(i + 1, num):
        if first.index(last[j]) < first.index(last[i]):
            cnt += 1
            break

print(cnt)