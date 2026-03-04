dxs, dys = [-1, -1, -1, 0, 1, 1, 1, 0], [-1, 0, 1, 1, 1, 0, -1, -1] #좌상부터 시반

def bfs(v):
    r, c = v[0],v[1]
    visited[r][c] = 1
    q = [v]

    while q:
        n = q.pop(0)
        x, y = n[0], n[1]
        for d in range(8):
            nx, ny = x + dxs[d], y + dys[d]
            if 0 <= nx < h and 0 <= ny < w and arr[nx][ny] == 1:
                if visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx,ny))


while True: 
    w, h = map(int, input().split())
    if w == h == 0:
        break
    arr = [list(map(int, input().split())) for _ in range(h)]
    visited = [[0] * w for _ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1 and visited[i][j] == 0:
                bfs((i,j))
                cnt += 1
    print(cnt)