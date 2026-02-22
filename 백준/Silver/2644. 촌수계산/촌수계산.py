n = int(input())
a, b = map(int, input().split())
m = int(input())
grid = [[] for _ in range(n+1)]
vis = [-1] * (n+1) 
for _ in range(m):
    p, c = map(int, input().split())
    grid[p].append(c) # p의 자식 중 m이 잇음을 표시
    grid[c].append(p) # 촌수 계산을 위해 양방향

def bfs(v):
    q = [v]
    vis[v] = 0
    while q:
        node = q.pop(0)
        for w in grid[node]:
            if vis[w] == -1:
                vis[w] = vis[node] + 1
                q.append(w)

bfs(a)
print(vis[b])
