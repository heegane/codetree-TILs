n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))
coins.sort(reverse=True)
cnt = 0
for coin in coins:
    if k < coin:
        continue
    else:
        cnt += k // coin
        k = k % coin
print(cnt)