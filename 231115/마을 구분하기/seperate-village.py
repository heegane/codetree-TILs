n = int(input())
graph = []
visited = [[0] * n for _ in range(n)]
result = []

for _ in range(n):
    graph.append(list(map(int, input().split())))


def dfs(start_x, start_y):
    global people_num
    visited[start_x][start_y] = 1
    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]
    for i in range(4):
        next_x = start_x + dxs[i]
        next_y = start_y + dys[i]
        if 0 <= next_x < n and 0 <= next_y < n:
            if visited[next_x][next_y] == 0 and graph[next_x][next_y] == 1:
                people_num += 1
                dfs(next_x, next_y)


cnt = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and visited[i][j] == 0:
            cnt += 1
            people_num = 1
            dfs(i, j)
            result.append(people_num)

print(cnt)
result.sort()
for content in result:
    print(content)