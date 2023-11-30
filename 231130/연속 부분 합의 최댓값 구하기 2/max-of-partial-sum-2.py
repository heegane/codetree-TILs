n = int(input())
result = []
arr = list(map(int,input().split()))

cnt = 0
for i in range(n):
    cnt += arr[i]
    if cnt < 0:
        result.append(cnt)
        cnt = arr[i]

result.append(cnt)
print(max(result))