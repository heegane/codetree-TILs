n, m = map(int, input().split())
arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

start_x, start_y = 0, 0
end_x, end_y = n - 1, m - 1
visited = [[0] * m for _ in range(n)]

# 하, 우
dxs = [1, 0]
dys = [0, 1]


def dfs(x, y):
    visited[x][y] = 1
    for i in range(2):
        next_x = x + dxs[i]
        next_y = y + dys[i]
        if 0 <= next_x < n and 0 <= next_y < m:
            if arr[next_x][next_y] == 1 and visited[next_x][next_y] == 0:
                dfs(next_x, next_y)


dfs(start_x, start_y)

if visited[end_x][end_y] == 1:
    print(1)
else:
    print(0)