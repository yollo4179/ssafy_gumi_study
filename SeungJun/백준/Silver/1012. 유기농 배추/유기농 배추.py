dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]

def bfs(v):
    q = [v]
    visited[v[1]][v[0]] = 1
    while q:
        w = q.pop(0)
        x, y = w[0], w[1]
        for d in range(4):
            nx, ny = x + dxs[d], y + dys[d]
            if 0 <= nx < m and 0 <= ny < n and arr[ny][nx] and not visited[ny][nx]:
                q.append((nx, ny))
                visited[ny][nx] = 1
            
T = int(input())
for _ in range(T):
    m, n, k = map(int, input().split())
    visited = [[0] * m for _ in range(n)]
    arr = [[0] * m for _ in range(n)]
    cnt = 0
    for _ in range(k):
        x, y = map(int, input().split())
        arr[y][x] = 1

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1 and visited[i][j] == 0:
                bfs((j,i))
                cnt += 1
    print(cnt)
    
