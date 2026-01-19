import sys
input = sys.stdin.readline
num = int(input())

lists = [0] * num
buttons = list(map(int,input().split()))
cnt  = 0
for i in range(num):
    if lists[i] != buttons[i]:
        lists[i] = 1 - lists[i]
        if i + 1 < num:
            lists[i+1] = 1 - lists[i+1]
        if i + 2 < num:
            lists[i+2] = 1 - lists[i+2]
        cnt += 1

print(cnt)