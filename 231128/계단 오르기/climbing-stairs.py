n = int(input())
dp = [0] * (n + 1)

for i in range(1, n + 1):
    if i == 0 or i == 1:
        dp[i] = 0
    elif i == 2 or i == 3:
        dp[i] = 1
    else:
        dp[i] = dp[i - 2] + dp[i - 3]

print(dp[n] % 10007)