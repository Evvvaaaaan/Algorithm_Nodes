import sys 
input = sys.stdin.readline
num = int(input())

sequence = list(map(int,input().split()))

dp = sequence[:]

for i in range(num):
    for j in range(i):
        if sequence[j] > sequence[i]:
            dp[i] = max(dp[i], dp[j]+ sequence[i])
        
        

print(max(dp))