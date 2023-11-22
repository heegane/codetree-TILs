n = int(input())
arr = list(map(int, input().split()))
result = []
sum_value = arr[0]
for i in range(1, n):
    if sum_value + arr[i] < 0:
        result.append(sum_value)
        sum_value = arr[i]
    else:
        sum_value += arr[i]
    result.append(sum_value)
print(max(result))