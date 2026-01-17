import sys

input = sys.stdin.readline
num = int(input())
complete_date = list(map(int,input().split()))
complete_date.sort(reverse=True)

lists = [0] * num

for i in range(num):
    lists[i] = (i+1) + complete_date[i]

print(max(lists) + 1)