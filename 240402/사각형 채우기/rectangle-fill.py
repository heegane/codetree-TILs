import sys

input = sys.stdin.readline

n = int(input())

dp = [1, 2, 3, 5]

if n <= 4:
    print(dp[n-1]%10007)
else:
    for i in range(4,n-4):
        dp.append(dp[i-2]+dp[i-1])
    print(dp[n-1]%10007)