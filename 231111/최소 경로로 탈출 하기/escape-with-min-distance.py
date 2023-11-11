from collections import deque

n, m = map(int, input().split())
arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

visited = [[0] * m for _ in range(n)]
step = [[0] * m for _ in range(n)]


def bfs(x, y):
    visited[x][y] = 1
    step[x][y] = 0
    q = deque()
    q.append([x, y])

    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]

    while q:
        x, y = q.popleft()
        for i in range(4):
            next_x = x + dxs[i]
            next_y = y + dys[i]
            if 0 <= next_x < n and 0 <= next_y < m:
                if arr[next_x][next_y] == 1 and visited[next_x][next_y] == 0:
                    visited[next_x][next_y] = 1
                    step[next_x][next_y] = step[x][y] + 1
                    q.append([next_x, next_y])


bfs(0, 0)

if step[n - 1][m - 1] == 0:
    print(-1)
else:
    print(step[n - 1][m - 1])