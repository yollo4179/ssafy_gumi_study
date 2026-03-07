import sys ; sys.stdin = open('그래프경로input.txt')


def dfs(v):
    # 방문체크
    visited[v] = 1
    # v와 인접한 정점(w) 방문 여부 확인 - 미방문시 dfs(w)
    for w in adj[v]:
        if visited[w] != 1:
            dfs(w)

T = int(input())
for tc in range(1,T+1):
    V, E = map(int, input().split())
    adj = [[] for _ in range(V+1)]
    visited = [0] * (V+1)
    for _ in range(E):
        s, e = map(int, input().split())
        adj[s].append(e)
    S, G = map(int, input().split())
    dfs(S)
    if visited[G] == 1:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')
