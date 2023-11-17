n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
result = []

for k in range(1, n + 1):
    for i in range(n - k + 1):
        for j in range(n - k + 1):
            sum_value = 0
            for x in range(k):
                for y in range(k):
                    sum_value += arr[i + x][j + y]
            result.append(sum_value)
print(max(result))