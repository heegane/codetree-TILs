n = int(input())
result = []
arr = list(map(int,input().split()))

cnt = 0
for i in range(n):
    if cnt + arr[i] < 0:
        result.append(cnt)
        cnt = arr[i]
    else:
        cnt += arr[i]
result.append(cnt)
print(max(result))