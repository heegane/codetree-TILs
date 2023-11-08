N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]


def dfs(start):
    visited[start] = True
    for next in graph[start]:
        if visited[next] == False:
            dfs(next)


for _ in range(M):
    start, end = map(int, input().split())
    # 양방향 그래프
    graph[start].append(end)
    graph[end].append(start)

visited = [False] * (N + 1)
dfs(1)
result = 0
for i in range(2, N + 1):
    if visited[i] == True:
        result += 1
print(result)