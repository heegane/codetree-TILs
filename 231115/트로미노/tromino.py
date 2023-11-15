from collections import deque

n, m = map(int, input().split())
graph = []
result = []

for _ in range(n):
    graph.append(list(map(int, input().split())))


def bfs(x, y, li):
    visited[x][y] = 1
    q = deque()
    q.append((x, y))
    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]
    while q:
        current_x, current_y = q.popleft()
        for i in range(4):
            next_x = current_x + dxs[i]
            next_y = current_y + dys[i]
            if 0 <= next_x < n and 0 <= next_y < m:
                if visited[next_x][next_y] == 0:
                    li.append(graph[next_x][next_y])
                    visited[next_x][next_y] = 1

    li.sort(reverse=True)
    return graph[x][y] + li[0] + li[1]


for i in range(n):
    for j in range(m):
        visited = [[0] * m for _ in range(n)]
        li = []
        if visited[i][j] == 0:
            result_value = bfs(i, j, li)
            result.append(result_value)
print(max(result))