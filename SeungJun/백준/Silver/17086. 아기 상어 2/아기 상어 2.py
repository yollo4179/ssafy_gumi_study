N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dxs, dys = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]
# 남쪽부터 반시계
def bfs(r,c):
    visited = [[-1] * M for _ in range(N)]
    q = [(r,c)]
    visited[r][c] = 0
    while q:
        x, y = q.pop(0)
        for d in range(8):
            nx, ny = x + dxs[d], y + dys[d]
            if 0<=nx<N and 0<=ny<M and visited[nx][ny] == -1: #방문 안 했으면
                    if arr[nx][ny] == 0: # 그리고 상어가 아니면
                        visited[nx][ny] = visited[x][y] + 1
                        q.append((nx,ny))
                    else: # 상어를 만나면
                        return visited[x][y] + 1

dists = []             
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
             continue
        dists.append(bfs(i,j))

print(max(dists))