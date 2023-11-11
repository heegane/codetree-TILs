n, m, t = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# 움직이는 함수
def move(x, y, move_location):
    max_value, max_x, max_y = arr[x][y], -1, -1
    for i in range(4):
        next_x = x + dx[i]
        next_y = y + dy[i]
        if 0 <= next_x < n and 0 <= next_y < n:
            if max_value < arr[next_x][next_y]:
                max_value = arr[next_x][next_y]
                max_x = next_x
                max_y = next_y
    # 움직임이 없다면
    if max_x == -1 and max_y == -1:
        locations[x][y] = 0
        # 구슬 이동이 없어서 충돌이 나지 않았음을 의미
        move_location[x][y] = -1
    else:
        locations[x][y] = 0
        move_location[max_x][max_y] += 1


# 충돌났는지 확인하는 함수
def check(move_location):
    for i in range(n):
        for j in range(n):
            if move_location[i][j] > 1:
                move_location[i][j] = 0


# 각 구슬의 시작 위치 저장
locations = [[0] * n for _ in range(n)]
for _ in range(m):
    r, c = map(int, input().split())
    locations[r - 1][c - 1] = 1

move_location = [[0] * n for _ in range(n)]
for _ in range(t):
    for i in range(n):
        for j in range(n):
            if locations[i][j] == 1:
                move(i, j, move_location)
    check(move_location)
    locations = move_location

# 구슬의 수 출력
result = 0
for i in range(n):
    for j in range(n):
        if locations[i][j] == 1 or locations[i][j] == -1:
            result += 1
print(result)