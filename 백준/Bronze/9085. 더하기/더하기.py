import sys
input = sys.stdin.readline

num = int(input())

for _ in range(num):
    a = int(input())
    nums = list(map(int, input().split()))
    print(sum(nums))