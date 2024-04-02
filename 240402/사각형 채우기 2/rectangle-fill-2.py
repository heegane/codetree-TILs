n = int(input())

dp = [1,3,5]

if n <= 3:
    print(dp[n-1]%10007)
else:
    for i in range(3,n+1):
        if i%2 == 0:
            dp.append(dp[i-2]*dp[i-2]+dp[i-1])
        else:
            dp.append(2*dp[i-1]-1)
    print(dp[n-1]%10007)