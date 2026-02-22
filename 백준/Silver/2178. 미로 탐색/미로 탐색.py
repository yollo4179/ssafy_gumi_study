n, m = map(int, input().split())
vis = [[0] * m for _ in range(n)]
arr = [list(map(int, input())) for _ in range(n)]
drs, dcs = [-1, 0, 1, 0], [0, 1, 0, -1]

def in_range(r, c):
    return 0<=r<n and 0<=c<m
def bfs(r, c):
    q = [(r,c)]
    vis[r][c] = 1
    while q:
        pos = q.pop(0)
        r, c = pos[0], pos[1]
        for d in range(4):
            nr, nc = r + drs[d], c + dcs[d]
            if in_range(nr, nc) and arr[nr][nc] == 1:
                if vis[nr][nc] == 0:
                    vis[nr][nc] = vis[r][c] + 1
                    q.append((nr,nc))

bfs(0,0)
print(vis[n-1][m-1])