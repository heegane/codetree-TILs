n = int(input())
hi = []
for _ in range(n):
    hi.append(int(input()))

result = []
answer = []
for i in range(1, max(hi)):
    temp = hi
    cnt = 0
    for j in range(len(temp)):
        if temp[j] <= i:
            temp[j] = 0
        else:
            temp[j] = temp[j] - i
    for j in range(len(temp)):
        if temp[j] != 0:
            cnt = 1
        else:
            result.append(cnt)
            cnt = 0
    result.append(cnt)
    answer.append(result.count(1))

print(max(answer))