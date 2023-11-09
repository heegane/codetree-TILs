n, m = map(int, input().split())

# 상하좌우, 대각선까지
dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, 1, -1, 1, -1]
arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))


def move(target_num):
    # 1의 위치 찾기
    x, y = -1, -1
    for i in range(n):
        for j in range(n):
            if arr[i][j] == target_num:
                # 타겟 번호의 인덱스
                x, y = i, j
                break
        if x != -1 and y != -1:
            break

    max_value = -1
    max_x, max_y = -1, -1
    # 인접한 숫자 중에서 큰 값의 인덱스 찾기
    for i in range(8):
        next_x = x + dx[i]
        next_y = y + dy[i]
        if 0 <= next_x < n and 0 <= next_y < n:
            if arr[next_x][next_y] > max_value:
                max_value = arr[next_x][next_y]
                max_x, max_y = next_x, next_y

    # 숫자 이동
    arr[x][y], arr[max_x][max_y] = arr[max_x][max_y], arr[x][y]


for _ in range(m):
    for i in range(1, n * n + 1):
        move(i)

# 출력
for i in range(n):
    print(*arr[i])