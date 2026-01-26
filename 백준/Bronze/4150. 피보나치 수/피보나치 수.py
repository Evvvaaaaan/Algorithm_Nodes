num = int(input())

def fib(v):
    if v <= 1:
        return v
    dp = [0] * (v + 1)
    dp[1] = 1

    for i in range(2, v+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[v]
print(fib(num))