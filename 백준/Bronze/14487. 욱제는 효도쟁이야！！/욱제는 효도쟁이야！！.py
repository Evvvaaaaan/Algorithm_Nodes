import sys
input = sys.stdin.readline

num = int(input())
prices = list(map(int, input().split()))

prices.sort()

sum_p = 0
for i in range(num - 1):
    sum_p += prices[i]

print(sum_p)