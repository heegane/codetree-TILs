n, m, k = map(int, input().split())
arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

# 인덱스
k -= 1
row_index = 0
while True:
    cnt = 0
    for i in range(k, k + m):
        if arr[row_index][i] == 0:
            cnt += 1
    # 블럭이 떨어질 자리가 있다는 뜻
    if cnt == m:
        # 다음 행 검사
        row_index += 1
        # 그 다음 행이 index n-1보다 크면 배열 범위를 벗어난 것
        if row_index > n - 1:
            break
        else:
            continue
    # 블럭이 떨어질 자리가 없다는 뜻
    else:
        break

for i in range(k, k + m):
    arr[row_index - 1][i] = 1

for a in arr:
    print(*a)