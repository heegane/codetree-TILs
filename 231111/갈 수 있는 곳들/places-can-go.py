from collections import deque


def bfs(x, y):
    visited[x][y] = 1
    q = deque()
    q.append([x, y])

    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]

    while q:
        x, y = q.popleft()
        for i in range(4):
            next_x = x + dxs[i]
            next_y = y + dys[i]
            if 0 <= next_x < n and 0 <= next_y < n:
                if arr[next_x][next_y] == 0 and visited[next_x][next_y] == 0:
                    visited[next_x][next_y] = 1
                    q.append([next_x, next_y])


n, k = map(int, input().split())

arr = []
result = 0
visited = [[0] * n for _ in range(n)]

for _ in range(n):
    arr.append(list(map(int, input().split())))

for _ in range(k):
    r, c = map(int, input().split())
    bfs(r - 1, c - 1)

for i in range(n):
    for j in range(n):
        if visited[i][j] == 1:
            result += 1
print(result)