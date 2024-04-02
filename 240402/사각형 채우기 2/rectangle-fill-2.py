n = int(input())

dp = [1, 3, 5]

if n <= 3:
    print(dp[n - 1] % 10007)
else:
    for i in range(3, n + 1):
        dp.append(2 * dp[i - 2] + dp[i - 1])
    print(dp[n - 1] % 10007)