num = int(input())

dp = [100001] * (num+1)

dp[0] = 0

coins = [1,2,5,7]

for i in range(1, num+1):
    for coin in coins:
        if i >= coin:
            dp[i] = min(dp[i], dp[i-coin]+1)

print(dp[num])