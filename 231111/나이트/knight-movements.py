from collections import deque

n = int(input())

dxs = [-1, -2, -2, -1, 1, 2, 2, 1]
dys = [-2, -1, 1, 2, -2, -1, 1, 2]

visited = [[0] * n for _ in range(n)]
step = [[0] * n for _ in range(n)]


def bfs(x, y):
    visited[x][y] = 1
    step[x][y] = 0
    q = deque()
    q.append([x, y])

    while q:
        x, y = q.popleft()
        for i in range(8):
            next_x = x + dxs[i]
            next_y = y + dys[i]
            if 0 <= next_x < n and 0 <= next_y < n:
                if visited[next_x][next_y] == 0:
                    visited[next_x][next_y] = 1
                    step[next_x][next_y] = step[x][y] + 1
                    q.append([next_x, next_y])


r1, c1, r2, c2 = map(int, input().split())
if r1 == r2 and c1 == c2:
    print(0)
else:
    bfs(r1 - 1, c1 - 1)
    if step[r2 - 1][c2 - 1] == 0:
        print(-1)
    else:
        print(step[r2 - 1][c2 - 1])