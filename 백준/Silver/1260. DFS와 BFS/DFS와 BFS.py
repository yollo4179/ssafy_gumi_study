def dfs(v):
    visited[v] = 1
    vis_list.append(v)

    for w in grid[v]:
        if visited[w] == 0:
            dfs(w)

def bfs(v):
    visited[v] = 1
    vis_list.append(v)
    q = [*grid[v]]

    while q:
        w = q.pop(0)
        if visited[w] == 0:
            visited[w] = 1
            q.extend(grid[w])
            vis_list.append(w)

N, M, V = map(int, input().split())
grid = [[] for _ in range(N+1)]
for _ in range(M):
    s, e = map(int, input().split())
    grid[s].append(e)
    grid[e].append(s)
for i in range(N+1):
    grid[i].sort()
visited = [0] * (N+1)
vis_list = []
dfs(V)
print(*vis_list)
visited = [0] * (N+1)
vis_list = []
bfs(V)
print(*vis_list)