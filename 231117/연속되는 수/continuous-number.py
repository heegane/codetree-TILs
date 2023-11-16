n = int(input())
arr = []
for _ in range(n):
    arr.append(input())
ks = []
for a in arr:
    if a not in ks:
        ks.append(a)

result = []
for k in ks:
    temp = list(''.join(arr).replace(k, ''))
    cnt = 0
    for i in range(len(temp) - 1):
        if temp[i] == temp[i + 1]:
            cnt += 1
        else:
            result.append(cnt + 1)
            cnt = 0
    result.append(cnt)
print(max(result))