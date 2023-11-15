n, m = map(int, input().split())
home_heights = []
result = []

max_height = 0
for _ in range(n):
    datas = list(map(int, input().split()))
    for data in datas:
        if max_height < data:
            max_height = data
    home_heights.append(datas)


def dfs(start_x, start_y, k):
    visited[start_x][start_y] = 1
    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]
    for i in range(4):
        next_x = start_x + dxs[i]
        next_y = start_y + dys[i]
        if 0 <= next_x < n and 0 <= next_y < m:
            if visited[next_x][next_y] == 0 and home_heights[next_x][next_y] > k:
                dfs(next_x, next_y, k)


for k in range(1, max_height + 1):
    cnt = 0
    visited = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if visited[i][j] == 0 and home_heights[i][j] > k:
                cnt += 1
                dfs(i, j, k)
    result.append((cnt, k))

result.sort(key=lambda x: (-x[0], x[1]))
print("%d %d" % (result[0][1], result[0][0]))