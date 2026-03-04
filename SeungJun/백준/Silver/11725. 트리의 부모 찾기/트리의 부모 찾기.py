import sys
sys.setrecursionlimit(10**5+1)

def dfs(v):
    visited[v] = 1
    for w in tree[v]:
        if visited[w] == 0:
            par[w] = v # w번 노드의 부모 노드는 v
            dfs(w)

N = int(input())
tree = [[] for _ in range(N+1)]
par = [0] * (N+1)
for _ in range(N-1):
    s, e = map(int, input().split())
    tree[s].append(e)
    tree[e].append(s)
visited = [0] * (N+1)
dfs(1)
for i in range(2, N+1):
    print(par[i])