import sys
sys.setrecursionlimit(10**6)

N = int(input())
grid = [[] for _ in range(N+1)]
dist = {}

def dfs(v): 
    if v == 1:
        vis[v] = 0
    for w in grid[v]:
        if w != 1 and vis[w] == 0:
            if w < v :
                vis[w] = vis[v]+ dist[(w,v)]
                dfs(w)
            else:
                vis[w] = vis[v] + dist[(v,w)]
                dfs(w)
                

for _ in range(N-1):
    a, b, c = map(int, input().split())
    grid[a].append(b)
    grid[b].append(a)
    if a > b :
        a, b = b, a
    dist[(a,b)] = c
vis = [0] * (N+1)
dfs(1)
print(max(vis))