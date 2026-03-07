import sys ; sys.stdin = open('노드의거리input.txt')


def bfs(adj, s_node, e_node):
    dist = [-1] * (V+1)
    q = [s_node]
    dist[s_node] = 0

    while q:
        curr = q.pop(0)

        for w in adj[curr]:
            if dist[w] == -1:
                dist[w] = dist[curr] + 1 # 다음 레벨까지의 거리
                q.append(w)
            if w == e_node:
                return dist[w]
    return 0 # while이 중간에 종료되지 않음 = 전체 탐색하고도 e_node를 찾지 못함


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adj = [[] for _ in range(V+1)]
    for i in range(E): # 인접 노드
        s, e = map(int, input().split())
        adj[s].append(e)
        adj[e].append(s)
    s_node, e_node = map(int, input().split())
    print(f'#{tc} {bfs(adj, s_node, e_node)}')